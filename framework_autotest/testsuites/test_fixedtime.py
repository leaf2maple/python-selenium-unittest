import unittest
import time
from pageobject.wb01_homepage import HomePage
from pageobject.wb01_fixedtimepage import FixedTime
from framework.browser_engine import BrowserEngine
from framework.login import Login


class TestFixedTime(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login(cls.driver)
        login.skip_or_login()
        homepage = HomePage(cls.driver)
        homepage.fixedTime_click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_set_fixed_time_switch(self):
        fixedtime = FixedTime(self.driver)
        el = "//span[text()='开机时间']"
        value = self.driver.find_element_by_xpath(el).is_displayed()
        if value:
            time.sleep(1)
            fixedtime.fixed_time_switch_click()
            time.sleep(1)
            try:
                assert self.driver.find_element_by_xpath(el).is_displayed() is False
                print("test pass")
                fixedtime.get_screenshot_as_file()
            except Exception as e:
                print("test1 fail", format(e))
        else:
            time.sleep(1)
            fixedtime.fixed_time_switch_click()
            time.sleep(1)
            try:
                assert self.driver.find_element_by_xpath(el).is_displayed() is True
                print("test pass")
                fixedtime.get_screenshot_as_file()
            except Exception as e:
                print("test2 fail", format(e))

    def test_set_fixed_time_fail(self):
        fixedtime = FixedTime(self.driver)
        el = "//span[text()='开机时间']"
        value = self.driver.find_element_by_xpath(el).is_displayed()
        if value is False:
            fixedtime.fixed_time_switch_click()
        time.sleep(1)
        fixedtime.action_time_input_text_same()
        time.sleep(1)
        fixedtime.tag_click()
        fixedtime.off_time_input_text()
        time.sleep(1)
        fixedtime.tag_click()
        fixedtime.everyday_li_click()
        time.sleep(1)
        fixedtime.tag_click()
        fixedtime.apply_btn_click()
        time.sleep(1)
        try:
            p = "//p[text()='开关机计划时间不能相同']"
            assert fixedtime.element_exist(p)
            fixedtime.get_screenshot_as_file()
            fixedtime.frame_apply_btn_click()
            time.sleep(1)
            print("test pass")
        except Exception as e:
            print("test fail", format(e))

    def test_set_fixed_time_success(self):
        fixedtime = FixedTime(self.driver)
        el = "//span[text()='开机时间']"
        value = self.driver.find_element_by_xpath(el).is_displayed()
        if value is False:
            fixedtime.fixed_time_switch_click()
        time.sleep(1)
        fixedtime.action_time_input_text()
        time.sleep(1)
        fixedtime.tag_click()
        fixedtime.off_time_input_text()
        time.sleep(1)
        fixedtime.tag_click()
        fixedtime.everyday_li_click()
        time.sleep(1)
        fixedtime.tag_click()
        fixedtime.apply_btn_click()
        time.sleep(1)
        try:
            span = "//span[text()='定时开关机设置成功']"
            assert fixedtime.element_exist(span)
            fixedtime.get_screenshot_as_file()
            fixedtime.frame_apply_btn_click()
            time.sleep(1)
            print("test pass")
        except Exception as e:
            print("test fail", format(e))


if __name__ == "__main__":
    unittest.main()
