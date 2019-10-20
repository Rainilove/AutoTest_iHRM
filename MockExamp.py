"""
   场景: 电商网站后端未实现，但是要求，点击某个商品的链接是，可以返回具体的商品信息

"""
from unittest import mock

# 后端
data = {
    "name": "apple 11",
    "price": "10000",
    "color": "red"
}
product = mock.Mock(return_value=data)

# 前端
print(product.return_value.get("name"))
print(product.return_value.get("price"))
print(product.return_value.get("color"))
