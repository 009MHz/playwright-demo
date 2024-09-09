import pytest
from pages.home_page import *
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def home_page(page):
    home_page = HomePage(page)
    with allure.step("▸ Navigate to onemap home page"):
        await home_page.action.open_page()
    return home_page


@allure.epic("Home")
@allure.story("Smoke Testing: Home Page")
@allure.feature("Home/ Map/ Header")
@pytest.mark.positive
@pytest.mark.smoke
class TestSmokeJobPage:
    @allure.title("Home Page Map Main Validation")
    @allure.severity(severity.CRITICAL)
    @pytest.mark.parametrize("action, feature", [
        ("header", "Home/ Map Header"),
        ("bottom menu", "Home/ Bottom Menu"),
        ("footer", "Home/ Footer"),
        ])
    async def test_home_page_component(self, home_page, action, feature):
        allure.dynamic.feature(feature)
        if action == "header":
            with allure.step("Validate that the Map Header is exist and enabled"):
                await home_page.check.mini_banner()
                await home_page.check.search_menu()
                await home_page.check.community_toggle()
                await home_page.check.school_toggle()
                await home_page.check.medical_toggle()
                await home_page.check.restaurant_toggle()
                await home_page.check.map_mode3D()
        elif action == "bottom menu":
            with allure.step("Validate that the Map Bottom Menu is exist and accessible"):
                await home_page.check.map_drawer()
                await home_page.check.share_button()
                await home_page.check.get_my_location()
                await home_page.check.zoom_in_button()
                await home_page.check.zoom_out_button()

        elif action == "footer":
            with allure.step("Validate that the Footer Menu is exist and accessible"):
                await home_page.check.one_map_icon()
                await home_page.check.map_legend()
                await home_page.check.year_license()
                await home_page.check.contact_us()
                await home_page.check.terms_of_use()
                await home_page.check.report_cta()

    @allure.title("Home Page Main Toggle Interaction")
    @allure.severity(severity.CRITICAL)
    @pytest.mark.parametrize("marker_type, feature", [
        ("Hawker Centres", "Home/ Map/ Header/ Restaurant"),
        ("Medical", "Home/ Map/ Header/ Medical"),
        ("Community", "Home/ Map/ Header/ Community"),
    ])
    async def test_map_header_interaction_toggle(self, home_page, marker_type, feature):
        allure.dynamic.feature(feature)
        with allure.step(f"Interact With {marker_type} Toggle to show the marker"):
            if marker_type == "Hawker Centres":
                await home_page.action.show_hawker_centres_marker()
            elif marker_type == "Medical":
                await home_page.action.show_medical_marker()
            elif marker_type == "Community":
                await home_page.action.show_community_marker()
            await home_page.check.search_this_area_presence()

        with allure.step(f"Interact With {marker_type} Toggle again to hide the marker"):
            if marker_type == "Hawker Centres":
                await home_page.action.hide_hawker_centres_marker()
            elif marker_type == "Medical":
                await home_page.action.hide_medical_marker()
            elif marker_type == "Community":
                await home_page.action.hide_community_marker()
            await home_page.check.search_this_area_dismissal()
