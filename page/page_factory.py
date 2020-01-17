from page.first_page import FirstPage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):
    def __init__(self,driver):
        self.driver = driver

    def first_page(self):
        return FirstPage(self.driver)

    def mine_page(self):
        return MinePage(self.driver)

    def login_page(self):
        return LoginPage(self.driver)
