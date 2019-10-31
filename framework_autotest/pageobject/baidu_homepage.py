from framework.base_page import BasePage


class HomePage(BasePage):

        input_box_type = 'xpath'
        input_box = r"//*[@id='kw']"

        button_type = 'xpath'
        button = r"//*[@id='su']"

        news_link_type = 'xpath'
        news_link = r"//*[@name='tj_trnews']"

        def input_box_send(self, text):
            self.send_keys(self.input_box_type, self.input_box, text)

        def button_click(self):
            self.click(self.button_type, self.button)

        def news_link_click(self):
            self.click(self.news_link_type, self.news_link)

