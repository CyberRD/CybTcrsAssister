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
        page = self.tcrs_page

        page.navigate_to_date(profile.date_start)
        while True:
            weekday_start, weekday_end = self._get_page_weekday_range_by_date()
            week_activities = WeekActivities(profile.weekday_activities,
                                             profile.max_work_hour)

            self.fillin_week_timecard(week_activities.matrix,
                                      weekday_start,
                                      weekday_end)
            # page.click_save()

            # TODO: rename appropriate name of _page_date_exceed_end_date
            if not self._page_date_exceed_end_date():
                page.click_next_week()
            else:
                # exceed end date
                break

    def fillin_week_timecard(self,
                             activities_matrix,
                             weekday_start=1,
                             weekday_end=5):

        page = self.tcrs_page

        # TODO: still need check the activities have been selected.

        # prepare a list for duplicated activities
        target_activity_list = []
        for activity, hour_list in activities_matrix.iteritems():
            target_activity_list.append((activity, hour_list))

        activity_index = 0
        # for activity, hour_list in activities_matrix.iteritems():
        for activity, hour_list in target_activity_list:

            project = activities_to_project.get(activity)
            # _logger.debug(type(project), type(activity))

            # activity locator should be unicode
            activity = unicode(activity, 'utf-8')
            page.select_activity(activity_index, project, activity)

            for weekday in range(weekday_start, weekday_end + 1):
                spent_hour = hour_list[weekday]
                if spent_hour > 0:
                    spent_hour = self._convert_to_tcrs_loc_format(spent_hour)
                    page.select_spent_hours(activity_index, weekday, spent_hour)

            activity_index += 1

    @classmethod
    def _convert_to_tcrs_loc_format(cls, spent_hour):
        return str(int(spent_hour)) if spent_hour % 1.0 == 0.0 else str(spent_hour)

    def _get_page_weekday_range_by_date(self):

        profile = self.tcrs_profile

        weekday_start = 1
        weekday_end = 5

        # find start weekday
        date_start_obj = datetime.strptime(profile.date_start, "%Y-%m-%d")
        for weekday in range(1, 6):
            page_date, weekday_str = self.tcrs_page.get_date_of_weekday(weekday)
            page_date_obj = datetime.strptime(page_date, "%m-%d")
            page_date_obj = page_date_obj.replace(date_start_obj.year)

            if page_date_obj >= date_start_obj:
                weekday_start = weekday
                break
            else:
                continue

        # find end weekday
        date_end_obj = datetime.strptime(profile.date_end, "%Y-%m-%d")
        for weekday in range(1, 6)[::-1]:
            page_date, weekday_str = self.tcrs_page.get_date_of_weekday(weekday)

            page_date_obj = datetime.strptime(page_date, "%m-%d")
            page_date_obj = page_date_obj.replace(date_end_obj.year)

            if page_date_obj <= date_end_obj:
                weekday_end = weekday
                break
            else:
                continue

        return weekday_start, weekday_end

    def _page_date_exceed_end_date(self):

        profile = self.tcrs_profile
        date_end_obj = datetime.strptime(profile.date_end, "%Y-%m-%d")

        end_in_the_page = False

        for weekday in range(1, 8)[::-1]:

            page_date, weekday_str = self.tcrs_page.get_date_of_weekday(weekday)
            page_date_obj = datetime.strptime(page_date, "%m-%d")
            page_date_obj = page_date_obj.replace(date_end_obj.year)

            if page_date_obj < date_end_obj:
                continue
            elif page_date_obj >= date_end_obj:
                end_in_the_page = True
            else:
                _logger.error(page_date)
                raise Exception("Error page date.")

        return end_in_the_page

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )

    agent = Agent("..\Profile.ini")
    agent.navigate_to_timecard_page()
    agent.test()
    # agent.navigate_to_timecard_page()
    # agent.run_steps()
    # agent.navigate_to_timecard_page()