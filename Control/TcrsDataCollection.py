# -*- coding: utf-8 -*-
import logging
import numpy

_logger = logging.getLogger(__name__)

SPENT_HOUR = numpy.linspace(0, 8, 17)


class WeekActivitiesMatrix(object):

    def __init__(self, weekday_activities_row_setting, max_hour):

        self._activity_map = {}
        self._max_hour = max_hour

        for weekday in range(1, 6):

            for activity_name, time_range in weekday_activities_row_setting[weekday - 1]:

                print activity_name, time_range

                if not str(activity_name).startswith("rest"):
                    # add to map
                    self._build_activity(activity_name)

                    # decide work hour
                    if "-" in time_range:
                        pass
                    elif type(time_range) == int:
                        pass
                    else:
                        pass

                else:
                    # build rest
                    rest_activity_name = time_range  # this is the ini input format
                    self._build_activity(rest_activity_name)

    def _build_activity(self, activity_name):
        if activity_name not in self._activity_map:
            # build a map weekday spent hour list with [%no use%, %Mon.%, ..., %Sat.%]
            self._activity_map[activity_name] = [-1, 0, 0, 0, 0, 0, 0]

    def _total_spent_hours_of_weekday(self, weekday):

        total_spent_hours = 0
        for activity_name, spent_hour_list in self._activity_map.iteritems():
            total_spent_hours += spent_hour_list[weekday]

        return total_spent_hours

    @classmethod
    def _get_spent_hour(cls, time_range, max_hour, current_spent_hour):

        if max_hour - current_spent_hour > 0:
            pass

        if "-" in time_range:
            pass

    @property
    def activity_map(self):
        return self._activity_map

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )
