import page
from base.base_page import BasePage


class FirstPage(BasePage):
    mine_btn = page.mine_btn
    def click_mine_btn(self):
        self.click_func(self.mine_btn)
