import unittest
import time
from framework.browser_engine import BrowserEngine
from pageobject.wb01_wirenetworkpage import WireNetWorkPage
from framework.login import Login
from pageobject.wb01_homepage import HomePage


class TestWireNetWork(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login(cls.driver)
        login.skip_or_login()
        homepage = HomePage(cls.driver)
        homepage.wireNetwork_click()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_011_wirenetwork_switch(self):
        wirenetwork = WireNetWorkPage(self.driver)
        # 关闭
        wirenetwork.wirenetwork_switch_click()
        time.sleep(1)
        try:
            el = self.driver.find_element_by_xpath("//div[@class='wireNetwork']")
            assert "IP设置" not in el.text
            print("test_011 pass")
            wirenetwork.get_screenshot_as_file()
        except Exception as e:
            print("test_011 fail", format(e))
        # 打开
        wirenetwork.wirenetwork_switch_click()
        time.sleep(1)
        try:
            el = self.driver.find_element_by_xpath("//span[@class='title' and text()='IP设置']")
            assert "IP设置" in el.text
            print("test_011 pass")
            wirenetwork.get_screenshot_as_file()
        except Exception as e:
            print("test_011 fail", format(e))

    def test_012_ip_manual_set(self):
        wirenetwork = WireNetWorkPage(self.driver)
        wirenetwork.ip_ul_click()
        wirenetwork.ip_manual_set_click()
        try:
            el = "//span[@class='address-input-title' and text()='IP地址']/following-sibling::span[1]"
            assert self.driver.find_element_by_xpath(el) is True
            print("test_012 pass")
            wirenetwork.get_screenshot_as_file()
        except Exception as e:
            print("test_012 fail", format(e))

    def test_013_ip_auto_set(self):
        wirenetwork = WireNetWorkPage(self.driver)
        wirenetwork.ip_ul_click()
        wirenetwork.ip_auto_set_click()
        try:
            el = "//span[@class='address-input-title' and text()='IP地址']/following-sibling::span[1]"
            assert self.driver.find_element_by_xpath(el) is True
            print("test_013 pass")
            wirenetwork.get_screenshot_as_file()
        except Exception as e:
            print("test_013 fail", format(e))


if __name__ == '__main__':
    unittest.main()
