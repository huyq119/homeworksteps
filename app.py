"""
__author__ = 'huyuqi'
__time__ = '2021/2/8 下午9:34'
__desc__ = ''
"""

# 启动app、关闭app、重启app、进入首页。。。
import yaml
from appium import webdriver

from basepage import BasePage
from page.main_page import MainPage


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = "com.xueqiu.android.common.MainActivity"

    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = yaml.safe_load(open("./configuration.yml"))["caps"]["deviceName"]
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = "true"
            caps["unicodeKeyBoard"] = "true"
            caps["resetKeyBoard"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
