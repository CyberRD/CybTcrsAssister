# -*- coding: utf8 -*-
import logging
from datetime import datetime
import time

from TcrsDataCollection import WeekActivities
from PageObject.PageTcrs import PageTcrs
import TcrsProfile
from PageObject.loc.ActivityOption import activities_to_project


class Agent(object):

    def __init__(self, profile_path, office_pwd):
        self.tcrs_profile = TcrsProfile.Loader(profile_path, office_pwd)
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
            page.click_save()

            # TODO: need to refactor to check all working hours have been selected and saved.
            time.sleep(5)

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
        """
        :param activities_matrix: which is a virtual data structure
                                  from TcrsDataCollection.WeekActivities,
                                  so it not consider with real selected status
        :param weekday_start: on this page which weekday should be for choosing start day
                             , it depends on the profile setting
        :param weekday_end: on this page which weekday should be for choosing end day
                            , it depends on the profile setting
        """

        page = self.tcrs_page

        already_selected_activity_list = []
        selected_activity_index = 0
        # check if there's selected activity or not
        while True:
            if page.is_activity_selected(selected_activity_index):
                already_selected_activity_list.append(page.get_selected_activity(selected_activity_index))
                selected_activity_index += 1
            else:
                break

        # prepare a matrix for selected and un-selected activities working hour
        for activity, hour_list in activities_matrix.iteritems():
            if unicode(activity, 'utf-8') in already_selected_activity_list:
                logging.debug("%s has been selected in this page." % activity)
                tmp_index = already_selected_activity_list.index(unicode(activity, 'utf-8'))
                already_selected_activity_list[tmp_index] = (activity, hour_list)
            else:
                already_selected_activity_list.append((activity, hour_list))

        logging.debug("already_selected_activity_list:")
        logging.debug(already_selected_activity_list)

        activity_index = 0
        # fill in hours
        for activity, hour_list in already_selected_activity_list:

            project = activities_to_project.get(activity)
            # _logger.debug(type(project), type(activity))

            if activity_index >= selected_activity_index:
                # activity locator should be unicode
                page.select_activity(activity_index, project, unicode(activity, 'utf-8'))

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
                logging.debug("select start weekday=%s" % str(weekday))
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
                logging.debug("select end weekday=%s" % str(weekday))
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
                logging.error(page_date)
                raise Exception("Error page date.")

        return end_in_the_page

    def test(self):

        page = self.tcrs_page

        page.navigate_to_date("2016-09-01")
        print page.get_selected_activity(0)
        print type(page.get_selected_activity(0))
        print page.is_activity_selected(0)
        print page.is_activity_selected(4)


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