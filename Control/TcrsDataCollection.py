# -*- coding: utf-8 -*-
import logging
import random
import numpy

_logger = logging.getLogger(__name__)


class WeekActivities(object):

    SPENT_HOUR_OPTIONS = numpy.linspace(0, 8, 17)

    def __init__(self, weekday_activities_row_setting, max_work_hour):

        self._activities_matrix = {}
        self._max_work_hour = float(max_work_hour)

        for weekday in range(1, 6):
            for activity_name, time_range in weekday_activities_row_setting[weekday - 1]:

                _logger.debug("%s, %s" % (activity_name, time_range))
                cur_work_hour = self._total_spent_hours_of_weekday(weekday)
                # print cur_work_hour
                if not str(activity_name).startswith("rest"):
                    # add to dict
                    self._build_activity(activity_name)
                    spent_hour = self._get_spent_hour(time_range,
                                                      self._max_work_hour,
                                                      cur_work_hour)
                else:
                    # build rest
                    activity_name = time_range  # this is the ini input format

                    self._build_activity(activity_name)
                    spent_hour = self._max_work_hour - cur_work_hour
                    print spent_hour
                    spent_hour = self._get_hour_format(spent_hour)

                self._activities_matrix.get(activity_name)[weekday] = spent_hour

    @property
    def matrix(self):
        return self._activities_matrix

    def _build_activity(self, activity_name):
        if activity_name not in self._activities_matrix:
            # build a map weekday spent hour list with [%no use%, %Mon.%, ..., %Sat.%]
            self._activities_matrix[activity_name] = [-1, 0, 0, 0, 0, 0, 0]

    def _total_spent_hours_of_weekday(self, weekday):

        total_spent_hours = 0
        for activity_name, spent_hour_list in self._activities_matrix.iteritems():
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
            choose_index_start = int(range_start * 2)
            choose_index_end = int(range_end * 2) + 1
            spent_hour = random.choice(cls.SPENT_HOUR_OPTIONS[choose_index_start:choose_index_end])
        else:
            spent_hour = cls._get_hour_format(time_range)

        # check remaining hours
        if max_work_hour - current_spent_hour - spent_hour >= 0:
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
            _logger.error("in_str: %s" % in_str)
            raise Exception('time range should be like "1.5~3" '
                            'or exactly a number. e.g. "3".')

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )
