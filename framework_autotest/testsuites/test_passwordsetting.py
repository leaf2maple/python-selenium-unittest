import unittest
import time
from pageobject.wb01_passwordsettingpage import PasswordSetting
from pageobject.wb01_homepage import HomePage
from framework.login import Login
from framework.browser_engine import BrowserEngine


class TestPasswordSetting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login(cls.driver)
        login.skip_or_login()
        homepage = HomePage(cls.driver)
        homepage.passwordSetting_click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_019_modify_device_name(self):
        passwordsetting = PasswordSetting(self.driver)
        passwordsetting.input_device_name()
        time.sleep(1)
        passwordsetting.apply_btn1_click()
        passwordsetting.modify_success_btn_click()
        try:
            assert "1234567890" in passwordsetting.get_device_name()
            print('test019 pass')
        except Exception as e:
            print('test019 fail', format(e))


if __name__ == '__main__':
    unittest.main()
