from framework.base_page import BasePage


class Language(BasePage):

    language_input = "//div[contains(@class,'el-input--suffix')]"
    language_input_type = "xpath"
    Chinese_li = "//ul[contains(@class,'el-select-dropdown__list')]/li[1]"
    Chinese_li2 = "//ul[contains(@class,'el-select-dropdown__list')]/li[2]"
    English_li = "//ul[contains(@class,'el-select-dropdown__list')]/li[3]"
    Japanese_li = "//ul[contains(@class,'el-select-dropdown__list')]/li[4]"
    cancel_btn = "//div[@class='button-wrapper']/button[1]"
    cancel_btn_type = "xpath"
    apply_btn = "//div[@class='button-wrapper']/button[2]"
    apply_btn_type = "xpath"
    frame_apply_btn = "//p[@class='footer']/button"

    def chinese_click(self):
        self.click(self.language_input_type, self.language_input)
        self.click(self.language_input_type, self.Chinese_li)

    def english_click(self):
        self.click(self.language_input_type, self.language_input)
        self.click(self.language_input_type, self.English_li)

    def apply_btn_click(self):
        self.click(self.apply_btn_type, self.apply_btn)

    def frame_apply_btn_click(self):
        self.click(self.apply_btn_type, self.frame_apply_btn)
