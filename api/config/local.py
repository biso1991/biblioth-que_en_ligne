import os
from .common import Common

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True
    # import mimetypes
    # mimetypes.add_type("application/zip", ".zip")
    # mimetypes.add_type("application/javascript", ".js")
    # mimetypes.add_type("text/css", ".css")
    # mimetypes.add_type("text/html", ".html")
    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ("django_nose",)
    TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
    NOSE_ARGS = [
        BASE_DIR,
        "-s",
        "--nologcapture",
        "--with-coverage",
        "--with-progressive",
        "--cover-package=api",
    ]
    # Mail
    # EMAIL_HOST = 'localhost'
    # EMAIL_PORT = 1025
