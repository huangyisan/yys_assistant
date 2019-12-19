from yys_functions import game_func


def soul(focus:int=1, exec_count:int=1, team_leader:bool = True, reward:bool = True, dry_run=True):
    '''
    类魂十执行行为，从组队界面开始到开箱后过场背景图片，为一个结算过程
    :param focus: 式神位置
    :param exec_count: 执行次数
    :param team_leader: 是否为队长
    :param reward: 悬赏封印是否接受
    :param dry_run: dry run mode
    :return:
    '''

    if dry_run:
        print(1111111111111111)
        t_exec_count = 1
    else:
        t_exec_count = exec_count if exec_count else True

    res_team_page = res_battle_during = res_battle_end = (None,None)

    while t_exec_count:
        if team_leader:
            res_team_page = game_func.team_page(pos='p_team_pic_pos',click_pos='c_team_start_pos')
            res_battle_during = game_func.battle_during(pos='p_multi_simhun_fire_pos')
            res_battle_end = game_func.battle_end(pos='p_background_pic_pos',click_pos='c_open_box_pos')


        else:
            res_battle_during = game_func.battle_during(pos='p_multi_simhun_fire_pos')
            res_battle_end = game_func.battle_end(pos='p_background_pic_pos',click_pos='c_open_box_pos')
        if dry_run:
            res_list = [res_team_page,res_battle_during,res_battle_end]
            res_list = list(filter(lambda i: i[0]==1, res_list))
            # error_info = [ i[0]==0 for i in res_list ]
            if res_list:
                error_info = str([i[1] for i in res_list])

                return (1,error_info)
            else:
                return (0,'配置正常')
        t_exec_count -=1





