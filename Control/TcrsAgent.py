# -*- coding: utf8 -*-
import logging

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

    def fillin_by_profile(self):

        profile = self.tcrs_profile
        week_activities = WeekActivities(profile.weekday_activities,
                                           profile.max_work_hour)

        for activity, hour_list in week_activities.matrix.iteritems():
            print activity, activities_to_project.get(activity)

    def fillin_week_timecard(self,
                             activities_matrix,
                             weekday_start=1,
                             weekday_end=5):
        pass

    def get_weekday_range(self, date_start, date_end):

        weekday_start = 1
        weekday_end = 5

        return weekday_start, weekday_end

    def is_in_date_range(self, start_date, end_date):
        raise NotImplementedError()

    def is_after_end_date(self, end_date):
        raise NotImplementedError()

    def is_before_start_date(self, start_date):
        raise NotImplementedError()


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )

    agent = Agent("..\Profile.ini")
    agent.fillin_by_profile()
    # agent.navigate_to_timecard_page()