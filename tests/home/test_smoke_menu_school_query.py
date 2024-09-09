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
            await school.action.click_school_query_toggle


    # @allure.title("Home Page Main Toggle Interaction")
    # @allure.severity(severity.CRITICAL)
    # @pytest.mark.parametrize("marker_type, feature", [
    #     ("Hawker Centres", "Home/ Map/ Header/ Restaurant"),
    #     ("Medical", "Home/ Map/ Header/ Medical"),
    #     ("Community", "Home/ Map/ Header/ Community"),
    # ])
    # async def test_map_header_interaction_toggle(self, school, marker_type, feature):
    #     allure.dynamic.feature(feature)
    #     with allure.step(f"Interact With {marker_type} Toggle to show the marker"):
    #         if marker_type == "Hawker Centres":
    #             await school.action.show_hawker_centres_marker()
    #         elif marker_type == "Medical":
    #             await school.action.show_medical_marker()
    #         elif marker_type == "Community":
    #             await school.action.show_community_marker()
    #         await school.check.search_this_area_presence()
    #
    #     with allure.step(f"Interact With {marker_type} Toggle again to hide the marker"):
    #         if marker_type == "Hawker Centres":
    #             await school.action.hide_hawker_centres_marker()
    #         elif marker_type == "Medical":
    #             await school.action.hide_medical_marker()
    #         elif marker_type == "Community":
    #             await school.action.hide_community_marker()
    #         await school.check.search_this_area_dismissal()
