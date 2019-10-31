from framework.base_page import BasePage


class LoginPage(BasePage):

    password_box = "//input[@type='password' and @maxlength='18']"
    password_box_type = "xpath"

    confirm_password_box = "//input[@type='password' and @maxlength='50']"
    confirm_password_box_type = "xpath"

    prompt_box = "//input[@type='text']"
    prompt_box_type = "xpath"

    login_btn = "//button[contains(@class,'login-confirm')]"
    login_btn_type = "xpath"

    skip_button = "//button[contains(@class,'login-skip')]"
    skip_button_type = "xpath"

    password_box2 = "//input[@type='password']"
    login_btn2 = "//button[contains(@class,'login-confirm')]"
    login_type = "xpath"

    password = "123456"
    again_password = "123456"
    again_password_err = "1234567"
    prompt = "123456"

    def input_password(self):
        self.send_keys(self.password_box_type, self.password_box, self.password)

    def confirm_password(self):
        self.send_keys(self.confirm_password_box_type, self.confirm_password_box, self.again_password)

    def confirm_password_err(self):
        self.send_keys(self.confirm_password_box_type, self.confirm_password_box, self.again_password_err)

    def set_prompt(self):
        self.send_keys(self.prompt_box_type, self.prompt_box, self.prompt)

    def login_btn_click(self):
        self.click(self.login_btn_type, self.login_btn)

    def skip_click(self):
        self.click(self.skip_button_type, self.skip_button)

    def input_password2(self):
        self.send_keys(self.login_type, self.password_box2, self.password)

    def login_btn2_click(self):
        self.click(self.login_type, self.login_btn2)
