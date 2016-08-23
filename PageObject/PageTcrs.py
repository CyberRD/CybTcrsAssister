# -*- coding: utf-8 -*-
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re

from loc import TcrsControl as loc

_logger = logging.getLogger(__name__)

TCRS_BASE_URL = "https://tcrs.cybersoft4u.com.tw/"


class PageTcrs(object):

    PAGE_URL = "/TCRS/login.jsp"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = TCRS_BASE_URL
        self.verificationErrors = []
        self.accept_next_alert = True

    def navigate_to_timecard_page(self, login_name, login_pwd):
        driver = self.driver

        driver.get(self.base_url + self.PAGE_URL)

        driver.find_element_by_name(loc.name).clear()
        driver.find_element_by_name(loc.name).send_keys(login_name)
        driver.find_element_by_name(loc.password).clear()
        driver.find_element_by_name(loc.password).send_keys(login_pwd)
        driver.find_element_by_name(loc.login_btn).click()

        driver.find_element_by_link_text(loc.tab_timecard).click()

    def select_activity(self, activity_name, project_name=None):
        pass

    def select_spent_hours(self, date, activity_name):
        pass

    def is_spent_hours_set(self, date, activity_name):
        pass

    def save_record(self):
        driver = self.driver
        driver.find_element_by_name("save2").click()


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )

    controller = PageTcrs()
    controller.navigate_to_timecard_page()