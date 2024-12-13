import pytest
from pages.login.login_page import LoginPage
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def login(page):
    login = LoginPage(page)
    with allure.step("▸ Navigate to HerokuApp Login page"):
        await login.action.open_page()
    return login


@allure.epic("Login Page")
@allure.story("Login Page - Unit Test")
@allure.feature("Login Page")
@pytest.mark.positive
@pytest.mark.smoke
class TestSmokeJobPage:
    @allure.title("Login Page Initial Test")
    @allure.severity(severity.CRITICAL)
    async def test_login_initial_state(self, login):
        with allure.step("Check Initial Header existence"):
            await login.check.header_existence()
            await login.check.subheader_presence()

        with allure.step("Check Initial main field existence"):
            await login.check.username_field()
            await login.check.password_field()
            await login.check.login_button()
