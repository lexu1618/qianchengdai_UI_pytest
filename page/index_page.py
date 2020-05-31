"""
====================================
Author：樵夫
Time：2020/5/15    21:18
====================================
"""
from common.base_page import BasePage
from locator.index_locator import IndexLocator


class IndexPafe(BasePage):

    def my_use_info(self):
        """获取我的账户信息"""
        try:
            self.get_element(IndexLocator.user_info, "首页_定位我的账户")
        except:
            return '登录失败'
        else:
            return '登录成功'

    def click_quit(self):
        """点击退出登录"""
        self.click_element(IndexLocator.quit_btn, "首页_点击退出登录")

    def click_toubiao(self):
        """点击进入抢投标"""
        self.click_element(IndexLocator.invest_btn, "首页_点击抢投标")
