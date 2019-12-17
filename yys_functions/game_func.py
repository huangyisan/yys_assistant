from .win32_func import compare_rgb, click_mouse

def team_page()->bool:
    '''
    判定是否是组队界面，如果是，则点击开始按钮
    :return:
    '''
    while True:
        if compare_rgb('team_pic_pos'):
            click_mouse('team_start_pos')
            return True

def battle_ready()->bool:
    '''
    判定是否为战斗准备阶段，如果是，则点击准备鼓面按钮
    :return: 
    '''
    while True:
        if compare_rgb('simhun_ready_pos'):
            click_mouse('c_simhun_ready_pos')
            return True

def battle_during(fire_pos:str)->bool:
    '''
    判定当前是否处于战斗阶段
    :return:
    '''
    while True:
        if not compare_rgb(fire_pos):
            return True

def battle_end()->bool:
    '''
    判定当前战斗是否结束,鬼火状态消失，则一直点击，准备开箱，直到找到结束背景色或者组队界面，则停止
    :param fire_pos:
    :return:
    '''
    while True:
        if not compare_rgb('p_background_pic_pos'):
            click_mouse('c_open_box_pos')
        else:
            return True

def select_position(sprite_pos:str):
    '''

    :param sprite_pos: 式神位置
    :return:
    '''
    click_mouse(sprite_pos,random_num=2)


def reward_page(action:str):
    '''
    悬赏封印情况
    :param action: 是否接受悬赏封印
    :return:
    '''
    if compare_rgb('p_reward_detect_pos'):
        click_mouse(action)



