# -*- coding: utf-8 -*-
import logging
from ConfigParser import SafeConfigParser


_logger = logging.getLogger(__name__)


class ProfileLoader(object):

    def __init__(self, profile):
        self._config = SafeConfigParser()
        SafeConfigParser.read(profile)

        self.login_name = self._config.get('account', 'name')
        self.login_pwd = self._config.get('account', 'pwd')

        self.date_start = self._config('date', 'start')
        self.date_end = self._config('date', 'end')

    def activity_map(self):
        return self._activity_map


if __name__ == '__main__':
    pass