from pages.login.login_page import LoginPage
from playwright.async_api import Page, expect
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LoginInit(LoginPage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def create_session(self, username: str, password: str):
        logger.info("Opening Login Page")
        await self.open_page()
        logger.info(f"Providing username type: {username}")
        await self.username_insert(username)
        logger.info("Providing Valid Password")
        await self.password_insert(password)
        await self.click_login_btn()
        assert r'/secure' in self.page.url
