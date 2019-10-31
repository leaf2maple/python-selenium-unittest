from framework.base_page import BasePage


class DesktopBackground(BasePage):

    code_show_switch = "//span[@class='el-switch__core']"
    code_show_switch_type = "xpath"
    custom_desktop = "//div[contains(@class,'custom-background')]"
    custom_desktop_type = "xpath"
    cancel_btn1 = "//div[@class='desktop-background']/div[3]/button[1]"
    cancel_btn1_type = "xpath"
    apply_btn1 = "//div[@class='desktop-background']/div[3]/button[2]"
    apply_btn1_type = "xpath"

    background1 = "//ul[@class='template-list']/li[1]/div[2]"
    background2 = "//ul[@class='template-list']/li[2]/div[2]"
    background3 = "//ul[@class='template-list']/li[3]/div[2]"
    background4 = "//ul[@class='template-list']/li[4]/div[2]"
    background5 = "//ul[@class='template-list']/li[5]/div[2]"
    background6 = "//ul[@class='template-list']/li[6]/div[2]"
    background_type = "xpath"
    cancel_btn2 = "//div[@class='template']/div[2]/button[1]"
    apply_btn2 = "//div[@class='template']/div[2]/button[2]"
    success_apply_btn = "//p[@class='footer']/button"
    btn2_type = "xpath"

    def background1_click(self):
        self.click(self.background_type, self.background1)

    def background2_click(self):
        self.click(self.background_type, self.background2)

    def background3_click(self):
        self.click(self.background_type, self.background3)

    def background4_click(self):
        self.click(self.background_type, self.background4)

    def background5_click(self):
        self.click(self.background_type, self.background5)

    def background6_click(self):
        self.click(self.background_type, self.background6)

    def apply2_click(self):
        self.click(self.btn2_type, self.apply_btn2)

    def success_apply_btn_click(self):
        self.click(self.btn2_type, self.success_apply_btn)
