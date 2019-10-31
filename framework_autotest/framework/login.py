import time
from framework.logger import Logger
from pageobject.wb01_loginpage import LoginPage


logger = Logger('login').get_log()


class Login(object):

    def __init__(self, driver):
        self.driver = driver

    def skip_or_login(self):
        loginpage = LoginPage(self.driver)
        el = "//button[contains(@class,'login-skip')]"
        value = loginpage.element_exist(el)
        if value:
            loginpage.skip_click()
            logger.info("跳过登录")
        else:
            loginpage.input_password2()
            loginpage.login_btn2_click()
            time.sleep(1)
            logger.info("输入密码登录")
