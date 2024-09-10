import pytest
from pages.home_page_school_query import *
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def school(page):
    sch_query = SchoolQuery(page)
    with allure.step("▸ Navigate to onemap home page"):
        await sch_query.action.open_page()
    return sch_query


@allure.epic("Home")
@allure.story("Smoke Testing: Home Page")
@allure.feature("Home/ Map/ Header")
@pytest.mark.positive
@pytest.mark.smoke
class TestSmokeJobPage:
    @allure.feature("Home/ Map/ Header/ School Query")
    @allure.title("Home Page School Toggle Interaction")
    @allure.severity(severity.CRITICAL)
    async def test_school_query_component(self, school):
        with allure.step("Click on the School Query Toggle"):
            await school.action.click_school_query_toggle()

        with allure.step("Verify that the School Query Side menu is exist and interactable"):
            await school.check.side_menu_initial_state()
            await school.check.side_menu_close_btn()
            await school.check.side_menu_kindergarten_btn()

        with allure.step("Click on the side menu {feature} button "):
            await school.action.click_kindergarten_btn()

        with allure.step("Verify the {feature} disclaimer "):
            await school.check.kindergarten_disclaimer_title()
            await school.check.kindergarten_disclaimer_info()
            await school.check.kindergarten_disclaimer_FAQ()
            await school.check.kindergarten_disclaimer_agree()

        with allure.step("Click on the {feature} disclaimer Agree button "):
            await school.action.click_kindergarten_agree_btn()

        with allure.step("Verify the {feature} Search Result Anchor option window"):
            await school.check.kindergarten_search_result_header()
            await school.check.kindergarten_search_result_anchor()
            await school.check.kindergarten_search_result_anchor_item()

        with allure.step("Click on the {feature} Search Result Nearby option window"):
            await school.action.click_kindergarten_search_result_nearby()

        with allure.step("Verify the {feature} Search Result Nearby option window"):
            await school.check.kindergarten_search_result_nearby()
            await school.check.kindergarten_search_result_nearby_item()

