from framework.base_page import BasePage


class WirelessNetWork(BasePage):

    # 5G开关
    hotspot_5g_switch = "//div[@class='generatio']/div/div/div/span[@class='el-switch__core']"
    hotspot_5g_switch_type = "xpath"
    # SSID_5G
    ssid_5g_box = "//div[@class='generatio']/div/div[2]/div/div/input[@type='text']"
    ssid_5g_type = "xpath"
    # password_5G
    password_5g_box = "//div[@class='generatio']/div/div[2]/div/div/input[@type='password']"
    password_5g_type = "xpath"
    # 5G信道下拉列表
    route_5G_ul = "//div[@x-placement='top-start']/div/div/ul"
    route_5G_ul_type = "xpath"
    route_165 = "//div[@x-placement='top-start']/div/div/ul/li[5]"
    # 隐藏SSID
    hide_ssid_5g = "//div[@class='generatio']/div/div[2]/div[4]/label/span/span"
    hide_ssid_5g_type = "xpath"
    # 取消按钮/确定按钮
    cancel_btn1 = "//div[@class='generatio']/div/div[2]/div[5]/button[contains(@class,'cancel-btn')]"
    cancel_btn1_type = "xpath"
    apply_btn1 = "//div[@class='generatio']/div/div[2]/div[5]/button[contains(@class,'apply')]"
    apply_btn1_type = "xpath"

    # 2.4G开关
    hotspot_2_4g_switch = "//div[contains(@class,'second')]/div/div/div/span[@class='el-switch__core']"
    hotspot_2_4g_switch_type = "xpath"
    # SSID_2.4G
    ssid_2_4g_box = "//div[contains(@class,'second')]/div/div[2]/div/div/input[@type='text']"
    ssid_2_4g_type = "xpath"
    # password_2.4G
    password_2_4g_box = "//div[contains(@class,'second')]/div/div[2]/div/div/input[@type='password']"
    password_2_4g_type = "xpath"
    # 2.4G信道下拉列表route_2.4G
    route_2_4G_input = "//div[contains(@class,'second')]/div/div[2]/div[3]/div/div/input"
    route_2_4G_div_type = "xpath"
    route_auto = "//li/span[text()='自动选择']"
    route_12 = "//li/span[text()='信道12']"

    # 隐藏SSID
    hide_ssid_2_4g = "//div[contains(@class,'second')]/div/div[2]/div[4]/label/span/span"
    hide_ssid_2_4g_type = "xpath"
    # 取消按钮/确定按钮
    cancel_btn2 = "//div[contains(@class,'second')]/div/div[2]/div[5]/button[1]"
    cancel_btn2_type = "xpath"
    apply_btn2 = "//div[contains(@class,'second')]/div/div[2]/div[5]/button[2]"
    apply_btn2_type = "xpath"
    open_wifi_apply2 = "//p[@class='footer']/button"
    open_wifi_apply2_type = "xpath"
    close_wifi_apply2 = "//p[@class='footer']/button[2]"
    close_wifi_apply2_type = "xpath"

    # 网络隔离开关
    internet_switch = "//div[@class='isolation-title']/div/span"
    internet_switch_type = "xpath"

    # 相关数据
    ssid_2_4g = "1234567890"
    password_2_4g = "1234567890"

    def hotspot_5g_switch_click(self):
        self.click(self.hotspot_5g_switch_type, self.hotspot_5g_switch)

    def hide_ssid_5g_click(self):
        self.click(self.hide_ssid_5g_type, self.hide_ssid_5g)

    def cancel_btn1_click(self):
        self.click(self.cancel_btn1_type, self.cancel_btn1)

    def apply_btn1_click(self):
        self.click(self.apply_btn1_type, self.apply_btn1)

    # 2.4g相关操作
    def hotspot_2_4g_switch_click(self):
        self.click(self.hotspot_2_4g_switch_type, self.hotspot_2_4g_switch)

    def ssid_2_4g_input(self):
        self.send_keys(self.ssid_2_4g_type, self.ssid_2_4g_box, self.ssid_2_4g)

    def password_2_4g_input(self):
        self.send_keys(self.password_2_4g_type, self.password_2_4g_box, self.password_2_4g)

    def route_2_4g_click(self):
        self.click(self.route_2_4G_div_type, self.route_2_4G_input)
        self.click(self.route_2_4G_div_type, self.route_12)

    def hide_ssid_2_4g_click(self):
        self.click(self.hide_ssid_2_4g_type, self.hide_ssid_2_4g)

    def cancel_btn2_click(self):
        self.click(self.cancel_btn2_type, self.cancel_btn2)

    def apply_btn2_click(self):
        self.click(self.apply_btn2_type, self.apply_btn2)

    def open_wifi_apply_click(self):
        self.click(self.open_wifi_apply2_type, self.open_wifi_apply2)

    def close_wifi_apply_click(self):
        self.click(self.close_wifi_apply2_type, self.close_wifi_apply2)

    # 网络隔离
    def internet_switch_click(self):
        self.click(self.internet_switch_type, self.internet_switch)
