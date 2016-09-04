# -*- coding: utf-8 -*-

import logging

from Control.TcrsAgent import Agent

_logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
        level=logging.DEBUG,
        datefmt='%y-%m-%d %H:%M:%S'
    )

    # profile = Loader("Profile.ini")
    #
    # activity_map1 = VirtualActivitiesMatrix(profile.weekday_activities,
    #                                         profile.max_work_hour)


