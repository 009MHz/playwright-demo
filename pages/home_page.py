from pages.__base import BasePage
from elements.__home import *
from playwright.async_api import Page, expect


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.action = HomeInteraction(page)
        self.check = HomeValidation(page)


class HomeInteraction(BasePage):
    async def open_page(self):
        await self.page.goto(PageInfo.url)
        assert 'gov.sg' in self.page.url, f"Incorrect URL: {self.page.url} detected"


class HomeValidation(BasePage):
    async def mini_banner_presence(self):
        await self._look(Header.top_banner)
        await expect(self._find(Header.top_banner)).to_have_text('A Singapore Government Agency Website')
        await expect(self._find(Header.top_banner)).not_to_have_attribute('href', 'https://www.gov.sg')

    async def map_mode_presence(self):
        await self._look(Header.map_mode)
        await expect(self._find(Header.map_mode)).to_be_enabled()
