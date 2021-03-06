from page.basepage import BasePage
from page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps("../page/market_page.yaml", "goto_search")
        # self.find_and_click((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"))
        return SearchPage(self.driver)