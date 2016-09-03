# -*- coding: utf-8 -*-
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import Select

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
        """

        :param index: start from 0
        :param project_name: name of project name
        :param activity_name: name of activity name
        :return:
        """
        driver = self.driver

        self.select_project(index, project_name)

        activity_loc_name = 'activity%s' % str(index)
        Select(driver.find_element_by_name(activity_loc_name))\
            .select_by_visible_text(activity_name)

    def select_project(self, index, project_name):
        """

        :param index: start from 0
        :param project_name:
        :return:
        """
        driver = self.driver
        proj_loc_name = 'project%s' % str(index)
        Select(driver.find_element_by_name(proj_loc_name)) \
            .select_by_visible_text(project_name)

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
        name = "activity" + str(index)

        return self.get_selected_value(name)

    def click_next_week(self):
        driver = self.driver

        loc = "next_week >>"
        driver.find_element_by_link_text(loc).click()

    def click_last_week(self):
        driver = self.driver

        loc = "<< last_week"
        driver.find_element_by_link_text(loc).click()

    def navigate_to_date(self, date):
        driver = self.driver

        date_choose_path = "TCRS/Timecard/timecard_week/daychoose.jsp?cho_date=%s" % str(date)
        driver.get(self.base_url + date_choose_path)

        # assert on the page
        # assert page has been loaded finished

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
    controller.navigate_to_date('2016-09-22')
    # print controller.get_selected_vlaue("project4")
    # controller.test()
