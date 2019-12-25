from win32_func import compare_rgb, click_mouse
from configparser import ConfigParser,NoOptionError
# from yys_functions.decorater import dry_run
from project_settings import yys_config_path
import time
import sys

# running状态存储pixel info
pixel_info = {}

cfg = ConfigParser()
config_file = yys_config_path
cfg.read(config_file, encoding='utf-8')
dry_run_flag = int(cfg.get('dry_run', 'flag'))
sleep_time = float(cfg.get('time','sleep_time'))

for i in cfg.items('pixel_info'):
    pixel_info[i[0]] = i[1]


def dry_run(flag=dry_run_flag):
    '''
    dry run decorator，用来检测所用到的pos是否采集
    :param flag: True->enable dry run mode, False -> disable dry run mode
    :return:
    '''
    def decorate(func):
        def wrapper(**kwargs):
            if flag:
                for key,value in kwargs.items():
                    try:
                        res = cfg.get('pos_name',value)
                        # 异常触发检测
                        pixel_info[res]
                    except (NoOptionError,KeyError):
                        error_pos = '{}'.format(res)
                        return 1, error_pos
                return 0,'配置正确'
            else:
                func(**kwargs)
        return wrapper
    return decorate

def judge_rgb_reward_ui(reward_pos,click_reward_pos)->bool:
    '''
    是否为悬赏封印
    :param pos:
    :param click_pos:
    :return:
    '''
    print('检测是否有悬赏')
    if compare_rgb(reward_pos):
        click_mouse(click_reward_pos)
        return True
    return True

@dry_run(flag=dry_run_flag)
def judge_rgb_team_ui(pos,reward_pos,click_reward_pos)->bool:
    '''
    if in team page, return loop
    :param pos:  判断界面
    :return:
    '''

    while True:
        time.sleep(sleep_time)
        judge_rgb_reward_ui(reward_pos,click_reward_pos)
        if compare_rgb(pos):
            print('当前为组队界面')
            return True

@dry_run(flag=dry_run_flag)
def click_btn_team_start(pos,click_pos,reward_pos,click_reward_pos)->bool:
    '''
    click team start butten if it is active
    :param pos: 挑战按钮是否可点击
    :param click_pos:挑战按钮
    :return:
    '''
    while True:
        time.sleep(sleep_time)
        judge_rgb_reward_ui(reward_pos,click_reward_pos)
        if compare_rgb(pos):
            click_mouse(click_pos)
            print('当前挑战按钮可用')
            return True

@dry_run(flag=dry_run_flag)
def judge_rgb_battle_pre_ui(pos,reward_pos,click_reward_pos)->bool:
    '''
    if in battle page ,return loop
    :param pos: 战斗准备状态
    :return:
    '''
    while True:
        time.sleep(sleep_time)
        judge_rgb_reward_ui(reward_pos,click_reward_pos)
        if compare_rgb(pos):
            print('当前为战斗准备状态')
            return True

@dry_run(flag=dry_run_flag)
def judge_rgb_btn_battle_start(pos,click_pos,reward_pos,click_reward_pos)->bool:
    '''
    click battle start button if it is active（when set "manual start" in setting page）
    :param pos:
    :return:
    '''
    while True:
        time.sleep(sleep_time)
        judge_rgb_reward_ui(reward_pos,click_reward_pos)
        if compare_rgb(pos):
            click_mouse(click_pos)
            print('当前开始按钮可以点击')
            return True

@dry_run(flag=dry_run_flag)
def judge_rgb_battle_during_ui(pos,reward_pos,click_reward_pos)->bool:
    '''
    if in battle ,return loop
    :param pos:
    :return:
    '''
    while True:
        time.sleep(sleep_time)
        judge_rgb_reward_ui(reward_pos,click_reward_pos)
        if compare_rgb(pos):
            print('当前为战斗中。。。。')
            return True

@dry_run(flag=dry_run_flag)
def click_btn_ShiSheng(click_pos,reward_pos,click_reward_pos)->bool:
    '''
    click ShiSheng position. (if specify "ShiSheng position" in setting page)
    :param click_pos:
    :return:
    '''
    judge_rgb_reward_ui(reward_pos,click_reward_pos)
    time.sleep(sleep_time)
    click_mouse(click_pos)
    return True


@dry_run(flag=dry_run_flag)
def judge_rgb_battle_ending_ui(pos,reward_pos,click_reward_pos)->bool:
    '''
    click area avoild items, before detect specify background
    :param pos:
    :return:
    '''
    while True:
        time.sleep(sleep_time)
        judge_rgb_reward_ui(reward_pos,click_reward_pos)
        if not compare_rgb(pos):
            print('当前为战斗结束状态')
            return True

@dry_run(flag=dry_run_flag)
def click_area_battle_ending(pos,click_pos,reward_pos,click_reward_pos)->bool:
    '''
    stop click if detect any rgb in background picture or invite ui
    :param pos:
    :param click_pos:
    :return:
    '''
    while True:
        time.sleep(sleep_time)
        judge_rgb_reward_ui(reward_pos,click_reward_pos)
        if not compare_rgb(pos):
            click_mouse(click_pos)
            print('当前进行战斗后开箱')
        else:
            return True
