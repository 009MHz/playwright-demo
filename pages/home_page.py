from pages.__base import BasePage
from elements.__home import *
from playwright.async_api import Page, expect


class Home(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def open_page(self):
        await self.page.goto(PageInfo.url)
