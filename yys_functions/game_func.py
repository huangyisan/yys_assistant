from yys_functions.win32_func import compare_rgb, click_mouse
from functools import wraps
from configparser import ConfigParser,NoOptionError
from yys_functions.decorater import dry_run


# running状态存储pixel info
pixel_info = {}

# control dry run mode
flag = True
@dry_run(flag)
def team_page(pos='team_pic_pos',click_pos='c_team_start_pos')->bool:
    '''
    判定是否是组队界面，如果是，则点击开始按钮
    :param pos:  判断界面
    :param click_pos: 开始按钮
    :return:
    '''

    while True:
        if compare_rgb(pos):
            click_mouse(click_pos)
            return True

@dry_run(flag)
def battle_ready(pos='simhun_ready_pos',click_pos='c_simhun_ready_pos')->bool:
    '''
    判定是否为战斗准备阶段，如果是，则点击准备鼓面按钮
    :return: 
    '''
    while True:
        if compare_rgb(pos):
            click_mouse(click_pos)
            return True

@dry_run(flag)
def battle_during(pos):
    '''
    判定当前是否处于战斗阶段
    :return:
    '''
    while True:
        if not compare_rgb(pos):
            return True

def battle_end(pos='p_background_pic_pos',click_pos='c_open_box_pos'):
    '''
    判定当前战斗是否结束,鬼火状态消失，则一直点击，准备开箱，直到找到结束背景色或者组队界面，则停止
    :param pos: 鬼火位置
    :param click_pos:  开箱位置
    :return:
    '''

    while True:
        if not compare_rgb(pos):
            click_mouse(click_pos)
        else:
            return True

def select_position(click_pos):
    '''

    :param click_pos: 式神位置
    :return:
    '''
    click_mouse(click_pos,random_num=2)

def reward_page(pos,click_pos):
    '''
    悬赏封印情况
    :param pos:  悬赏封印pos
    :param click_pos:  是否接受
    :return:
    '''

    if compare_rgb(pos):
        click_mouse(click_pos)

@dry_run(flag)
def test_func(a):
    print(a)
