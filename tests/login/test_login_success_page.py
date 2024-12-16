import pytest
from pages.login.success_page import SuccessPage
from pages.login.login_page import LoginPage
from pages.login import PreCond
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def login(page):
    login = LoginPage(page)
    return login


@pytest.fixture(scope='function')
async def success(page):
    success = SuccessPage(page)
    pre_cond = PreCond(success.page)
    await pre_cond.load_success_page()
    return success


@allure.epic("Login Success Page")
@allure.story("Login Success Page - Unit Test")
@pytest.mark.smoke
class TestLoginSuccessPage:
    @pytest.mark.positive
    @allure.severity(severity.NORMAL)
    @pytest.mark.parametrize(
        "section", [
            "header",
            "logout"]
    )
    async def test_login_success_initial_state(self, success, section):
        with allure.step("Check URL redirection match"):
            await success.validate_url_redirection()

        if section == "header":
            allure.dynamic.title("Login Success Initial State Check: Page Header & Information")
            allure.dynamic.severity(allure.severity_level.NORMAL)
            allure.dynamic.feature("Login Success/ Page Info/ Header")

            with allure.step("Check Initial Header existence"):
                await success.banner_presence()
                await success.banner_close_btn()
                await success.header_presence()
                await success.subheader_presence()

            with allure.step("Check Initial Banner functionality"):
                await success.close_banner()

        elif section == "logout":
            allure.dynamic.title("Login Page Initial State Check: Logout Component")
            allure.dynamic.severity(allure.severity_level.CRITICAL)
            allure.dynamic.feature("Login Success/ Logout Button")

            with allure.step("Check Logout button existence"):
                await success.logout_btn_presence()

            with allure.step("Check Logout button functionality"):
                await success.click_logout()

    @allure.title("Logout action should returns to Login Page with correct information")
    @allure.severity(severity.CRITICAL)
    @allure.feature("Login Success/ Logout Action")
    async def test_login_success_logout_flow(self, success, login):
        with allure.step("Click on the Logout button"):
            await success.click_logout()

        with allure.step("Verify the URL redirection"):
            await login.url_redirection()

        with allure.step("Verify the logout banner existence"):
            await login.logout_banner_presence()
            await login.logout_banner_close()

        with allure.step("Interact with logout banner"):
            await login.close_success_banner()

        with allure.step("Verify the Login Page Information"):
            await login.header_presence()
            await login.validate_subheader_presence()

        with allure.step("Verify the Login Page main form state"):
            await login.password_field()
            await login.username_field()
            await login.login_button()
