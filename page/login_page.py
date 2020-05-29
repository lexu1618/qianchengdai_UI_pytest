"""
====================================
Author：樵夫
Time：2020/5/15    21:19
====================================
"""
from common.handleconfig import config
from locator.login_locator import LoginLocator


class LoginPage:
    url = config.get("env", "base_url") + config.get("url", "login_url")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)

    def login(self, user, pwd):
        """输入账号密码，登录"""
        self.driver.find_element(*LoginLocator.phone_ele).send_keys(user)
        self.driver.find_element(*LoginLocator.pwd_ele).send_keys(pwd)
        self.driver.find_element(*LoginLocator.login_btn).click()

    def get_error_info(self):
        """获取文本错误信息"""
        res = self.driver.find_element(*LoginLocator.error_info).text
        return res

    def get_tips_info(self):
        """获取弹窗信息"""
        res = self.driver.find_element(*LoginLocator.alert_info).text
        return res

    def page_refresh(self):
        """刷新页面"""
        self.driver.get(url=self.url)

    def click_re_mobile(self):
        """点击取消记住手机号"""
        self.driver.find_element(*LoginLocator.re_mobile).click()
