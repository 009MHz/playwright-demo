import re
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
    """Header"""
    async def mini_banner(self):
        await self._look(Header.top_banner)
        await expect(self._find(Header.top_banner)).to_have_text('A Singapore Government Agency Website')
        await expect(self._find(Header.top_banner)).not_to_have_attribute('href', 'https://www.gov.sg')

    async def map_mode(self):
        await self._look(Header.map_mode)
        await expect(self._find(Header.map_mode)).to_be_enabled()
        await expect(self._find(Header.map_mode)).not_to_have_attribute('class', 'active')
        
    async def search_menu(self):
        await self._look(Header.search)
        await expect(self._find(Header.search)).to_be_enabled()
        
    async def community_toggle(self):
        await self._look(Header.community)
        await expect(self._find(Header.community)).to_be_enabled()
        await expect(self._find(Header.community)).to_have_text('Community')
        
    async def school_toggle(self):
        await self._look(Header.school)
        await expect(self._find(Header.school)).to_be_enabled()
        await expect(self._find(Header.school)).to_have_text('School Query')
        
    async def medical_toggle(self):
        await self._look(Header.medical)
        await expect(self._find(Header.medical)).to_be_enabled()
        await expect(self._find(Header.medical)).to_have_text('Medical')
        
    async def restaurant_toggle(self):
        await self._look(Header.restaurant)
        await expect(self._find(Header.restaurant)).to_be_enabled()
        await expect(self._find(Header.restaurant)).to_have_text('Hawker Centres')
        
    async def map_mode3D(self):
        await self._look(Header.map_mode)
        await expect(self._find(Header.map_mode)).to_be_enabled()

    """Bottom Menu"""
    async def map_drawer(self):
        await self._look(BottomMenu.Drawer.button)
        await expect(self._find(BottomMenu.Drawer.button)).to_be_enabled()
        
    async def share_button(self):
        await self._look(BottomMenu.share)
        await expect(self._find(BottomMenu.share)).to_be_enabled()
        
    async def get_my_location(self):
        await self._look(BottomMenu.my_loc)
        await expect(self._find(BottomMenu.my_loc)).to_be_enabled()

    async def zoom_in_button(self):
        await self._look(BottomMenu.zoom_in)
        await expect(self._find(BottomMenu.zoom_in)).to_be_enabled()

    async def zoom_out_button(self):
        await self._look(BottomMenu.zoom_out)
        await expect(self._find(BottomMenu.zoom_out)).to_be_enabled()

    """Footer"""
    async def one_map_icon(self):
        await expect(self._find(BottomMenu.zoom_out)).to_be_visible()

    async def map_legend(self):
        await self._look(BottomMenu.legend)
        await expect(self._find(BottomMenu.legend)).to_contain_text(re.compile(r'm|km'))

    async def year_license(self):
        await self._look(BottomMenu.footer_year)
        await expect(self._find(BottomMenu.footer_year)).to_have_text('Map data ©2023 SLA')
        await expect(self._find(BottomMenu.footer_year)).to_have_attribute('href', 'mailto:onemap@sla.gov.sg')

    async def contact_us(self):
        await self._look(BottomMenu.footer_contact)
        await expect(self._find(BottomMenu.footer_contact)).to_have_attribute("href", "mailto:onemap@sla.gov.sg")

    async def terms_of_use(self):
        t_o_u = self.page.locator('.footerLinks a', has_text='Terms of Use')
        await expect(t_o_u).to_have_attribute('href', 'https://www.onemap.gov.sg/legal/termsofuse.html')

    async def report_cta(self):
        reporter = self.page.locator('.footerLinks a', has_text='Report Vulnerability')
        await expect(reporter).to_have_attribute('href', 'https://www.tech.gov.sg/report_vulnerability')
