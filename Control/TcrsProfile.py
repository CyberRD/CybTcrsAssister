# -*- coding: utf-8 -*-
import logging
from ConfigParser import SafeConfigParser

_logger = logging.getLogger(__name__)


class Loader(object):

    def __init__(self, profile):

        self._config = SafeConfigParser()
        self._config.read(profile)

        self.login_name = self._config.get('account', 'name')
        self.login_pwd = self._config.get('account', 'pwd')

        self.date_start = self._config.get('timecard-setting', 'date_start')
        self.date_end = self._config.get('timecard-setting', 'date_end')
        self.max_work_hour = self._config.get('timecard-setting', 'max_work_hour')

        # build weekday activities
        self.weekday_activities = []
        for weekday in range(1, 6):

            weekday_section = "weekday%s" % str(weekday)
            assert self._config.has_section(weekday_section), \
                    'There\'s no section:"%s"' % weekday_section

            self.weekday_activities.append(self._config.items(weekday_section))


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )

    profile = Loader("..\Profile.ini")
    print profile.login_name

    print profile.date_start
    print profile.date_end

    print profile.weekday_activities
    # print profile.weekday
    # print unicode(profile.weekday1[0][0]).encode('utf-8')
    # print u''.join(unicode(profile.weekday1[0][0]).encode('utf-8'))