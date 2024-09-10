import re
from pages.__base import BasePage
from elements.__home import *
from playwright.async_api import Page, expect


class SchoolQuery(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.action = Interaction(page)
        self.check = Validation(page)


class Interaction(BasePage):
    async def open_page(self):
        await self.page.goto(PageInfo.url, timeout=45000)
        assert 'gov.sg' in self.page.url, f"Incorrect URL: {self.page.url} detected"

    async def click_school_query_toggle(self):
        await self._force(Header.school)
        assert '/#/SchoolQueryInfo' in self.page.url, f"Incorrect URL: {self.page.url} detected"
        await expect(self._find(SchQuery.main)).to_be_visible()

    async def click_kindergarten_btn(self):
        await self._click(SchQuery.Kindergarten.button)
        await expect(self._find(SchQuery.Kindergarten.disclaimer)).to_be_visible()

    async def click_kindergarten_agree_btn(self):
        await self._click(SchQuery.Kindergarten.disc_button)
        await expect(self._find(SchQuery.Kindergarten.result)).to_be_visible()

    async def click_kindergarten_search_result_nearby(self):
        await self._click(SchQuery.Kindergarten.result_option_nearby)
        await expect(self._find(SchQuery.Kindergarten.result_nearby_list)).to_be_visible()

    async def click_primary_school_btn(self):
        await self._click(SchQuery.PrimarySchool.button)
        await expect(self._find(SchQuery.PrimarySchool.disclaimer)).to_be_visible()

    async def click_primary_school_agree_btn(self):
        await self._click(SchQuery.PrimarySchool.disc_button)
        await expect(self._find(SchQuery.PrimarySchool.result)).to_be_visible()

    async def click_primary_school_search_result_nearby(self):
        await self._click(SchQuery.PrimarySchool.result_option_nearby)
        await expect(self._find(SchQuery.PrimarySchool.result_nearby_list)).to_be_visible()

    async def click_secondary_school_btn(self):
        await self._click(SchQuery.SecondarySchool.button)
        await expect(self._find(SchQuery.SecondarySchool.disclaimer)).to_be_visible()

    async def click_secondary_school_agree_btn(self):
        await self._click(SchQuery.SecondarySchool.disc_button)
        await expect(self._find(SchQuery.SecondarySchool.result)).to_be_visible()
        
    async def click_post_second_school_btn(self):
        await self._click(SchQuery.PostSecond.button)
        await expect(self._find(SchQuery.PostSecond.disclaimer)).to_be_visible()

    async def click_post_second_school_agree_btn(self):
        await self._click(SchQuery.PostSecond.disc_button)
        await expect(self._find(SchQuery.PostSecond.result)).to_be_visible()


class Validation(BasePage):
    async def side_menu_initial_state(self):
        await self._look(SchQuery.main)
        await expect(self._find(SchQuery.menu_title)).to_have_text('SCHOOL QUERY')
        
    async def side_menu_close_btn(self):
        await self._look(SchQuery.main)
        await expect(self._find(SchQuery.close)).to_be_enabled()

    async def side_menu_kindergarten_btn(self):
        await self._look(SchQuery.Kindergarten.button)
        await expect(self._find(SchQuery.Kindergarten.button)).to_be_enabled()
        await expect(self._find(SchQuery.Kindergarten.button)).to_have_text('MOE Kindergarten')

    async def side_menu_primary_school_btn(self):
        await self._look(SchQuery.Kindergarten.button)
        await expect(self._find(SchQuery.Kindergarten.button)).to_be_enabled()
        await expect(self._find(SchQuery.Kindergarten.button)).to_have_text('MOE Kindergarten')

    async def search_this_area_dismissal(self):
        await self._conceal(MapSearch.this_area_wrapper)

        await expect(self._find(MapSearch.this_area_btn)).not_to_be_visible()
        await expect(self._find(MapSearch.cancel_area_btn)).not_to_be_visible()

    async def kindergarten_disclaimer_title(self):
        await self._look(SchQuery.Kindergarten.disclaimer)
        await expect(self._find(SchQuery.Kindergarten.disc_title)).to_have_text('Disclaimer - MOE Kindergarten (MK)')

    async def kindergarten_disclaimer_info(self):
        await self._look(SchQuery.Kindergarten.disclaimer)
        await expect(self._find(SchQuery.Kindergarten.disc_info)).to_contain_text('information accurate as of November')
        await expect(self._find(SchQuery.Kindergarten.disc_info)).to_contain_text('to calculate Home-School Distance.')

    async def kindergarten_disclaimer_FAQ(self):
        await self._look(SchQuery.Kindergarten.disclaimer)
        await expect(self._find(SchQuery.Kindergarten.disc_faq)).to_have_text('FAQ on MOE Kindergarten Registration')
        await expect(self._find(SchQuery.Kindergarten.disc_faq)).to_have_attribute(
            'href', re.compile(r'preschool/moe-kindergarten/register'))

    async def kindergarten_disclaimer_agree(self):
        await self._look(SchQuery.Kindergarten.disclaimer)
        await expect(self._find(SchQuery.Kindergarten.disc_button)).to_be_enabled()
        await expect(self._find(SchQuery.Kindergarten.disc_button)).to_have_text('I Agree')

    async def kindergarten_search_result_header(self):
        await self._look(SchQuery.Kindergarten.result)
        await expect(self._find(SchQuery.Kindergarten.result_title)).to_have_text('MOE Kindergarten')
        await expect(self._find(SchQuery.Kindergarten.result_print)).to_be_enabled()
        await expect(self._find(SchQuery.Kindergarten.result_back)).to_be_enabled()

    async def kindergarten_search_result_anchor(self):
        await self._look(SchQuery.Kindergarten.result_option_anchor)
        await expect(self._find(SchQuery.Kindergarten.result_option_anchor)).to_have_text(
            'Find MOE Kindergartens Near a Building')

    async def kindergarten_search_result_anchor_item(self):
        await expect(self._find(SchQuery.Kindergarten.result_anchor_near_title)).to_contain_text('within 500m')
        await expect(self._find(SchQuery.Kindergarten.result_anchor_far_title)).to_contain_text('500m - 1km')

    async def kindergarten_search_result_nearby(self):
        await self._look(SchQuery.Kindergarten.result_option_nearby)
        await expect(self._find(SchQuery.Kindergarten.result_option_nearby)).to_have_text(
            'Find Buildings Near a MOE Kindergarten')

    async def _get_kindergarten_nearby_item(self) -> int:
        item_count = await self._find(SchQuery.Kindergarten.result_nearby_item).count()
        print(f"Retrieved item count: {item_count}")
        return item_count

    async def kindergarten_search_result_nearby_item(self):
        item_limit = await self._get_kindergarten_nearby_item()
        for x in range(1, item_limit + 1):
            curr_item = f"{SchQuery.Kindergarten.result_nearby_item}[{x}]"
            # check_value = await self._find(curr_item).get_attribute('schoolname')
            # print(curr_item, check_value)
            await expect(self._find(curr_item)).to_have_attribute(
                'schoolname', re.compile(r'MOE_KINDERGARTEN_@_'))
            await expect(self._find(curr_item)).to_contain_text('MOE KINDERGARTEN @')

    async def primary_school_disclaimer_title(self):
        await self._look(SchQuery.PrimarySchool.disclaimer)
        await expect(self._find(SchQuery.PrimarySchool.disc_title)).to_have_text('Disclaimer - Primary Schools')

    async def primary_school_disclaimer_info(self):
        await self._look(SchQuery.PrimarySchool.disclaimer)
        await expect(self._find(SchQuery.PrimarySchool.disc_info)).to_contain_text(
            'information accurate as of May 2024')
        await expect(self._find(SchQuery.PrimarySchool.disc_info)).to_contain_text(
            'strictly for the purpose of the Primary One Registration')

    async def primary_school_disclaimer_FAQ(self):
        await self._look(SchQuery.PrimarySchool.disclaimer)
        await expect(self._find(SchQuery.PrimarySchool.disc_faq)).to_have_text('FAQ on MOE Primary One Registration')
        await expect(self._find(SchQuery.PrimarySchool.disc_faq)).to_have_attribute(
            'href', 'https://www.moe.gov.sg/primary/p1-registration/')

    async def primary_school_disclaimer_agree(self):
        await self._look(SchQuery.PrimarySchool.disclaimer)
        await expect(self._find(SchQuery.PrimarySchool.disc_button)).to_be_enabled()
        await expect(self._find(SchQuery.PrimarySchool.disc_button)).to_have_text('I Agree')

    async def primary_school_search_result_header(self):
        await self._look(SchQuery.PrimarySchool.result)
        await expect(self._find(SchQuery.PrimarySchool.result_title)).to_have_text('Primary School')
        await expect(self._find(SchQuery.PrimarySchool.result_print)).to_be_enabled()
        await expect(self._find(SchQuery.PrimarySchool.result_back)).to_be_enabled()

    async def primary_school_search_result_anchor(self):
        await self._look(SchQuery.PrimarySchool.result_option_anchor)
        await expect(self._find(SchQuery.PrimarySchool.result_option_anchor)).to_have_text(
            'Find Schools Near a Building')

    async def primary_school_search_result_anchor_item(self):
        await expect(self._find(SchQuery.PrimarySchool.result_anchor_near_title)).to_contain_text('within 1km')
        await expect(self._find(SchQuery.PrimarySchool.result_anchor_far_title)).to_contain_text('1 - 2km')

    async def primary_school_search_result_nearby(self):
        await self._look(SchQuery.PrimarySchool.result_option_nearby)
        await expect(self._find(SchQuery.PrimarySchool.result_option_nearby)).to_have_text(
            'Find Buildings Near a School')

    async def _get_prim_school_nearby_item(self) -> int:
        item_count = await self._find(SchQuery.PrimarySchool.result_nearby_item).count()
        print(f"Retrieved item count: {item_count}")
        return item_count

    async def primary_school_search_result_nearby_item(self):
        item_limit = await self._get_prim_school_nearby_item()
        for x in range(1, item_limit + 1):
            curr_item = f"{SchQuery.PrimarySchool.result_nearby_item}[{x}]"
            # check_value = await self._find(curr_item).get_attribute('schoolname')
            # print(curr_item, check_value)
            await expect(self._find(curr_item)).not_to_have_text('')

    async def side_menu_secondary_school_btn(self):
        await self._look(SchQuery.SecondarySchool.button)
        await expect(self._find(SchQuery.SecondarySchool.button)).to_be_enabled()
        await expect(self._find(SchQuery.SecondarySchool.button)).to_have_text('Secondary School')

    async def secondary_school_disclaimer_title(self):
        await self._look(SchQuery.SecondarySchool.disclaimer)
        await expect(self._find(SchQuery.SecondarySchool.disc_title)).to_have_text('Disclaimer - Secondary Schools')

    async def secondary_school_disclaimer_info(self):
        await self._look(SchQuery.SecondarySchool.disclaimer)
        await expect(self._find(SchQuery.SecondarySchool.disc_info)).to_contain_text('information accurate')
        await expect(self._find(SchQuery.SecondarySchool.disc_info)).to_contain_text('schools for Secondary 1 admission')

    async def secondary_school_disclaimer_agree(self):
        await self._look(SchQuery.SecondarySchool.disclaimer)
        await expect(self._find(SchQuery.SecondarySchool.disc_button)).to_be_enabled()
        await expect(self._find(SchQuery.SecondarySchool.disc_button)).to_have_text('I Agree')

    async def secondary_school_search_result_header(self):
        await self._look(SchQuery.SecondarySchool.result)
        await expect(self._find(SchQuery.SecondarySchool.result_title)).to_have_text('Secondary School')
        await expect(self._find(SchQuery.SecondarySchool.result_back)).to_be_enabled()

    async def _get_secondary_school_item_count(self) -> int:
        await self._look(SchQuery.SecondarySchool.result_option_item)
        item_count = await self._find(SchQuery.SecondarySchool.result_option_item).count()
        print(f"Retrieved item count: {item_count}")
        return item_count

    async def secondary_school_search_result_item(self):
        item_limit = await self._get_secondary_school_item_count()
        for x in range(1, item_limit + 1):
            curr_item = f"{SchQuery.SecondarySchool.result_option_item}[{x}]"
            # check_value = await self._find(curr_item).get_attribute('schoolname')
            # print(curr_item, check_value)
            await expect(self._find(curr_item)).not_to_have_text('')
            
    async def side_menu_post_second_school_btn(self):
        await self._look(SchQuery.PostSecond.button)
        await expect(self._find(SchQuery.PostSecond.button)).to_be_enabled()
        await expect(self._find(SchQuery.PostSecond.button)).to_have_text('Secondary School')

    async def post_second_school_disclaimer_title(self):
        await self._look(SchQuery.PostSecond.disclaimer)
        await expect(self._find(SchQuery.PostSecond.disc_title)).to_have_text('Disclaimer - Secondary Schools')

    async def post_second_school_disclaimer_info(self):
        await self._look(SchQuery.PostSecond.disclaimer)
        await expect(self._find(SchQuery.PostSecond.disc_info)).to_contain_text('information accurate')
        await expect(self._find(SchQuery.PostSecond.disc_info)).to_contain_text('schools for Secondary 1 admission')

    async def post_second_school_disclaimer_agree(self):
        await self._look(SchQuery.PostSecond.disclaimer)
        await expect(self._find(SchQuery.PostSecond.disc_button)).to_be_enabled()
        await expect(self._find(SchQuery.PostSecond.disc_button)).to_have_text('I Agree')

    async def post_second_school_search_result_header(self):
        await self._look(SchQuery.PostSecond.result)
        await expect(self._find(SchQuery.PostSecond.result_title)).to_have_text('Secondary School')
        await expect(self._find(SchQuery.PostSecond.result_back)).to_be_enabled()

    async def _get_post_second_school_item_count(self) -> int:
        await self._look(SchQuery.PostSecond.result_option_item)
        item_count = await self._find(SchQuery.PostSecond.result_option_item).count()
        print(f"Retrieved item count: {item_count}")
        return item_count

    async def post_second_school_search_result_item(self):
        item_limit = await self._get_post_second_school_item_count()
        for x in range(1, item_limit + 1):
            curr_item = f"{SchQuery.PostSecond.result_option_item}[{x}]"
            # check_value = await self._find(curr_item).get_attribute('schoolname')
            # print(curr_item, check_value)
            await expect(self._find(curr_item)).not_to_have_text('')