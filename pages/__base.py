from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _find(self, locator: str):
        return self.page.locator(locator)

    async def _look(self, locator: str, timeout: int = 10000):
        await self.page.wait_for_selector(locator, state='visible', timeout=timeout)

    async def _conceal(self, locator: str, timeout: int = 7000):
        await self.page.wait_for_selector(locator, state='hidden', timeout=timeout)

    async def _touch(self, locator: str, timeout: int = 10000):
        await self._look(locator)
        await self.page.locator(locator).is_enabled(timeout=timeout)

    async def _type(self, locator: str, text: str, timeout: int = 10000):
        await self._look(locator, timeout)
        await self.page.locator(locator).fill(text)

    async def _click(self, locator: str, timeout: int = 10000):
        await self._touch(locator, timeout=timeout)
        await self.page.locator(locator).click()

    async def _double_click(self, locator: str, timeout: int = 10000):
        await self._touch(locator, timeout=timeout)
        await self.page.locator(locator).dblclick()

    async def _force(self, locator: str, timeout: int = 10000):
        await self._look(locator, timeout)
        await self.page.locator(locator).click(force=True, delay=500)
