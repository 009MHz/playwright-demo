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
        pass

    async def password_insert(self, password: str):
        pass

    async def click_login_btn(self):
        pass


class LoginPageValidation(BasePage):
    async def header_presence(self):
        pass

    async def subheader_presence(self):
        pass

    async def username_field(self):
        pass

    async def password_field(self):
        pass

    async def login_button(self):
        pass

