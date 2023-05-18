from .common import Common


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ("gunicorn", )
