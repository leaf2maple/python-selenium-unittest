import unittest
import time
from pageobject.wb01_languagepage import Language
from pageobject.wb01_homepage import HomePage
from framework.browser_engine import BrowserEngine
from framework.login import Login


class TestLanguage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login(cls.driver)
        login.skip_or_login()
        homepage = HomePage(cls.driver)
        homepage.language_click()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_language_set(self):
        language = Language(self.driver)
        el = "//div[text()='语言选择']"
        if language.element_exist(el):
            language.english_click()
            language.apply_btn_click()
            time.sleep(1)
            try:
                assert language.element_exist(el) is False
                language.get_screenshot_as_file()
                language.frame_apply_btn_click()
                print("test pass")
                time.sleep(1)
                language.chinese_click()
                language.apply_btn_click()
                time.sleep(1)
                language.frame_apply_btn_click()
            except Exception as e:
                print("test fail", format(e))
        else:
            language.chinese_click()
            language.apply_btn_click()
            time.sleep(1)
            try:
                assert language.element_exist(el) is True
                language.get_screenshot_as_file()
                language.frame_apply_btn_click()
                print("test pass")
            except Exception as e:
                print("test fail", format(e))


if __name__ == '__main__':
    unittest.main()
