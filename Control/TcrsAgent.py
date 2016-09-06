# -*- coding: utf8 -*-
import logging
from datetime import datetime

from TcrsDataCollection import WeekActivities
from PageObject.PageTcrs import PageTcrs
import TcrsProfile
from PageObject.loc.ActivityOption import activities_to_project

_logger = logging.getLogger(__name__)


class Agent(object):

    def __init__(self, profile_path):
        self.tcrs_profile = TcrsProfile.Loader(profile_path)
        self.tcrs_page = PageTcrs()

    def navigate_to_timecard_page(self):

        profile = self.tcrs_profile

        self.tcrs_page.navigate_to_timecard_page(profile.login_name, profile.login_pwd)

    def run_steps(self):

        profile = self.tcrs_profile
        week_activities = WeekActivities(profile.weekday_activities,
                                         profile.max_work_hour)

        # self.tcrs_page.navigate_to_date(profile.date_start)
        """
        while(True):
            fill in activities(weekday_start, weekday_end)
            if not end_date_in_the_page:
                page.click_next()
            else:
                break
        """

        for activity, hour_list in week_activities.matrix.iteritems():
            print activity, activities_to_project.get(activity)

    def fillin_week_timecard(self,
                             activities_matrix,
                             weekday_start=1,
                             weekday_end=5):
        pass

    def _get_page_weekday_range_by_date(self):

        profile = self.tcrs_profile

        weekday_start = 1
        weekday_end = 5

        # find start weekday
        for weekday in range(1, 6):
            page_date, weekday_str = self.tcrs_page.get_date_of_weekday(weekday)
            # TODO: compare date
            if page_date >= profile.date_start:
                weekday_start = weekday
                break
            else:
                continue

        # find end weekday
        for weekday in range(1, 6)[::-1]:
            page_date, weekday_str = self.tcrs_page.get_date_of_weekday(weekday)
            # TODO: compare date
            if page_date <= profile.date_end:
                weekday_end = weekday
                break
            else:
                continue

        return weekday_start, weekday_end

    def end_date_in_the_page(self):

        profile = self.tcrs_profile
        date_end_obj = datetime.strptime(profile.date_end, "%Y-%m-%d")

        end_in_the_page = False

        for weekday in range(1, 6)[::-1]:

            page_date, weekday_str = self.tcrs_page.get_date_of_weekday(weekday)
            page_date_obj = datetime.strptime(page_date, "%m-%d")
            page_date_obj = page_date_obj.replace(date_end_obj.year)

            # TODO: compare date
            if page_date_obj < date_end_obj:
                continue
            elif page_date_obj == date_end_obj:
                end_in_the_page = True
            else:
                raise Exception("date_end setting error!!")

        return end_in_the_page

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )

    agent = Agent("..\Profile.ini")
    agent.run_steps()
    # agent.navigate_to_timecard_page()