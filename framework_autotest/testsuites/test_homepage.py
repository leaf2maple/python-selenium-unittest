import unittest
import time
from pageobject.wb01_homepage import HomePage
from framework.browser_engine import BrowserEngine
from framework.login import Login


class TestWb01HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login(cls.driver)
        login.skip_or_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_001_click_wireNetwork(self):
        homepage = HomePage(self.driver)
        homepage.wireNetwork_click()
        time.sleep(1)
        try:
            assert "有线网络" in self.driver.find_element_by_class_name("module-title").text
            print("test001 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test001 fail", format(e))

    def test_002_click_wirelessNetwork(self):
        homepage = HomePage(self.driver)
        homepage.wirelessNetwork_click()
        time.sleep(1)
        try:
            assert "无线热点" in self.driver.find_element_by_class_name("module-title").text
            print("test002 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test002 fail", format(e))

    def test_003_click_passwordSetting(self):
        homepage = HomePage(self.driver)
        homepage.passwordSetting_click()
        time.sleep(1)
        try:
            assert "密码设置" in self.driver.find_element_by_class_name("module-title").text
            print("test003 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test003 fail", format(e))

    def test_004_click_desktopSetting(self):
        homepage = HomePage(self.driver)
        homepage.desktopSetting_click()
        time.sleep(1)
        try:
            assert "显示设置" in self.driver.find_element_by_class_name("module-title").text
            print("test004 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test004 fail", format(e))

    def test_005_click_desktopBackground(self):
        homepage = HomePage(self.driver)
        homepage.desktopBackground_click()
        time.sleep(2)
        try:
            assert "桌面壁纸" in self.driver.find_element_by_class_name("module-title").text
            print("test005 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test005 fail", format(e))

    def test_006_click_fixedTime(self):
        homepage = HomePage(self.driver)
        homepage.fixedTime_click()
        time.sleep(1)
        try:
            assert "定时开关机" in self.driver.find_element_by_class_name("module-title").text
            print("test006 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test006 fail", format(e))

    def test_007_click_language(self):
        homepage = HomePage(self.driver)
        homepage.language_click()
        try:
            assert "语言选择" in self.driver.find_element_by_class_name("module-title").text
            print("test007 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test007 fail", format(e))

    def test_008_click_control(self):
        homepage = HomePage(self.driver)
        homepage.control_click()
        time.sleep(1)
        try:
            assert "集控服务" in self.driver.find_element_by_class_name("module-title").text
            print("test008 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test008 fail", format(e))

    def test_009_click_reset(self):
        homepage = HomePage(self.driver)
        homepage.reset_click()
        time.sleep(1)
        try:
            assert "恢复出厂设置" in self.driver.find_element_by_class_name("module-title").text
            print("test009 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test009 fail", format(e))

    def test_010_click_about(self):
        homepage = HomePage(self.driver)
        homepage.about_click()
        time.sleep(1)
        try:
            assert "关于" in self.driver.find_element_by_class_name("module-title").text
            print("test010 pass")
            homepage.get_screenshot_as_file()
        except Exception as e:
            print("test010 fail", format(e))


if __name__ == '__main__':
    unittest.main()

