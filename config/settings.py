# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import os

from config.local_settings import *  # NOQA


DEBUG = os.environ.get('IS_DEBUG', '1') != '0'

TITLE = 'test'

ERROR_CODE_DEFINE = (
    ('ERR_ACTION_NOT_FOUND',            10001,  '未找到 action '),
)
