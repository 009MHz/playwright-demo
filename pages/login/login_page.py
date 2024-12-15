import re
from pages.__base import BasePage
from elements.__login import *
from playwright.async_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.action = LogInPageInteraction(page)
        self.check = LoginPageValidation(page)


class LogInPageInteraction(BasePage):
    async def open_page(self):
        await self.page.goto(Url.login)
        assert r'/login' in self.page.url, f"Incorrect URL: {self.page.url} detected"

    async def username_insert(self, username: str):
        await expect(self._find(Interactor.username_input)).to_be_empty()
        await self._type(Interactor.username_input, username)
        await expect(self._find(Interactor.username_input)).not_to_be_empty()

    async def password_insert(self, password: str):
        await expect(self._find(Interactor.password_input)).to_be_empty()
        await self._type(Interactor.password_input, password)
        await expect(self._find(Interactor.password_input)).not_to_be_empty()

    async def click_login_btn(self):
        await self._click(Interactor.login_btn)

    async def close_success_banner(self):
        await expect(self._find(PageInfo.banner_main)).to_contain_text("You logged out of the secure area!")
        await self._click(PageInfo.banner_close)
        await expect(self._find(PageInfo.banner_main)).not_to_be_visible()


class LoginPageValidation(BasePage):
    async def header_presence(self):
        await self._look(PageInfo.header)
        page_header = await self._find(PageInfo.header).text_content()
        assert page_header == "Login Page", f"The Current page title:{page_header} not match with 'Login Page'"

    async def subheader_presence(self):
        await self._look(PageInfo.sub_header)
        await expect(self._find(PageInfo.sub_header)).to_contain_text(
            "This is where you can log into the secure area")
        await expect(self._find(PageInfo.sub_header)).to_contain_text(
            "If the information is wrong you should see error messages")

    async def username_field(self):
        await self._look(Interactor.username_label)
        await expect(self._find(Interactor.username_label)).to_have_text("Username")
        
        await self._look(Interactor.username_input)
        await expect(self._find(Interactor.username_input)).to_be_enabled()
        await expect(self._find(Interactor.username_input)).to_have_value('')

    async def password_field(self):
        await self._look(Interactor.password_label)
        await expect(self._find(Interactor.password_label)).to_have_text("Password")

        await self._look(Interactor.password_input)
        await expect(self._find(Interactor.password_input)).to_be_enabled()
        await expect(self._find(Interactor.password_input)).to_have_value('')

    async def login_button(self):
        await self._look(Interactor.login_btn)
        await expect(self._find(Interactor.login_btn)).to_be_enabled()
        await expect(self._find(Interactor.login_btn)).to_contain_text("Login")

    async def logout_banner_presence(self):
        await self._look(PageInfo.banner_main)
        await expect(self._find(PageInfo.banner_main)).to_contain_text("You logged out of the secure area!")

    async def logout_banner_close(self):
        await self._look(PageInfo.banner_close)
        await expect(self._find(PageInfo.banner_close)).to_be_enabled()
