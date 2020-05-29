"""
====================================
Author：樵夫
Time：2020/5/24    3:40
====================================
"""
from locator.invest_locator import InvestLocator
from selenium.webdriver.remote.webdriver import WebDriver
import time

class InvestPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(30)

    def get_user_amount(self):
        """获取用户投资前余额"""
        return self.driver.find_element(*InvestLocator.invest_ele).get_attribute('data-amount')

    def input_invest_money(self, money):
        """输入投资金额"""
        self.driver.find_element(*InvestLocator.invest_ele).clear()
        self.driver.find_element(*InvestLocator.invest_ele).send_keys(money)

    def click_invest_all(self):
        """点击全投勾选框"""
        self.driver.find_element(*InvestLocator.invest_all_ele).click()

    def click_invest_btn(self):
        """点击投资按钮"""
        self.driver.find_element(*InvestLocator.invest_btn).click()

    def get_invest_btn_info(self):
        """获取投资按钮提示信息"""
        time.sleep(1)
        return self.driver.find_element(*InvestLocator.invest_btn).text

    def get_alert_error_info(self):
        """获取错误信息弹框信息"""
        time.sleep(1)
        return self.driver.find_element(*InvestLocator.alert_error_ele).text

    def click_close_alert_error_info(self):
        """关闭错误信息弹框"""
        self.driver.find_element(*InvestLocator.re_alert_error).click()

    def page_refresh(self):
        """刷新页面"""
        self.driver.refresh()

    def get_invest_info(self):
        """获取页面投资成功的弹窗信息"""
        time.sleep(10)
        return self.driver.find_element(*InvestLocator.invest_success).text

    def click_invest_success_info(self):
        """ 点击查看投资成功的信息"""
        time.sleep(10)
        self.driver.find_element(*InvestLocator.click_success_info).click()