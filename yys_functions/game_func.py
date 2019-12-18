from win32_func import compare_rgb, click_mouse
from functools import wraps
from configparser import ConfigParser,NoOptionError

def dry_run(flag:bool=True)->function:
    '''

    :param flag: True->enable dry run mode, False -> disable dry run mode
    :return:
    '''
    def decorate(func):
        def wrapper(*args):
            if flag:
                cfg = ConfigParser()
                config_file = '../yys_configurations/config.ini'
                cfg.read(config_file, encoding='utf-8')
                try:
                    for arg in args:
                        cfg.get('pixel_info',arg)
                except NoOptionError:
                    print('error')
            else:
                func(*args)
        return wrapper
    return decorate


def team_page(pos='team_pic_pos',click_pos='c_team_start_pos')->bool:
    '''

    :param pos:
    :return:
    '''
    '''
    判定是否是组队界面，如果是，则点击开始按钮
    :return:
    '''
    while True:
        if compare_rgb(pos):
            click_mouse(click_pos)
            return True

def battle_ready(pos='simhun_ready_pos',click_pos='c_simhun_ready_pos')->bool:
    '''
    判定是否为战斗准备阶段，如果是，则点击准备鼓面按钮
    :return: 
    '''
    while True:
        if compare_rgb(pos):
            click_mouse(click_pos)
            return True

def battle_during(pos:str)->bool:
    '''
    判定当前是否处于战斗阶段
    :return:
    '''
    while True:
        if not compare_rgb(pos):
            return True

def battle_end(pos='p_background_pic_pos',click_pos='c_open_box_pos')->bool:
    '''
    判定当前战斗是否结束,鬼火状态消失，则一直点击，准备开箱，直到找到结束背景色或者组队界面，则停止
    :param fire_pos:
    :return:
    '''
    while True:
        if not compare_rgb(pos):
            click_mouse(click_pos)
        else:
            return True

def select_position(click_pos:str):
    '''

    :param sprite_pos: 式神位置
    :return:
    '''
    click_mouse(click_pos,random_num=2)


def reward_page(click_pos:str):
    '''
    悬赏封印情况
    :param action: 是否接受悬赏封印
    :return:
    '''
    if compare_rgb('p_reward_detect_pos'):
        click_mouse(click_pos)
