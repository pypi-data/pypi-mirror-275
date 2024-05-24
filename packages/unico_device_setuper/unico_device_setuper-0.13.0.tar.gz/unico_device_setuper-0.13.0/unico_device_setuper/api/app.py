from unico_device_setuper.api import app_maker
from unico_device_setuper.lib import cfg

APP = app_maker.make_app_from_config(cfg.read_config())
