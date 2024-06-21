import json
import logging
from test_cases.api_domain_service_base import DomainService


class DomianServiceManager(DomainService):
    def post_SetAutoRenew(self, data, **kwargs):
        """开启/关闭自动续费功能"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.SetAuto_Renew(params=params, data=data)
        return _, resp

    def get_QuerySingle_DomainPrice(self, **kwargs):
        """域名询价"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.QuerySingle_DomainPrice(params=params)
        return _, resp

    # 这是一个方法定义，他接受一个self参数(通常用于只想当前对象)以及其他可能的参数
    def get_GetShoppingList(self):
        """获取购物车列表内容"""
        # 在方法内部，使用self.api.GetShoppingList()调用了一个名为GetShoppingList的函数(方法)，并将返回的结果存储在变量resp中，这里使用了通配符_来忽略第一个返回值。
        _, resp = self.api.GetShoppingList()
        # 这一行代码的目的是从resp对象中提取出购物车列表的内容：
        # 首先使用json.dumps(resp)将resp对象转换成JSON格式的字符串，
        # 然后使用json,loads(…)将其转换成Python对象(字典)
        # 接下来，使用.get("Result")从字典中获取键值为"Result"的值，
        # 再使用.get("domain_list")从上一步获得的值中获取键为"domain_list"的值，并将结果赋值给变量domain_list
        domain_list = json.loads(json.dumps(resp)).get("Result").get("domain_list")
        # 使用logging.info函数将一条日志记录写入日志文件或输出到控制台，日志消息是一个字符串，其中包含了购物车列表的长度信息，%s是一个占位符，用于将len(domain_list)的值插入到日志消息中
        logging.info("domain list len is --> %s" % len(domain_list))
        # 最后返回一个元组，包含两个参数
        return _, domain_list

    def post_AddDomain_ToShoppingList(self, data, **kwargs):
        """单个-添加到购物车"""
        params = {
            "domina": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.AddDomain_ToShoppingList(params=params, data=data)
        return _, resp

    def post_BatchAddDomain_ToShoppingList(self, data, **kwargs):
        """批量-添加到购物车"""
        params = {
            "domina": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.BatchAddDomain_ToShoppingList(params=params, data=data)
        return _, resp

    def post_Remove_DomainFromShoppingList(self, data, **kwargs):
        """删除购物车中单个域名"""
        params = {
            "domina": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.BatchAddDomain_ToShoppingList(params=params, data=data)
        return _, resp
