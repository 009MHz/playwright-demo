import logging
import os
from utils.sess_handler import SessionHandler


class Config:
    def __init__(self):
        self.browser = None
        self.page = None
        self.session_handler = None

    def _headless(self):
        return os.getenv("headless", "False").lower() == "true"

    def _browser(self) -> str:
        return os.getenv("browser")

    def _test_mode(self) -> str:
        return os.getenv("mode")

    def _browser_args(self) -> dict:
        launch_args = {
            "args": [
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-gpu"],
            "headless": self._headless()
        }

        if self._browser() == "chromium":
            launch_args["args"].append("--start-maximized")

        return launch_args

    async def setup_browser(self, playwright):
        mode = self._test_mode()
        called_browser = self._browser()
        # logging.info(f"Called browser: {called_browser}")
        
        if mode in ['pipeline', 'local']:
            self.browser = await playwright[called_browser].launch(**self._browser_args())
        elif mode == 'grid':
            server_url = "http://remote-playwright-server:4444"
            self.browser = await playwright[called_browser].connect(server_url)
        else:
            raise ValueError(f"Unsupported execution type: {mode}")

        self.session_handler = SessionHandler(self.browser, self._headless())

    async def context_init(self, storage_state=None, user_type="user"):
        context_options = {
            "viewport": {"width": 1920, "height": 1080},
            "no_viewport": not self._headless()
        }
        
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


logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('filelock').setLevel(logging.CRITICAL)
