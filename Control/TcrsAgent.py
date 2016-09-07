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

        # for activity, hour_list in week_activities.matrix.iteritems():
        #     print activity, activities_to_project.get(activity)

    def fillin_week_timecard(self,
                             activities_matrix,
                             weekday_start=1,
                             weekday_end=5):

        page = self.tcrs_page

        activity_index = 0
        for activity, hour_list in activities_matrix.iteritems():

            project = activities_to_project.get(activity)
            # _logger.debug(type(project), type(activity))

            activity = unicode(activity, 'utf-8')
            page.select_activity(activity_index,
                                 project,
                                 activity)

            for weekday in range(weekday_start, weekday_end + 1):
                # TODO: dirty work
                hour = str(hour_list[weekday])
                if hour != "0.0":
                    if float(hour) % 1 == 0.0: hour = str(int(float(hour)))
                    page.select_spent_hours(activity_index, weekday, hour)

            activity_index += 1

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
    agent.run_steps()
    # agent.navigate_to_timecard_page()