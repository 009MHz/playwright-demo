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
@pytest.mark.smoke
class TestLoginInitPage:
    @pytest.mark.positive
    @allure.title("Login Page Initial State Check: Page Header & Information")
    @allure.severity(severity.NORMAL)
    @allure.feature("Login Page/ Page Info/ Header")
    async def test_login_initial_state_page_header(self, login):
        with allure.step("Check Initial Header existence"):
            await login.check.header_presence()
            await login.check.subheader_presence()

    @allure.title("Login Page Initial State Check: Login Form Component")
    @allure.severity(severity.BLOCKER)
    @allure.feature(
        "Login Page/ Username field",
        "Login Page/ Password field",
        "Login Page/ Login Button")
    async def test_login_initial_state_page_main_form(self, login):
        with allure.step("Check Initial main field existence"):
            await login.check.username_field()
            await login.check.password_field()
            await login.check.login_button()

    @pytest.mark.positive
    @allure.title("Normal Login Page Action Flow")
    @allure.severity(severity.CRITICAL)
    async def test_login_flow_action(self, login):
        with allure.step("1. Insert a valid username on the username field"):
            await login.action.username_insert("tomsmith")

        with allure.step("2. Insert a valid password on the password field"):
            await login.action.password_insert("SuperSecretPassword!")

        with allure.step("3. Click on the Login Button"):
            await login.action.click_login_btn()

        # with allure.step("4. Verify the success login state"):
        #     await login.check.success_login()
