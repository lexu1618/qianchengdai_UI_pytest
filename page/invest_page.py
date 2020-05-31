"""
====================================
Author：樵夫
Time：2020/5/24    3:40
====================================
"""
from common.base_page import BasePage
from locator.invest_locator import InvestLocator
import time


class InvestPage(BasePage):

    def get_user_amount(self):
        """获取用户投资前余额"""
        return self.get_element_attrbute(InvestLocator.invest_ele, "data-amount", "投资_获取投资前余额")

    def input_invest_money(self, money):
        """输入投资金额"""
        self.driver.find_element(*InvestLocator.invest_ele).clear()
        self.input_text(InvestLocator.invest_ele, money, "投资_输入投资金额")

    def click_invest_all(self):
        """点击全投勾选框"""
        self.click_element(InvestLocator.invest_all_ele, "投资_点击全投勾选框")

    def click_invest_btn(self):
        """点击投资按钮"""
        self.click_element(InvestLocator.invest_btn, "投资_点击投资按钮")

    def get_invest_btn_info(self):
        """获取投资按钮提示信息"""
        time.sleep(1)
        return self.get_element_text(InvestLocator.invest_btn, "投资_获取投资按钮提示信息")

    def get_alert_error_info(self):
        """获取错误信息弹框信息"""
        time.sleep(1)
        return self.get_element_text(InvestLocator.alert_error_ele, "投资_获取错误信息弹框信息")

    def click_close_alert_error_info(self):
        """关闭错误信息弹框"""
        self.click_element(InvestLocator.re_alert_error, "投资_关闭错误信息弹框")

    def page_refresh(self):
        """刷新页面"""
        self.driver.refresh()

    def get_invest_info(self):
        """获取页面投资成功的弹窗信息"""
        ele = self.wait_element_visibility(InvestLocator.invest_success, "投资_获取页面投资成功的弹窗信息")
        return ele.text

    def click_invest_success_info(self):
        """ 点击查看投资成功的信息"""
        self.wait_element_clickable(InvestLocator.click_success_info, "投资_点击查看投资成功的信息", timeout=60).click()
