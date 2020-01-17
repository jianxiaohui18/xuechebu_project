import page
from base.base_page import BasePage


class LoginPage(BasePage):
    username = page.username_box
    password = page.password_box
    login_btn = page.login_btn
    alter_btn = page.alter_btn
    def input_username(self,username):
        self.input_func(self.username,username)    #输入用户名
    def input_password(self,pwd):
        self.input_func(self.password, pwd)    #输入密码
    def click_login_btn(self):
        self.click_func(self.login_btn)    #点击登录按钮
    def click_alter_btn(self):
        self.click_func(self.alter_btn)    #点击弹出框中的警告