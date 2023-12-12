from auto_search.auto_search import auto_search, chrome, safari
from game_bot_2048.bot import execute
from util.util import click

# Integrates previously implemented scripts so that we can automate multiple tasks with only 1 execution.
# Especially helpful for AFKing overnight.

# Set Safari browser icon position
icon = [320, 1065]

execute()
click(425, 60, 2, 2)
auto_search(7, 10, chrome)
click(icon[0], icon[1], 15, 15)
auto_search(3, 5, safari)
