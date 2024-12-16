import re

from pages.__base import BasePage
from elements.__login import *
from playwright.async_api import Page, expect


class SuccessPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """# Success Page Interaction"""
    async def close_banner(self):
        await self._click(PageInfo.banner_close)
        await expect(self._find(PageInfo.banner_main)).not_to_be_visible()

    async def click_logout(self):
        await self._click(PostSuccess.logout_btn)

    """# Success Page Validation"""
    async def validate_url_redirection(self):
        url_redir = self.page.url
        assert "secure" in url_redir

    async def banner_presence(self):
        await self._look(PageInfo.banner_main)
        await expect(self._find(PageInfo.banner_main)).to_contain_text("You logged into a secure area!")
        await self._capture("Success Login Banner")

    async def banner_close_btn(self):
        await self._look(PageInfo.banner_close)
        await expect(self._find(PageInfo.banner_close)).to_be_enabled()

    async def header_presence(self):
        await self._look(PageInfo.header)
        page_header = await self._find(PageInfo.header).text_content()
        assert "Secure Area" in page_header, f"The Current page title:{page_header} not match with 'Secure Area'"

    async def subheader_presence(self):
        await self._look(PageInfo.sub_header)
        await expect(self._find(PageInfo.sub_header)).to_have_text(
            "Welcome to the Secure Area. When you are done click logout below.")

    async def logout_btn_presence(self):
        await self._look(PostSuccess.logout_btn)
        await expect(self._find(PostSuccess.logout_btn)).to_be_enabled()
        await expect(self._find(PostSuccess.logout_btn)).to_have_text("Logout")
        await self._capture("Logout Button Presence")
