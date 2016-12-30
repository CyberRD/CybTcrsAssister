# -*- coding: utf-8 -*-

import getpass

from Control.TcrsAgent import Agent
from utils.LoggingHelper import *

logger = get_logger('./logging.ini')

logging.basicConfig(
    format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
    level=logging.DEBUG,
    datefmt='%y-%m-%d %H:%M:%S'
)

office_pwd = getpass.getpass("Please input your domain password:")

agent = Agent("Profile.ini", office_pwd)
agent.navigate_to_timecard_page()
agent.run_steps()
