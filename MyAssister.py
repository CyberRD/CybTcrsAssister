# -*- coding: utf-8 -*-

from Control.TcrsAgent import Agent
from Utils.LoggingHelper import *

logger = get_logger('./logging.ini')

logging.basicConfig(
    format='[%(asctime)s] %(levelname)s [%(funcName)s] - %(message)s [%(filename)s:%(lineno)d]',
    level=logging.DEBUG,
    datefmt='%y-%m-%d %H:%M:%S'
)


agent = Agent("Profile.ini")
agent.navigate_to_timecard_page()
agent.run_steps()
