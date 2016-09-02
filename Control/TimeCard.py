# -*- coding: utf8 -*-

import logging

from PageObject.PageTcrs import PageTcrs

_logger = logging.getLogger(__name__)


class Action(PageTcrs):

    def __init__(self):
        pass

    def fill_activity(self,
                      date_start,
                      date_end,
                      virtual_activities_map):
        pass

    def is_in_date_range(self, start_date, end_date):
        raise NotImplementedError()

    def is_after_end_date(self, end_date):
        raise NotImplementedError()

    def is_before_start_date(self, start_date):
        raise NotImplementedError()


class TimeCardActivityMap(object):

    def __init__(self, profile):
        self.activity_map = []

    def build(self):
        raise NotImplementedError()
