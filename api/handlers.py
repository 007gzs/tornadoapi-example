# encoding: utf-8
from __future__ import absolute_import, unicode_literals

from tornadoapi import fields
from tornadoapi.conf import settings
from tornadoapi.core.err_code import ErrCode
from tornadoapi.handler import ApiHandler, ApiDocHandler


class BaseHandler(ApiHandler):

    def options(self, *args, **kwargs):
        self.finish()


class TestHandler(BaseHandler):
    test_param = fields.CharField(description='测试参数', default=None)
    test_choice = fields.ChoiceField(description='选择参数', default=None, choices=((0, '选项0'), (1, '选项1')))

    @classmethod
    def get_return_sample(cls):
        return ErrCode.SUCCESS.get_res_dict(data={'test_param': '测试参数', 'test_choice': '选择参数', 'title': '配置中TITLE'})

    @classmethod
    def get_handler_name(cls):
        return '测试'

    def get(self, *args, **kwargs):
        ret = {
            'test_param': self.test_param,
            'test_choice': self.test_choice,
            'title': settings.TITLE
        }
        self.write_api(ret)


default_handlers = [

    (r'doc', ApiDocHandler),
    (r'test/(?P<testparam>.*?)', TestHandler, {}, '测试'),
]
