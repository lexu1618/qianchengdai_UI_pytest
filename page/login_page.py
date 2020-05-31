"""
====================================
Author：樵夫
Time：2020/5/15    21:19
====================================
"""
from common.base_page import BasePage
from common.handleconfig import config
from locator.login_locator import LoginLocator


class LoginPage(BasePage):
    url = config.get("env", "base_url") + config.get("url", "login_url")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)

    def login(self, user, pwd):
        """输入账号密码，登录"""
        self.input_text(LoginLocator.phone_ele, user, "登录_账号输入")
        self.input_text(LoginLocator.pwd_ele, pwd, "登录_密码输入")
        self.click_element(LoginLocator.login_btn, "登录_点击登录按钮")

    def get_error_info(self):
        """获取文本错误信息"""
        return self.get_element_text(LoginLocator.error_info,"登录_文本错误信息")

    def get_tips_info(self):
        """获取弹窗信息"""
        ele = self.wait_element_visibility(LoginLocator.alert_info,"登录_弹窗错误信息")
        return ele.text

    def page_refresh(self):
        """刷新页面"""
        self.driver.get(url=self.url)

    def click_re_mobile(self):
        """点击取消记住手机号"""
        self.click_element(LoginLocator.re_mobile,"登录_点击取消记住手机号")
