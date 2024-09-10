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

    async def side_menu_prime_school_btn(self):
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

    async def _get_nearby_item(self) -> int:
        item_count = await self._find(SchQuery.Kindergarten.result_nearby_item).count()
        print(f"Retrieved item count: {item_count}")
        return item_count

    async def kindergarten_search_result_nearby_item(self):
        item_limit = await self._get_nearby_item()
        for x in range(1, item_limit + 1):
            curr_item = f"{SchQuery.Kindergarten.result_nearby_item}[{x}]"
            # check_value = await self._find(curr_item).get_attribute('schoolname')
            # print(curr_item, check_value)
            await expect(self._find(curr_item)).to_have_attribute(
                'schoolname', re.compile(r'MOE_KINDERGARTEN_@_'))
            await expect(self._find(curr_item)).to_contain_text('MOE KINDERGARTEN @')
