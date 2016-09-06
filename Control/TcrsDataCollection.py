# -*- coding: utf-8 -*-
import logging
import random
import numpy

_logger = logging.getLogger(__name__)


class WeekActivitiesMatrix(object):

    SPENT_HOUR_OPTIONS = numpy.linspace(0, 8, 17)

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
    def _get_spent_hour(cls, time_range, max_work_hour, current_spent_hour):

        # format check and decide spent hour
        split_symbol = '~'
        if split_symbol in time_range:
            token = time_range.split(split_symbol)
            range_start = cls._get_hour_format(token[0])
            range_end = cls._get_hour_format(token[1])

            # spent hour value should choose from SPENT_HOUR_OPTIONS,
            # so mapping the real hour to list option
            choose_index_start = range_start * 2
            choose_index_end = range_end * 2 + 1
            spent_hour = random.choice(cls.SPENT_HOUR_OPTIONS[choose_index_start:choose_index_end])
        else:
            spent_hour = cls._get_hour_format(time_range)

        # check remaining hours
        if max_work_hour - current_spent_hour + spent_hour >= 0:
            return spent_hour
        else:
            spent_hour = max_work_hour - current_spent_hour
            spent_hour = cls._get_hour_format(spent_hour)
            return spent_hour

    @classmethod
    def _get_hour_format(cls, in_str):

        try:
            trans_num = float(in_str)
            assert trans_num in cls.SPENT_HOUR_OPTIONS, "there's no such spent hour option"
            return trans_num

        except:
            raise Exception('time range should be like "1.5~3" '
                            'or exactly a number. e.g. "3".')

    @property
    def activity_map(self):
        return self._activity_map

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )
