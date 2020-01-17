from selenium.webdriver.common.by import By

#首页
mine_btn = By.XPATH,'//*[contains(@text,"我的")]'    #我的按钮

#我的页面
log_reg_btn = By.XPATH,'//*[contains(@text,"登录")]'   #登录/注册按钮
username_text = By.XPATH,'//*[contains(@text,"用户")]'

#登录页面
username_box = By.ID,'com.bjcsxq.chat.carfriend:id/login_phone_et'    #用户名输入框
password_box = By.ID,'com.bjcsxq.chat.carfriend:id/login_pwd_et'     #密码输入
login_btn = By.ID,'com.bjcsxq.chat.carfriend:id/login_btn'   #登录按钮
alter_btn = By.ID,'com.bjcsxq.chat.carfriend:id/btn_neg'    #弹窗按钮

