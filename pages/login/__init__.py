import os
import allure
from playwright.async_api import Page, expect
from elements.__login import *
from pages.__base import BasePage


class PreCond(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def load_login_page(self):
        with allure.step("▸ Navigate to HerokuApp Login page"):
            await self.page.goto(Url.login)
            assert r'/login' in self.page.url, f"Incorrect URL: {self.page.url} detected"

    async def load_success_page(self):
        await self.load_login_page()

        with allure.step("▸ Login with a valid account"):
            await self._type(Interactor.username_input, os.getenv("USERNAME_COMMON"))
            await self._type(Interactor.password_input, os.getenv("PASSWORD_COMMON"))
            await self._click(Interactor.login_btn)
            assert 'secure' in self.page.url, f"Login failed, incorrect URL: {self.page.url}"
