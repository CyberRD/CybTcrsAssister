# -*- coding: utf-8 -*-

import logging

from PageObject.PageTcrs import PageTcrs
from Control import Profile

_logger = logging.getLogger(__name__)


profile = Profile('Profile.ini')


controller = PageTcrs()
controller.navigate_to_timecard_page(profile.login_name, profile.login_pwd)
controller.fill_activity(profile.date_start, profile.date_end)


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )