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

    def __init__(self, web_driver):
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

    def select_activity(self, index, project_name, activity_name):
        raise NotImplementedError()

    def select_spent_hours(self, loc, hour):
        driver = self.driver

        Select(driver.find_element_by_name(loc)).select_by_visible_text(hour)
        # _logger.debug(Select(driver.find_element_by_name(loc)).first_selected_option.text)

    def get_selected_value(self, loc):
        driver = self.driver

        return Select(driver.find_element_by_name(loc)).first_selected_option.text.strip()

    def click_save(self):
        driver = self.driver
        driver.find_element_by_name("save2").click()

    def click_submit(self):
        driver = self.driver
        driver.find_element_by_name("submit").click()

    def get_weekday_of_date(self, weekday):
        """

        :param weekday: start from 1, ex: Monday=1, Tuesday=2...etc
        :return:
        """
        driver = self.driver

        index_of_weekday = int(weekday) + 3
        xpath = "//tr[2]/td[%s]" % str(index_of_weekday)
        print xpath
        date_weekday = driver.find_element_by_xpath(xpath).text
        _logger.debug(date_weekday)
        date = date_weekday.split('\n')[0].strip()
        weekday = date_weekday.split('\n')[1].strip()

        return date, weekday

    def get_activity_name_by_index(self, index):
        """

        :param index: start from 0
        :return:
        """
        driver = self.driver

        name = "activity" + str(index)

        return self.get_selected_value(name)

    def test(self):
        driver = self.driver

        print driver.find_element_by_xpath("//td[6]").text

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )

    controller = PageTcrs('Firefox')
    controller.navigate_to_timecard_page('alanliu', 'S@201609')
    controller.select_spent_hours("record1_3", "4")
    print controller.get_weekday_of_date(1)
    print controller.get_activity_name_by_index(0)
    # print controller.get_selected_vlaue("project4")
    # controller.test()
