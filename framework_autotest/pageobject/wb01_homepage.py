from framework.base_page import BasePage


class HomePage(BasePage):

    # 有线网络
    wireNetwork = "//i[@class='icon_internet']/following-sibling::span[1]"
    wireNetwork_type = 'xpath'
    # 无线网络
    wirelessNetwork = "//i[@class='icon_hotspot']/following-sibling::span[1]"
    wirelessNetwork_type = 'xpath'
    # 密码设置
    passwordSetting = "//i[@class='icon_keyword']/following-sibling::span[1]"
    passwordSetting_type = 'xpath'
    # 显示设置
    desktopSetting = "//i[@class='icon_desktop']/following-sibling::span[1]"
    desktopSetting_type = 'xpath'
    # 桌面壁纸
    desktopBackground = "//i[@class='icon_desktop_background']/following-sibling::span[1]"
    desktopBackground_type = 'xpath'
    # 定时开关机
    fixedTime = "//i[@class='icon_switch']/following-sibling::span[1]"
    fixedTime_type = 'xpath'
    # 语言选择
    language = "//i[@class='icon_language']/following-sibling::span[1]"
    language_type = 'xpath'
    # 时间和日期
    timedate = "//i[@class='icon_time']/following-sibling::span[1]"
    timedate_type = 'xpath'
    # 集控服务
    control = "//i[@class='icon_central_control']/following-sibling::span[1]"
    control_type = 'xpath'
    # 恢复出厂设置
    reset = "//i[@class='icon_reset']/following-sibling::span[1]"
    reset_type = 'xpath'
    # 关于
    about = "//i[@class='icon_about']/following-sibling::span[1]"
    about_type = 'xpath'

    def wireNetwork_click(self):
        self.click(self.wireNetwork_type, self.wireNetwork)

    def wirelessNetwork_click(self):
        self.click(self.wirelessNetwork_type, self.wirelessNetwork)

    def passwordSetting_click(self):
        self.click(self.passwordSetting_type, self.passwordSetting)

    def desktopSetting_click(self):
        self.click(self.desktopSetting_type, self.desktopSetting)

    def desktopBackground_click(self):
        self.click(self.desktopBackground_type, self.desktopBackground)

    def fixedTime_click(self):
        self.click(self.fixedTime_type, self.fixedTime)

    def language_click(self):
        self.click(self.language_type, self.language)

    def control_click(self):
        self.click(self.control_type, self.control)

    def reset_click(self):
        self.click(self.reset_type, self.reset)

    def about_click(self):
        self.click(self.about_type, self.about)
