# encoding: UTF-8
from __future__ import (
    print_function, unicode_literals, division, absolute_import
)
import os


class Constant(object):
    conf_dir = os.path.join('.', '.netease-musicbox')
    try:
        os.mkdir(conf_dir)
    except Exception as e:
        print(e) 
    download_dir = os.path.join(conf_dir, 'cached')
    config_path = os.path.join(conf_dir, 'config.json')
    storage_path = os.path.join(conf_dir, 'database.json')
    cookie_path = os.path.join(conf_dir, 'cookie')
    log_path = os.path.join(conf_dir, 'musicbox.log')
