from framework.base_page import BasePage


class DesktopSetting(BasePage):

    hdmi_signal_input1 = "//div[contains(@class,'is-focus')]/input"
    hdmi_signal_input1_type = "xpath"
    always_output1 = "//div[@x-placement='bottom-start']/div/div/ul/li[1]"
    always_output1_type = "xpath"
    sharing_output1 = "//div[@x-placement='bottom-start']/div/div/ul/li[2]"
    sharing_output1_type = "xpath"
    resuolution_input1 = "//div[@class='desktop2-setting-container']/div[1]/div[3]/div/div/input"
    resuolution_input1_type = "xpath"
    cancel_btn1 = "//div[@class='desktop2-setting-container']/div[1]/div[5]/button[1]"
    cancel_btn1_type = "xpath"
    apply_btn1 = "//div[@class='desktop2-setting-container']/div[1]/div[5]/button[2]"
    apply_btn1_type = "xpath"

    hdmi_signal_input2 = "//div[@class='desktop2-setting-container']/div[2]/div[2]/div/div/input"
    hdmi_signal_input2_type = "xpath"
    always_output2 = "//div[@x-placement='top-start']/div/div/ul/li[1]"
    always_output2_type = "xpath"
    sharing_output2 = "//div[@x-placement='top-start']/div/div/ul/li[2]"
    sharing_output2_type = "xpath"
    resuolution_input2 = "//div[@class='desktop2-setting-container']/div[2]/div[3]/div/div/input"
    resuolution_input2_type = "xpath"
    cancel_btn2 = "//div[@class='desktop2-setting-container']/div[2]/div[5]/button[1]"
    cancel_btn2_type = "xpath"
    apply_btn2 = "//div[@class='desktop2-setting-container']/div[2]/div[5]/button[2]"
    apply_btn2_type = "xpath"