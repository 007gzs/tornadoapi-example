# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import os


if __name__ == '__main__':
    os.environ.setdefault("TORNADOAPI_SETTINGS_MODULE", "config.settings")

    from tornado import ioloop, httpserver
    from tornado.options import options, define, parse_command_line
    from app import TestApiApplication

    define("port", default=8888, help="run on the given port", type=int)
    parse_command_line()
    io_loop = ioloop.IOLoop.instance()
    app = TestApiApplication()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("server start in 0.0.0.0:%d" % options.port)
    io_loop.start()
