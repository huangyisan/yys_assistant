from yys_functions.game_func import test_func
from yys_functions import game_func

def test1(flag):
    game_func.flag = flag
    test_func('1')

test1(flag=False)