"""
    场景:
        1.测试购物车接口，需要提前使用手机验证码登录
        2.关注点是购物车接口，而手机验证码登录实现繁琐
        3.需要简化登录，比如:输入任意手机验证码都可以登录成功
    流程：
        1.导包
        2.创建 mock 服务对象(预定义返回数据)
        3.使用 mock 服务替换真正的服务器服务
    注意:
        python 之前版本 mock 需要单独安装的， pip install mock
        之后集成进 unittest
"""
import unittest
# 导包
from unittest import mock


# 登录功能(开发编写的)
def login(tel, code):
    # ..... 业务实现
    return False


# 购物车功能
def cart():
    print("显示购物车信息")


# 测试
class TestShop(unittest.TestCase):
    def test_cart(self):
        # 创建mock服务
        mock_login = mock.Mock(return_value=True)

        # 前置条件:先登录
        # flag = login("13012345678", "6666")
        flag = mock_login("120", "8888")
        print("登录结果:", flag)
        # 确保登录成功,再测试购物车
        if flag:
            cart()
        else:
            print("登录失败")
