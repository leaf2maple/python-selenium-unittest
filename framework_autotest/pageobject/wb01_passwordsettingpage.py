from framework.base_page import BasePage


class PasswordSetting(BasePage):

    device_name = "//input[@type='text' and @maxlength='25']"
    device_name_type = "xpath"
    cancel_btn1 = "//div[@class='device-name-setting']/button[contains(@class,'cancel-btn')]"
    cancel_btn1_type = "xpath"
    apply_btn1 = "//div[@class='device-name-setting']/button[contains(@class,'apply')]"
    apply_btn1_type = "xpath"
    new_device_name = "1234567890"
    modify_success_btn = "//p[@class='footer']/button"
    modify_success_btn_type = "xpath"

    new_password_input = "//span[text()='新密码']/../div/input"
    new_password_input_type = "xpath"
    confirm_password_input = "//span[text()='确认密码']/../div/input"
    confirm_password_input_type = "xpath"
    password_prompt_input = "//input[@type='text' and @maxlength='40']"
    password_prompt_input_type = "xpath"
    cancel_btn2 = "//div[@class='password-change']/button[contains(@class,'cancel-btn')]"
    cancel_btn2_type = "xpath"
    apply_btn2 = "//div[@class='password-change']/button[contains(@class,'apply')]"
    apply_btn2_type = "xpath"

    def input_device_name(self):
        self.send_keys(self.device_name_type, self.device_name, self.new_device_name)

    def apply_btn1_click(self):
        self.click(self.apply_btn1_type, self.apply_btn1)

    def modify_success_btn_click(self):
        self.click(self.modify_success_btn_type, self.modify_success_btn)
