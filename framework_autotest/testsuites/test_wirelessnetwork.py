import unittest
import time
from pageobject.wb01_wirelessnetwork import WirelessNetWork
from pageobject.wb01_homepage import HomePage
from framework.browser_engine import BrowserEngine
from framework.login import Login


class TestWirelessNetWork(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login(cls.driver)
        login.skip_or_login()
        homepage = HomePage(cls.driver)
        homepage.wirelessNetwork_click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_014_click_2_4g_wifi(self):
        wirelessnetwork = WirelessNetWork(self.driver)
        el = "//p[@class='tip']"    # "暂未开启，开启后可进行无线热点-2.4G的设置"
        value = wirelessnetwork.element_exist(el)

        if value:
            wirelessnetwork.hotspot_2_4g_switch_click()
            time.sleep(1)
            wirelessnetwork.apply_btn2_click()
            time.sleep(1)
            wirelessnetwork.open_wifi_apply_click()
            try:
                assert wirelessnetwork.element_exist(el) is False
                wirelessnetwork.get_screenshot_as_file()
                print('test014 pass')
            except Exception as e:
                print('test014 fail', format(e))
        else:
            wirelessnetwork.hotspot_2_4g_switch_click()
            time.sleep(1)
            wirelessnetwork.close_wifi_apply_click()
            try:
                assert self.driver.find_element_by_xpath(el) is True
                wirelessnetwork.get_screenshot_as_file()
                print('test014 pass')
            except Exception as e:
                print('test014 fail', format(e))

    def test_015_set_ssid_2_4g_wifi(self):
        wirelessnetwork = WirelessNetWork(self.driver)
        el = "//p[@class='tip']"
        value = wirelessnetwork.element_exist(el)
        if value:
            time.sleep(1)
            wirelessnetwork.hotspot_2_4g_switch_click()
            time.sleep(1)
            wirelessnetwork.apply_btn2_click()
            time.sleep(1)
            wirelessnetwork.open_wifi_apply_click()
        wirelessnetwork.ssid_2_4g_input()
        wirelessnetwork.apply_btn2_click()
        time.sleep(1)
        wirelessnetwork.open_wifi_apply_click()
        try:
            assert '1234567890' in wirelessnetwork.get_ssid_name()
            print('test015 pass')
        except Exception as e:
            print('test015 fail', format(e))

    def test_016_set_password_2_4g_wifi(self):
        wirelessnetwork = WirelessNetWork(self.driver)
        el = "//p[@class='tip']"
        value = wirelessnetwork.element_exist(el)

        if value:
            wirelessnetwork.hotspot_2_4g_switch_click()
            time.sleep(1)
            wirelessnetwork.apply_btn2_click()
            time.sleep(1)
            wirelessnetwork.open_wifi_apply_click()
        wirelessnetwork.password_2_4g_input()
        wirelessnetwork.apply_btn2_click()
        time.sleep(1)
        wirelessnetwork.open_wifi_apply_click()
        try:
            assert '1234567890' in wirelessnetwork.get_password()
            print('test016 pass')
        except Exception as e:
            print('test016 fail', format(e))

    def test_017_set_route_2_4g_wifi(self):
        wirelessnetwork = WirelessNetWork(self.driver)
        el = "//p[@class='tip']"
        value = wirelessnetwork.element_exist(el)

        if value:
            time.sleep(1)
            wirelessnetwork.hotspot_2_4g_switch_click()
            time.sleep(1)
            wirelessnetwork.apply_btn2_click()
            time.sleep(1)
            wirelessnetwork.open_wifi_apply_click()
            time.sleep(2)
        wirelessnetwork.route_2_4g_click()
        try:
            span = "//li/span[text()='信道12']"
            assert "信道12" in self.driver.find_element_by_xpath(span).text
            print('test017 pass')
        except Exception as e:
            print('test017 fail', format(e))

    def test_018_close_all_wifi(self):
        wirelessnetwork = WirelessNetWork(self.driver)
        el = "//p[@class='tip']"
        value = wirelessnetwork.element_exist(el)
        if value is False:
            time.sleep(1)
            wirelessnetwork.hotspot_2_4g_switch_click()
            time.sleep(1)
            wirelessnetwork.close_wifi_apply_click()
            time.sleep(1)
        wirelessnetwork.hotspot_5g_switch_click()
        try:
            span = "//span[text()='无法关闭全部无线热点']"
            assert self.driver.find_element_by_xpath(span)
            print('test018 pass')
            wirelessnetwork.get_screenshot_as_file()
            wirelessnetwork.refresh()
        except Exception as e:
            print('test018 fail', format(e))


if __name__ == "__main__":
    unittest.main()

