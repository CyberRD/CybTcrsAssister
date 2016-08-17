# coding=UTF-8
import logging

from PageBase import PageTcrsBase
from loc import PageLogin as loc

_logger = logging.getLogger(__name__)


class PageLogin(PageTcrsBase):

    _url_token = "login.jsp"

    def login(self, name, pwd):

        # driver = self._driver
        self._find_element_by_locator(loc.user_name).clear()
        self._find_element_by_locator(loc.user_name).send_keys(name)
        self._find_element_by_locator(loc.password).clear()
        self._find_element_by_locator(loc.password).send_keys(pwd)
        self._find_element_by_locator(loc.login_btn).click()