import pytest
from pages.home_page import *
import allure
from allure import severity_level as severity

@pytest.fixture(scope='function')
async def home_page(page):
    home_page = HomePage(page)
    with allure.step("▸ Navigate to resume builder page"):
        await home_page.action.open_page()
    return home_page


@allure.epic("Home")
@allure.story("Smoke Testing: Home Page")
@allure.feature("Home/ Map")
@pytest.mark.positive
@pytest.mark.smoke
class TestSmokeJobPage:
    @allure.title("Home Page Map Validation")
    @allure.severity(severity.CRITICAL)
    async def test_home_page_component(self, home_page):
        await home_page.check.mini_banner_presence()
        await home_page.check.map_mode_presence()
