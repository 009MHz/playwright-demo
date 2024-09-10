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
    @pytest.mark.parametrize("school_type, feature", [
        ("Kindergarten", "Home/ Map/ Header/ School Query/ Kindergarten"),
        ("Primary School", "Home/ Map/ Header/ School Query/ Primary School"),
        ("Secondary School", "Home/ Map/ Header/ School Query/ Secondary School"),
    ])
    async def test_school_query_component(self, school, school_type, feature):
        allure.dynamic.feature(feature)
        with allure.step("Click on the School Query Toggle"):
            await school.action.click_school_query_toggle()

        with allure.step("Verify that the School Query Side menu is exist and interactable"):
            await school.check.side_menu_initial_state()
            await school.check.side_menu_close_btn()

        with allure.step(f"Click on the side menu {school_type} button"):
            if school_type == "Kindergarten":
                await school.action.click_kindergarten_btn()
            elif school_type == "Primary School":
                await school.action.click_primary_school_btn()

        with allure.step(f"Verify the {school_type} disclaimer"):
            if school_type == "Kindergarten":
                await school.check.kindergarten_disclaimer_title()
                await school.check.kindergarten_disclaimer_info()
                await school.check.kindergarten_disclaimer_FAQ()
                await school.check.kindergarten_disclaimer_agree()
            elif school_type == "Primary School":
                await school.check.primary_school_disclaimer_title()
                await school.check.primary_school_disclaimer_info()
                await school.check.primary_school_disclaimer_FAQ()
                await school.check.primary_school_disclaimer_agree()
            elif school_type == "Secondary School":
                await school.check.secondary_school_disclaimer_title()
                await school.check.secondary_school_disclaimer_info()
                await school.check.secondary_school_disclaimer_agree()

        with allure.step(f"Click on the {school_type} disclaimer Agree button"):
            if school_type == "Kindergarten":
                await school.action.click_kindergarten_agree_btn()
            elif school_type == "Primary School":
                await school.action.click_primary_school_agree_btn()
            elif school_type == "Secondary School":
                await school.action.click_secondary_school_agree_btn()

        with allure.step(f"Verify the {school_type} Search Result"):
            if school_type == "Kindergarten":
                await school.check.kindergarten_search_result_header()
                await school.check.kindergarten_search_result_anchor('Find MOE Kindergartens Near a Building')
                await school.check.kindergarten_search_result_anchor_item()

                with allure.step(f"Click on the {school_type} Search Result Nearby option window"):
                    await school.action.click_kindergarten_search_result_nearby()

                with allure.step(f"Verify the {school_type} Search Result Nearby option window"):
                    await school.check.kindergarten_search_result_nearby()
                    await school.check.kindergarten_search_result_nearby_item()
            elif school_type == "Primary School":
                await school.check.primary_school_search_result_header()
                await school.check.primary_school_search_result_anchor()
                await school.check.primary_school_search_result_anchor_item()

                with allure.step(f"Click on the {school_type} Search Result Nearby option window"):
                    await school.action.click_primary_school_search_result_nearby()

        with allure.step(f"Verify the {school_type} Search Result Nearby option window"):
            if school_type == "Kindergarten":
                await school.check.kindergarten_search_result_nearby('Find Buildings Near a MOE Kindergarten')
                await school.check.kindergarten_search_result_nearby_item(re.compile(r'MOE_KINDERGARTEN_@_'), 'MOE KINDERGARTEN @')
            elif school_type == "Primary School":
                await school.check.primary_school_search_result_nearby('Find Buildings Near a Primary School')
                await school.check.primary_school_search_result_nearby_item(re.compile(r'PRIMARY_SCHOOL_@_'), 'PRIMARY SCHOOL @')
                with allure.step(f"Verify the {school_type} Search Result Nearby option window"):
                    await school.check.primary_school_search_result_nearby()