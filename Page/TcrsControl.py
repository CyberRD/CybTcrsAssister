# -*- coding: utf-8 -*-
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re

_logger = logging.getLogger(__name__)


class TcrsController(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://tcrs.cybersoft4u.com.tw/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def navigate_to_timecard_page(self, login_name, login_pwd):
        driver = self.driver
        driver.get(self.base_url + "/TCRS/login.jsp")
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(login_name)
        driver.find_element_by_name("pw").clear()
        driver.find_element_by_name("pw").send_keys(login_pwd)
        driver.find_element_by_name("Image12").click()
        driver.find_element_by_link_text("Timecard").click()

    def select_project_and_activity(self, project, activity):
        pass

    def select_spent_hours(self, date, activity):
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

    controller = TcrsController()
    controller.navigate_to_timecard_page()