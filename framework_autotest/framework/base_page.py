from framework.logger import Logger
import os
import time
from PIL import Image


logger = Logger('BasePage').get_log()


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()
        logger.info('浏览器前进')

    def back(self):
        self.driver.back()
        logger.info('浏览器后退')

    def close(self):
        self.driver.close()
        logger.info('关闭浏览器当前页面')

    def refresh(self):
        self.driver.refresh()
        logger.info('刷新浏览器当前页面')

    def get_screenshot_as_file(self):
        time_name = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshot_file = os.path.dirname(os.path.abspath('.')) + r'\screenshots\{}'.format(time_name) + '.png'
        try:
            time.sleep(1)
            self.driver.get_screenshot_as_file(screenshot_file)
            logger.info('截图成功')
        except Exception as e:
            logger.error('screenshot fail:%s' % e)

    def find_element(self, type, selector):
        global element
        if type == 'id':
            element = self.driver.find_element_by_id(selector)
        elif type == 'name':
            element = self.driver.find_element_by_name(selector)
        elif type == 'class_name':
            element = self.driver.find_element_by_class_name(selector)
        elif type == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector)
        elif type == 'link_text':
            element = self.driver.find_element_by_link_text(selector)
        elif type == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector)
        elif type == 'xpath':
            element = self.driver.find_element_by_xpath(selector)
            logger.info('find element of xpath')
        elif type == 'CSS':
            element = self.driver.find_element_by_css_selector(selector)
        else:
            logger.error('please enter a valid type of element')
        return element

    def find_elements(self, type, selector):
        global elements
        if type == 'id':
            elements = self.driver.find_elements_by_id(selector)
        elif type == 'name':
            elements = self.driver.find_elements_by_name(selector)
        elif type == 'class_name':
            elements = self.driver.find_elements_by_class_name(selector)
        elif type == 'xpath':
            elements = self.driver.find_elements_by_xpath(selector)
        else:
            logger.error('please enter a valid type of elements')
        return elements

    def element_exist(self, selector):
        s = self.driver.find_elements_by_xpath(selector)
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True
        else:
            return False

    def send_keys(self, type, selector, text):
        el = self.find_element(type, selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_screenshot_as_file()

    def clear(self, type, selector):
        el = self.find_element(type, selector)
        try:
            el.clear()
            logger.info('clear text')
        except Exception as e:
            logger.error('clear fail:%s' % e)
            self.get_screenshot_as_file()

    def click(self, type, selector):
        el = self.find_element(type, selector)
        try:
            el.click()
            logger.info('click pass')
        except Exception as e:
            logger.error('click fail:%s' % e)
            self.get_screenshot_as_file()

    def text(self, type, selector):
        el_text = self.find_element(type, selector).text
        return el_text

    def title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    def current_window_handle(self):
        logger.info('获取当前窗口句柄')
        return self.driver.current_window_handle

    def switch_to_window(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                logger.info("切换窗口")

    # adb获取设备相关信息
    def get_ssid_name(self):
        cmd = "adb connect 10.10.10.50&&adb shell \"getprop|grep ssid\""
        with os.popen(cmd) as p:
            line = p.readlines()[1]
        return line

    def get_password(self):
        cmd = "adb connect 10.10.10.50&&adb shell \"getprop|grep password\""
        with os.popen(cmd) as p:
            line = p.readlines()[1]
        return line

    def get_device_name(self):
        cmd = "adb connect 10.10.10.50&&adb shell \"getprop|grep device.name\""
        with os.popen(cmd) as p:
            line = p.readlines()[1]
        return line

    def get_device_screencap(self, screencap_name):
        connect = "adb shell connect 10.10.10.50"
        screencap = "adb shell screencap -p /sdcard/" + screencap_name
        file = os.path.dirname(os.path.abspath(".")) + "\\image_contrast\\" + screencap_name
        pull = "adb pull /sdcard/" + screencap_name + " " + file
        rm = "adb shell rm /sdcard/" + screencap_name
        cmd = connect + "&&" + screencap + "&&" + pull + "&&" + rm
        p = os.popen(cmd)
        time.sleep(2)
        p.close()
        return file

    # 图像相似度
    def image_contrast(self, screencap_name, image2_path):
        file = self.get_device_screencap(screencap_name)
        image1 = Image.open(file)
        image1 = image1.resize((64, 64)).convert('RGB')
        image2 = Image.open(image2_path)
        image2 = image2.resize((64, 64)).convert('RGB')
        h1 = image1.histogram()
        h2 = image2.histogram()
        assert len(h1) == len(h2)
        result = sum(1 - (0 if h1 == h2 else float(abs(h1 - h2)) / max(h1, h2)) for h1, h2 in zip(h1, h2)) / len(h1)
        return result
