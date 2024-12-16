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
            await login.header_presence()
            await login.validate_subheader_presence()

    @allure.title("Login Page Initial State Check: Login Form Component")
    @allure.severity(severity.BLOCKER)
    @allure.feature(
        "Login Page/ Username field",
        "Login Page/ Password field",
        "Login Page/ Login Button")
    async def test_login_initial_state_page_main_form(self, login):
        with allure.step("Check Initial main field existence"):
            await login.username_field()
            await login.password_field()
            await login.login_button()

    @pytest.mark.positive
    @allure.severity(severity.BLOCKER)
    @allure.feature(
        "Login Page/ Username field",
        "Login Page/ Password field",
        "Login Page/ Login Button")
    @allure.title("Normal Login Page Action Flow")
    async def test_login_flow_action(self, login):
        with allure.step("1. Insert a valid username on the username field"):
            await login.username_insert("tomsmith")

        with allure.step("2. Insert a valid password on the password field"):
            await login.password_insert("SuperSecretPassword!")

        with allure.step("3. Click on the Login Button"):
            await login.click_login_btn()

    @pytest.mark.negative
    @allure.severity(severity.NORMAL)
    @allure.feature(
        "Login Page/ Page Info/ Banner",
        "Login Page/ Page Info/ Banner/ Invalid Username")
    @pytest.mark.parametrize("scheme", ["incorrect", "empty"])
    async def test_invalid_name_banner(self, login, scheme):
        if scheme == "incorrect":
            allure.dynamic.title("Invalid username should return the correct banner")
            allure.dynamic.feature("Login Page/ Page Info/ Banner/ Invalid Username/ Incorrect")
            with allure.step("1. Insert the invalid username on the username field"):
                await login.username_insert("PlaywrightQaTest")

        elif scheme == "empty":
            allure.dynamic.title("Empty username should return the correct banner")
            allure.dynamic.feature("Login Page/ Page Info/ Banner/ Invalid Username/ Empty")
            with allure.step("1. Leave the username field empty"):
                pass

        with allure.step("2. Insert a valid password on the password field"):
            await login.password_insert("SuperSecretPassword!")

        with allure.step("3. Click on the Login Button"):
            await login.click_login_btn()

        with allure.step("4. Verify the invalid username banner"):
            await login.invalid_banner_username()

        with allure.step("5. Close the invalid username banner"):
            await login.close_invalid_user_banner()

    @pytest.mark.negative
    @pytest.mark.parametrize("scheme", ["incorrect", "empty"])
    @allure.severity(severity.NORMAL)
    @allure.feature(
        "Login Page/ Page Info/ Banner",
        "Login Page/ Page Info/ Banner/ Invalid Password")
    async def test_invalid_password_banner(self, login, scheme):
        with allure.step("1. Insert a valid username in the username field"):
            await login.username_insert("tomsmith")

        if scheme == "incorrect":
            allure.dynamic.title("Invalid password should return the correct banner")
            allure.dynamic.feature("Login Page/ Page Info/ Banner/ Invalid Password/ Incorrect")
            with allure.step("2. Insert the invalid username on the username field"):
                await login.password_insert("PlaywrightQaTest")

        elif scheme == "empty":
            allure.dynamic.title("Empty password should return the correct banner")
            allure.dynamic.feature("Login Page/ Page Info/ Banner/ Invalid Password/ Empty")
            with allure.step("2. Leave the password field empty"):
                pass

        with allure.step("3. Click on the Login Button"):
            await login.click_login_btn()

        with allure.step("4. Verify the invalid password banner"):
            await login.invalid_banner_password()

        with allure.step("5. Close the invalid password banner"):
            await login.close_invalid_password_banner()
