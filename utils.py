from appium import webdriver


def init_driver():
    """驱动对象获取方法"""
    # 实例化驱动对象
    capabilities = {
        "platformName": "Android",  # 平台名称(Android 或 iOS)
        "platformVersion": "5.1",  # 系统版本
        "deviceName": "模拟器",  # 设备名称
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测应用的包名com.android.settings
        "appActivity": ".MainActivity",  # 待测应用的启动名.Settings
        "resetKeyboard": True,  # 解决无法输入中文的问题
        "unicodeKeyboard": True

    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver

if __name__ == '__main__':
    init_driver()
