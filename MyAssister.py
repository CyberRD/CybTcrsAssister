# -*- coding: utf-8 -*-

import logging

# from PageObject.PageTcrs import PageTcrs
from Control.Profile import ProfileLoader
from Control import TimeCard

_logger = logging.getLogger(__name__)


profile = ProfileLoader('Profile.ini')


controller = TimeCard.Action()
controller.navigate_to_timecard_page(profile.login_name, profile.login_pwd)
controller.fill_activity(profile.date_start,
                         profile.date_end,
                         virtual_activities_map)


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )