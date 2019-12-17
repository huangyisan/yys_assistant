from .game_func import team_page


def soul(focus:int, exec_count:int, team_leader:bool = True, auto:bool = True, open_box:bool = True, reward:bool = True):
    '''
    类魂十执行行为，从组队界面开始到开箱后过场背景图片，为一个结算过程
    :param focus: 式神位置
    :param exec_count: 执行次数
    :param team_leader: 是否为队长
    :param auto: 是否开启自动
    :param open_box: 是否战后开箱
    :param reward: 悬赏封印是否接受
    :return:
    '''
    
    t_exec_count = exec_count if exec_count else True

    while t_exec_count:
        team_page()



        exec_count -=1





