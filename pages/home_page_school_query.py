import re
from pages.__base import BasePage
from elements.__home import *
from playwright.async_api import Page, expect


class SchoolQuery(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.action = Interaction(page)
        self.check = Validation(page)


class Interaction(BasePage):
    async def open_page(self):
        await self.page.goto(PageInfo.url)
        assert 'gov.sg' in self.page.url, f"Incorrect URL: {self.page.url} detected"

    async def click_school_query_toggle(self):
        await self._force(Header.school)
        await expect(self._find(SchoolQuery.main)).to_be_visible()

    async def hide_hawker_centres_marker(self):
        await expect(self._find(Header.restaurant)).to_have_attribute('class', re.compile(r'btnactive'))

        await self._click(Header.restaurant)
        await expect(self._find(Header.restaurant)).not_to_have_attribute('class', re.compile(r'btnactive'))


class Validation(BasePage):
    async def mini_banner(self):
        await self._look(Header.top_banner)
        await expect(self._find(Header.top_banner)).to_have_text('A Singapore Government Agency Website')
        await expect(self._find(Header.top_banner)).not_to_have_attribute('href', 'https://www.gov.sg')
        
    async def school_toggle(self):
        await self._look(Header.school)
        await expect(self._find(Header.school)).to_be_enabled()
        await expect(self._find(Header.school)).to_have_text('School Query')


    async def search_this_area_dismissal(self):
        await self._conceal(MapSearch.this_area_wrapper)

        await expect(self._find(MapSearch.this_area_btn)).not_to_be_visible()
        await expect(self._find(MapSearch.cancel_area_btn)).not_to_be_visible()
