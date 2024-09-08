import pytest
from pages.home_page import Home
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def home_page(page):
    home_page = Home(page)
    await home_page.open_page()
    return home_page


@allure.epic("Home")
@allure.story("Smoke Testing: Home Page")
@allure.feature("Home/ Map")
@pytest.mark.positive
@pytest.mark.smoke
class TestSmokeJobPage:
    @allure.title("Home Page Map Validation")
    @allure.severity(severity.CRITICAL)
    async def test_sort_control(self, job_page):
        pass
