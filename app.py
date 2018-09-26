# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import os

from tornado import web
from tornadoapi.conf import settings
from tornadoapi.core import url_path_join
from tornadoapi.handler import NotFoundHandler

base_dir = os.getcwd()


def load_handlers(name):
    mod = __import__(name, fromlist=['default_handlers'])
    return mod.default_handlers


class TestApiApplication(web.Application):
    def __init__(self):
        config = {
            'debug': settings.DEBUG,
            'xsrf_cookies': False,
            'gzip': True,
            'autoreload': False,
            'base_url': '/api/',
            'headers': {"Access-Control-Allow-Origin": "*"}
        }

        handlers = self.init_handlers(config)
        super(TestApiApplication, self).__init__(handlers, **config)

    def init_handlers(self, config):
        """Load the (URL pattern, handler) tuples for each component."""

        # Order matters. The first handler to match the URL will handle the request.
        handlers = []
        handlers.extend(load_handlers('api.handlers'))

        # prepend base_url onto the patterns that we match
        new_handlers = []
        for handler in handlers:
            pattern = url_path_join(config['base_url'], handler[0])
            new_handler = tuple([pattern] + list(handler[1:]))
            new_handlers.append(new_handler)
        # add 404 on the end, which will catch everything that falls through
        new_handlers.append((r'(.*)', NotFoundHandler))
        return new_handlers
