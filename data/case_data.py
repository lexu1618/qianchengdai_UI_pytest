"""
====================================
Author：樵夫
Time：2020/5/15    21:39
====================================
"""


class LoginCase:
    """登录功能测试用例"""
    #   正常功能测试用例
    success_case_data = [
        {'mobile': "13760246701", 'pwd': "python", "expected": "登录成功"}
    ]

    #   异常功能测试用例_错误信息在页面上
    error_info_case_data = [
        {'mobile': "", 'pwd': "python", "expected": "请输入手机号"},
        {'mobile': "13760246701", 'pwd': "", "expected": "请输入密码"},
        {'mobile': "186118470553", 'pwd': "python", "expected": "请输入正确的手机号"}
    ]

    #   异常功能测试用例_错误信息在弹窗上
    error_alert_case_data = [
        {'mobile': "13760246701", 'pwd': "python1", "expected": "帐号或密码错误!"},
        {'mobile': "15146734123", 'pwd': "python", "expected": "此账号没有经过授权，请联系管理员!"}
    ]


class InvestCase:
    """投标功能测试用例"""

    #   正常投标功能测试用例
    success_case_data = [
        {'title': '投资成功', 'amount': "1000", "expected": "投标成功！"}
    ]

    #   文本框_错误投标功能测试用例
    error_ele_case_data = [
        {'title': '金额为1', 'amount': "1", "expected": "请输入10的整数倍"},
        {'title': '金额非10的倍数', 'amount': "456", "expected": "请输入10的整数倍"},
        {'title': '金额为字母', 'amount': "a", "expected": "请输入10的整数倍"},
        {'title': '金额为特殊字符', 'amount': "!!", "expected": "请输入10的整数倍"}
    ]

    #   弹窗_错误投标功能测试用例
    error_alert_case_data = [
        {'title': '金额为空', 'amount': " ", "expected": "请正确填写投标金额"},
        {'title': '金额为负数', 'amount': "-10", "expected": "请正确填写投标金额"},
        {'title': '金额为0', 'amount': "0", "expected": "请正确填写投标金额"},
        {'title': '金额为10的倍数少于100', 'amount': "50", "expected": "投标金额必须为100的倍数"}
    ]
