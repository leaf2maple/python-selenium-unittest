from framework.base_page import BasePage


class FixedTime(BasePage):

    fixed_time_switch = "//span[@class='el-switch__core']"
    fixed_time_switch_type = "xpath"
    action_time_input = "//input[@class='el-input__inner' and @placeholder='暂无开机计划']"
    action_time_input_type = "xpath"
    off_time_input = "//input[@class='el-input__inner' and @placeholder='暂无关机计划']"
    off_time_input_type = "xpath"
    weekly_repeat_div = "//div[@class='el-select__tags']"
    weekly_repeat_input_type = "xpath"
    everyday_li = "//ul[@class='el-scrollbar__view el-select-dropdown__list']/li[1]"
    # 开机与关机具体时间
    action_time = "00:01"
    action_time1 = "00:00"
    off_time = "00:00"
    # 标题元素
    tag_div = "//div[@class='module-title']"

    cancel_btn = "//div[@class='button-wrapper']/button[1]"
    cancel_btn_type = "xpath"
    apply_btn = "//div[@class='button-wrapper']/button[2]"
    apply_btn_type = "xpath"
    frame_apply_btn = "//p[@class='footer']/button"

    def fixed_time_switch_click(self):
        self.click(self.fixed_time_switch_type, self.fixed_time_switch)

    def action_time_input_text(self):
        self.send_keys(self.action_time_input_type, self.action_time_input, self.action_time)

    def action_time_input_text_same(self):
        self.send_keys(self.action_time_input_type, self.action_time_input, self.action_time1)

    def off_time_input_text(self):
        self.send_keys(self.off_time_input_type, self.off_time_input, self.off_time)

    def everyday_li_click(self):
        self.click(self.weekly_repeat_input_type, self.weekly_repeat_div)
        self.click(self.weekly_repeat_input_type, self.everyday_li)

    def tag_click(self):
        self.click(self.action_time_input_type, self.tag_div)

    def apply_btn_click(self):
        self.click(self.apply_btn_type, self.apply_btn)

    def frame_apply_btn_click(self):
        self.click(self.apply_btn_type, self.frame_apply_btn)
