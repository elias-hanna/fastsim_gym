import logging
from gym.envs.registration import register
from os.path import dirname, join

default_env = "assets/LS_maze_hard.xml"
empty_env = "assets/empty_map.xml"

logger = logging.getLogger(__name__)

register(
    id='FastsimSimpleNavigation-v0',
    entry_point='gym_fastsim.simple_nav:SimpleNavEnv',
    kwargs={"xml_env":join(dirname(__file__), default_env)}
)

register(
    id='FastsimEmptyMapNavigation-v0',
    entry_point='gym_fastsim.simple_nav:SimpleNavEnv',
    kwargs={"xml_env":join(dirname(__file__), empty_env)}
)

register(
    id='FastsimSimpleNavigationPos-v0',
    entry_point='gym_fastsim.simple_nav_pos:SimpleNavPosEnv',
    kwargs={"xml_env":join(dirname(__file__), default_env)}
)

register(
    id='FastsimEmptyMapNavigationPos-v0',
    entry_point='gym_fastsim.simple_nav_pos:SimpleNavPosEnv',
    kwargs={"xml_env":join(dirname(__file__), empty_env)}
)
