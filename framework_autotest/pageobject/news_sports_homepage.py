from framework.base_page import BasePage


class NewsSportsHomePage(BasePage):

    sport_link_type = 'xpath'
    sport_link = "//*[@id='channel-all']/div/ul/li[7]/a"

    def sport_link_click(self):
        self.click(self.sport_link_type, self.sport_link)
