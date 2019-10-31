from framework.base_page import BasePage


class Time(BasePage):

    lock_in_time_switch = "//span[@class='el-switch__core']"
    lock_in_time_switch_type = "xpath"

    time_zone_div = "//div[contains(@class,'is-focus')]"
    time_zone_div_type = "xpath"
    BeiJing = "//ul[contains(@class,'el-select-dropdown__list')]/li[1]"
    BeiJing_type = "xpath"
    HongKong = "//ul[contains(@class,'el-select-dropdown__list')]/li[2]"
    HongKong_type = "xpath"
    Tokyo = "//ul[contains(@class,'el-select-dropdown__list')]/li[3]"
    Tokyo_type = "xpath"
    Sydney = "//ul[contains(@class,'el-select-dropdown__list')]/li[4]"
    Sydney_type = "xpath"
    Djakarta = "//ul[contains(@class,'el-select-dropdown__list')]/li[5]"
    Djakarta_type = "xpath"
    Dubai = "//ul[contains(@class,'el-select-dropdown__list')]/li[6]"
    Dubai_type = "xpath"
    Calcutta = "//ul[contains(@class,'el-select-dropdown__list')]/li[7]"
    Calcutta_type = "xpath"

    date_set_div = "//div[contains(@class,'el-date-editor--datetime')]"
    date_set_div_type = "xpath"
    next_month = "//button[@aria-label='下个月']"
    next_month_type = "xpath"
    order_date = "//table[@class='el-date-table']/tbody/tr[3]/td[1]"
    order_date_type = "xpath"

    time_set_div = "//div[contains(@class,'el-date-editor--time')]"
    H_00 = "//div[contains(@class,'el-time-spinner') and contains(@class,'has-seconds')]/div[1]/div[1]/ul/li[1]"
    M_00 = "//div[contains(@class,'el-time-spinner') and contains(@class,'has-seconds')]/div[2]/div[1]/ul/li[1]"
    s_00 = "//div[contains(@class,'el-time-spinner') and contains(@class,'has-seconds')]/div[3]/div[1]/ul/li[1]"
    time_set_div_type = "xpath"

    cancel_btn = "//div[@class='button-wrapper']/button[1]"
    cancel_btn_type = "xpath"
    apply_btn = "//div[@class='button-wrapper']/button[2]"
    apply_btn_type = "xpath"