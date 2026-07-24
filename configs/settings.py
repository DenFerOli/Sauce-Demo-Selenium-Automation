import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = 'https://www.saucedemo.com/'

DEFAULT_TIMEOUT = 10
IMPLICIT_WAIT = 5
PAGE_LOAD_TIMEOUT = 30
PAGE_LOAD_STRATEGY = 'normal'

DATA_DIR = os.path.join(BASE_DIR, 'data')
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")