from framework.base_page import BasePage


class WireNetWorkPage(BasePage):

    # 有线网络开关
    wirenetwork_switch = "//span[@class='el-switch__core']"
    wirenetwork_switch_type = "xpath"
    # iP设置下拉列表
    ip_input = "//input[@class='el-input__inner']"
    ip_set_type = "xpath"
    # ip自动选择
    ip_auto = "//ul[contains(@class,'el-select-dropdown__list')]/li[1]/span"
    ip_auto_type = "xpath"
    # ip手动选择
    ip_manual = "//ul[contains(@class,'el-select-dropdown__list')]/li[2]/span"
    ip_manual_type = "xpath"
    # 取消按钮/确定按钮
    cancel_btn = "//button[contains(@class,'info')]"
    cancel_btn_type = "xpath"
    apply_btn = "//button[contains(@class,'apply')]"
    apply_btn_type = "xpath"

    def wirenetwork_switch_click(self):
        self.click(self.wirenetwork_switch_type, self.wirenetwork_switch)

    def ip_ul_click(self):
        self.click(self.ip_set_type, self.ip_input)

    def ip_auto_set_click(self):
        self.click(self.ip_auto_type, self.ip_auto)

    def ip_manual_set_click(self):
        self.click(self.ip_manual_type, self.ip_manual)

    def cancel_btn_click(self):
        self.click(self.cancel_btn_type, self.cancel_btn)

    def apply_btn_click(self):
        self.click(self.apply_btn_type, self.apply_btn)

