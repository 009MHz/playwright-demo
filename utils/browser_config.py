import os
import logging


class Config:
    def __init__(self):
        self.browsers = {}
        self.page = None
        self.session_handler = None

    def is_headless(self):
        return os.getenv("headless") == "True"

    async def setup_browser(self, playwright, browser_type=None):
        browser_type = browser_type or os.getenv("BROWSER", "chromium")

        if browser_type in self.browsers:
            self.browser = self.browsers[browser_type]
            return

        mode = os.getenv("mode")
        headless = self.is_headless()
        launch_args = {
            "headless": headless,
            "args": ["--start-maximized"]}

        if mode == 'pipeline':
            self.browser = await playwright[browser_type].launch(**launch_args)
        elif mode == 'local':
            self.browser = await playwright[browser_type].launch(**launch_args)
        elif mode == 'grid':
            server_url = "http://remote-playwright-server:4444"
            self.browser = await playwright[browser_type].connect(server_url)
        else:
            raise ValueError(f"Unsupported execution type: {mode}")

        self.browsers[browser_type] = self.browser

    async def context_init(self, storage_state=None, user_type="user"):
        context_options = {
            "viewport": {"width": 1920, "height": 1080} if self.is_headless() else None,
            "no_viewport": not self.is_headless()}

        if storage_state:
            context_options["storage_state"] = await self.session_handler.create_session(user_type)

        return await self.browser.new_context(**context_options)

    async def setup_page(self):
        context = await self.context_init()
        self.page = await context.new_page()
        return self.page

    async def setup_auth_page(self, auth_mode: str):
        context = await self.context_init(storage_state=True, user_type=auth_mode)
        self.page = await context.new_page()
        return self.page

    async def capture_handler(self):
        screenshot_option = os.getenv("screenshot", "off")
        if screenshot_option != "off":
            screenshot_path = f"reports/screenshots/{await self.page.title()}.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            await self.page.screenshot(path=screenshot_path, full_page=True)


logging.getLogger('asyncio').setLevel(logging.CRITICAL)
