import unittest
import time
import os
from pageobject.wb01_homepage import HomePage
from pageobject.wb01_desktopbackgroundpage import DesktopBackground
from framework.login import Login
from framework.browser_engine import BrowserEngine


class TestDesktopBackground(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login(cls.driver)
        login.skip_or_login()
        homepage = HomePage(cls.driver)
        homepage.desktopBackground_click()
        time.sleep(4)
        cls.file = os.path.dirname(os.path.abspath('.')) + "\\image_contrast\\"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_background1_click(self):
        desktopbackground = DesktopBackground(self.driver)
        desktopbackground.background1_click()
        desktopbackground.apply2_click()
        time.sleep(1)
        try:
            desktopbackground.success_apply_btn_click()
            background_path = self.file + "background1.png"
            result = desktopbackground.image_contrast('1.png', background_path)
            # print(result)
            assert result > 0.8
            print("test pass")
        except Exception as e:
            print("test fail", format(e))

    def test_background2_click(self):
        desktopbackground = DesktopBackground(self.driver)
        desktopbackground.background2_click()
        desktopbackground.apply2_click()
        time.sleep(1)
        try:
            desktopbackground.success_apply_btn_click()
            background_path = self.file + "background2.png"
            assert desktopbackground.image_contrast('1.png', background_path) > 0.8
            print("test pass")
        except Exception as e:
            print("test fail", format(e))

    def test_background3_click(self):
        desktopbackground = DesktopBackground(self.driver)
        desktopbackground.background3_click()
        desktopbackground.apply2_click()
        time.sleep(1)
        try:
            desktopbackground.success_apply_btn_click()
            background_path = self.file + "background3.png"
            assert desktopbackground.image_contrast('1.png', background_path) > 0.8
            print(desktopbackground.image_contrast('1.png', background_path))
            print("test pass")
        except Exception as e:
            print("test fail", format(e))

    def test_background4_click(self):
        desktopbackground = DesktopBackground(self.driver)
        desktopbackground.background4_click()
        desktopbackground.apply2_click()
        time.sleep(1)
        try:
            desktopbackground.success_apply_btn_click()
            background_path = self.file + "background4.png"
            assert desktopbackground.image_contrast('1.png', background_path) > 0.8
            print("test pass")
        except Exception as e:
            print("test fail", format(e))

    def test_background5_click(self):
        desktopbackground = DesktopBackground(self.driver)
        desktopbackground.background5_click()
        desktopbackground.apply2_click()
        time.sleep(1)
        try:
            desktopbackground.success_apply_btn_click()
            background_path = self.file + "background5.png"
            assert desktopbackground.image_contrast('1.png', background_path) > 0.8
            print("test pass")
        except Exception as e:
            print("test fail", format(e))

    def test_background6_click(self):
        desktopbackground = DesktopBackground(self.driver)
        desktopbackground.background6_click()
        desktopbackground.apply2_click()
        time.sleep(1)
        try:
            desktopbackground.success_apply_btn_click()
            background_path = self.file + "background6.png"
            assert desktopbackground.image_contrast('1.png', background_path) > 0.8
            print("test pass")
        except Exception as e:
            print("test fail", format(e))


if __name__ == '__main__':
    unittest.main()
