from yys_functions.win32_func import compare_rgb, click_mouse
from configparser import ConfigParser,NoOptionError
# from yys_functions.decorater import dry_run
from project_settings import yys_config_path
import time



# running状态存储pixel info
pixel_info = {}

cfg = ConfigParser()
config_file = yys_config_path
cfg.read(config_file, encoding='utf-8')
flag = int(cfg.get('dry_run', 'flag'))

def dry_run(flag=int(cfg.get('dry_run', 'flag'))):
    '''
    干跑装饰器，用来检测所用到的pos是否采集
    :param flag: True->enable dry run mode, False -> disable dry run mode
    :return:
    '''
    def decorate(func):
        def wrapper(**kwargs):
            print('dry_flag is ',flag)
            if flag:
                for key,value in kwargs.items():
                    try:
                        res = cfg.get('pos_name',value)
                        # 异常触发检测
                        pixel_info[res]
                    except (NoOptionError,KeyError):
                        error_info = '{} 缺失该坐标配置'.format(res)
                        return (1, error_info)
                return (0,'配置正确')
            else:
                func(**kwargs)
        return wrapper
    return decorate


# control dry run mode


@dry_run(flag=int(cfg.get('dry_run', 'flag')))
def team_page(pos,click_pos)->bool:
    '''
    判定是否是组队界面，如果是，则点击开始按钮
    :param pos:  判断界面
    :param click_pos: 开始按钮
    :return:
    '''

    while True:
        time.sleep(1)
        print('team_page stage')
        if compare_rgb(pos):
            click_mouse(click_pos)
            return True

@dry_run(flag=int(cfg.get('dry_run', 'flag')))
def battle_ready(pos,click_pos)->bool:
    '''
    判定是否为战斗准备阶段，如果是，则点击准备鼓面按钮。一般用不到，因为可以锁定队伍
    :return: 
    '''
    while True:
        time.sleep(1)
        print('battle_ready stage')
        if compare_rgb(pos):
            click_mouse(click_pos)
            return True

@dry_run(flag=int(cfg.get('dry_run', 'flag')))
def battle_during(pos):
    '''
    判定当前是否处于战斗阶段
    :return:
    '''
    while True:
        time.sleep(1)
        print('battle_during stage')
        if not compare_rgb(pos):
            return True

@dry_run(flag)
def battle_end(pos,click_pos):
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

@dry_run(flag)
def select_position(click_pos):
    '''

    :param click_pos: 式神位置
    :return:
    '''
    click_mouse(click_pos,random_num=2)

@dry_run(flag)
def reward_page(pos,click_pos):
    '''
    悬赏封印情况
    :param pos:  悬赏封印pos
    :param click_pos:  是否接受
    :return:
    '''

    if compare_rgb(pos):
        click_mouse(click_pos)
