import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobject.wb01_loginpage import LoginPage


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_fail(self):
        loginpage = LoginPage(self.driver)
        el = "//button[contains(@class,'login-skip')]"
        value = loginpage.element_exist(el)
        if value:
            loginpage.input_password()
            loginpage.confirm_password_err()
            time.sleep(1)
            loginpage.login_btn_click()
            try:
                s = "//span[@class='error']"
                assert "两次密码输入不一致，请重新输入" in self.driver.find_element_by_xpath(s).text
                print("test pass")
                loginpage.get_screenshot_as_file()
            except Exception as e:
                print("test fail", format(e))
        else:
            self.skipTest("跳过该用例")

    def test_register_success(self):
        loginpage = LoginPage(self.driver)
        el = "//button[contains(@class,'login-skip')]"
        value = loginpage.element_exist(el)
        if value:
            loginpage.input_password()
            loginpage.confirm_password()
            time.sleep(1)
            loginpage.login_btn_click()
            time.sleep(1)
            loginpage.input_password2()
            loginpage.login_btn2_click()
            time.sleep(1)
            try:
                s = "//span[text()='网络']"
                assert "网络" in self.driver.find_element_by_xpath(s).text
                print("test pass")
                loginpage.get_screenshot_as_file()
            except Exception as e:
                print("test fail", format(e))
        else:
            self.skipTest("跳过该用例")

    def test_login_skip(self):
        loginpage = LoginPage(self.driver)
        el = "//button[contains(@class,'login-skip')]"
        value = loginpage.element_exist(el)
        if value:
            loginpage.skip_click()
            try:
                s = "//span[text()='网络']"
                assert "网络" in self.driver.find_element_by_xpath(s).text
                print("test pass")
                loginpage.get_screenshot_as_file()
            except Exception as e:
                print("test fail", format(e))
        else:
            self.skipTest("跳过该用例")

    def test_login(self):
        loginpage = LoginPage(self.driver)
        el = "//button[contains(@class,'login-skip')]"
        value = loginpage.element_exist(el)
        if value is False:
            loginpage.input_password2()
            loginpage.login_btn2_click()
            time.sleep(1)
            try:
                s = "//span[text()='网络']"
                assert "网络" in self.driver.find_element_by_xpath(s).text
                print("test pass")
                loginpage.get_screenshot_as_file()
            except Exception as e:
                print("test fail", format(e))
        else:
            self.skipTest("跳过该用例")


if __name__ == '__main__':
    unittest.main()
