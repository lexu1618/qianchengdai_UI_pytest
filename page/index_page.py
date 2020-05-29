"""
====================================
Author：樵夫
Time：2020/5/15    21:18
====================================
"""
from locator.index_locator import IndexLocator


class IndexPafe:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def my_use_info(self):
        """获取我的账户信息"""
        try:
            self.driver.find_element(*IndexLocator.user_info)
        except:
            return '登录失败'
        else:
            return '登录成功'

    def click_quit(self):
        """点击退出登录"""
        self.driver.find_element(*IndexLocator.quit_btn).click()

    def click_toubiao(self):
        """点击进入抢投标"""
        self.driver.find_element(*IndexLocator.invest_btn).click()