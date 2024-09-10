class PageInfo:
    url = "https://www.onemap.gov.sg/"


class Header:
    top_banner = "#view-banner-gov-sg"
    search = ".search-location-wrapper"
    community = "#Community"
    school = "#SchoolQueryInfo"
    medical = "#Medical"
    restaurant = "#HawkerCentres"
    map_mode = "#btn2D3D"
    map_ball = ".compass"


class MapSearch:
    this_area_wrapper = "#searchHereDiv"
    this_area_btn = "#searchHerebtn"
    cancel_area_btn = "#cancelSearch"


class SchQuery:
    main = "#schoolQueryContainer"
    close = ".sqOptionBack"
    menu_title = ".schoolQueryTitleBlock"

    class Kindergarten:
        button = "#kindergarten"
        disclaimer = "div[id='disclaimerBlk_kindergarten']"
        disc_title = f"{disclaimer} .schoolQueryDisclaimerBlockTitle"
        disc_info = f"{disclaimer} .schoolQueryDisclaimerBlockContent"
        disc_faq = f"{disclaimer} .schoolFAQItem a"
        disc_button = "#schoolQueryDisclaimerBlockBtn_kindergarten"
        result = "//div[@id='categoryBlk_kindergarten' and contains(@class,'schoolQueryCatContentBlock')]"
        result_title = f"{result}//div[@class='schoolQueryCatTitle']"
        result_print = "#schoolQueryPrintBtn"
        result_back = "#schoolQueryCatBackBtn"
        result_option = "//div[@id='optionSchoolSearch_kindergarten']"
        result_option_anchor = f"{result_option}//div[@id='nearbySchoolOpt']"
        result_anchor_near_title = "(//div[@class='bufferTitle'])[1]"
        result_anchor_far_title = "(//div[@class='bufferTitle'])[2]"
        result_option_nearby = f"{result_option}//div[@id='nearbySchoolOptTwo']"
        result_nearby_list = "#schoolQueryAllResultsList_kindergarten"
        result_nearby_item = "(//div[@id='schoolListItemkindergarten'])"

    class PrimarySchool:
        button = "#priSchool"
        disclaimer = "#disclaimerBlk_priSchool"
        disc_title = f"{disclaimer} .schoolQueryDisclaimerBlockTitle"
        disc_info = f"{disclaimer} .schoolQueryDisclaimerBlockContent"
        disc_faq = f"{disclaimer} .schoolFAQItem a"
        disc_button = "#schoolQueryDisclaimerBlockBtn_priSchool"
        result = "//div[@id='categoryBlk_priSchool' and contains(@class,'schoolQueryCatContentBlock')]"
        result_title = f"{result}//div[@class='schoolQueryCatTitle']"
        result_print = "#schoolQueryPrintBtn"
        result_back = "#schoolQueryCatBackBtn"
        result_option = "//div[@id='optionSchoolSearch_priSchool']"
        result_option_anchor = f"{result_option}//div[@id='nearbySchoolOpt']"
        result_anchor_near_title = "(//div[@class='bufferTitle'])[1]"
        result_anchor_far_title = "(//div[@class='bufferTitle'])[2]"
        result_option_nearby = f"{result_option}//div[@id='nearbySchoolOptTwo']"
        result_nearby_list = "#schoolQueryAllResultsList_priSchool"
        result_nearby_item = "(//div[@id='schoolListItempriSchool'])"

    class SecondarySchool:
        button = "#secSchool"
        disclaimer = "div[id='disclaimerBlk_secSchool']"
        disc_title = f"{disclaimer} .schoolQueryDisclaimerBlockTitle"
        disc_info = f"{disclaimer} .schoolQueryDisclaimerBlockContent"
        disc_faq = f"{disclaimer} .schoolFAQItem a"
        disc_button = "#schoolQueryDisclaimerBlockBtn_secSchool"
        result = "//div[@id='categoryBlk_secSchool' and contains(@class,'schoolQueryCatContentBlock')]"
        result_title = f"{result}//div[@class='schoolQueryCatTitle']"
        result_back = "#schoolQueryCatBackBtn"
        result_option_list = "#schoolQueryAllResultsList_secSchool"
        result_option_item = "(//div[@id='schoolListItemsecSchool'])"

    class PostSecond:
        button = "#postSecSchool"
        disclaimer = "#disclaimerBlk_postSecSchool"
        disc_title = f"{disclaimer} .schoolQueryDisclaimerBlockTitle"
        disc_info = f"{disclaimer} .schoolQueryDisclaimerBlockContent"
        disc_faq = f"{disclaimer} .schoolFAQItem a"
        disc_button = "#schoolQueryDisclaimerBlockBtn_postSecSchool"
        result = "//div[@id='categoryBlk_postSecSchool' and contains(@class,'schoolQueryCatContentBlock')]"
        result_title = f"{result}//div[@class='schoolQueryCatTitle']"
        result_back = "#schoolQueryCatBackBtn"
        result_option_list = "#schoolQueryAllResultsList_postSecSchool"
        result_option_item = "(//div[@id='schoolListItempostSecSchool'])"



class BottomMenu:
    one_map = "#onemap3Btn"
    legend = ".distance-legend"
    feedback = ".wog--tabbed-button wog--tabbed-button-bottom-left"

    class Drawer:
        button = "#drawTools"
        tray = "#drawToolsTray"
        create_line = "#drawLine"
        create_polygon = "#drawPolygon"
        delete_line = "#deleteDraw"
        close = "#closeDrawTray"

    share = "#shareview"
    my_loc = "#getMyLoc"
    zoom_in = ".zoomInBtn"
    zoom_out = ".zoomOutBtn"
    footer_main = ".footerLinks"
    footer_year = "//a[normalize-space()='Map data ©2023 SLA']"
    footer_contact = "//a[normalize-space()='Contact Us']"
    footer_TOU = "//a[normalize-space()='Terms of Use']"
    footer_report = "//a[normalize-space()='Report Vulnerability']"

