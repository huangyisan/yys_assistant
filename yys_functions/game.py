from yys_functions import game_func


def soul(focus: int = 1, exec_count: int = 1, team_leader: bool = True, reward: bool = True, dry_run=True):
    '''
    类魂十执行行为，从组队界面开始到开箱后过场背景图片，为一个结算过程
    :param focus: 式神位置
    :param exec_count: 执行次数
    :param team_leader: 是否为队长
    :param reward: 悬赏封印是否接受
    :param dry_run: dry run mode
    :return:
    '''
    print(focus)

    if dry_run:
        t_exec_count = 1
    else:
        t_exec_count = exec_count if exec_count else True

        res_judge_rgb_team_ui = res_click_btn_team_start = res_judge_rgb_battle_pre_ui = res_judge_rgb_btn_battle_start = res_judge_rgb_battle_during_ui = res_judge_rgb_battle_ending_ui = res_click_area_battle_ending = (
            None, None)

    while t_exec_count:
        if team_leader:
            res_judge_rgb_team_ui = game_func.judge_rgb_team_ui(pos='j_rgb_team_ui_pos')
            res_click_btn_team_start = game_func.click_btn_team_start(pos='j_btn_team_start_pos', click_pos='c_btn_team_start_pos')
            res_judge_rgb_battle_pre_ui = game_func.judge_rgb_battle_pre_ui(pos='j_rgb_battle_pre_ui_pos')
            res_judge_rgb_btn_battle_start = game_func.judge_rgb_btn_battle_start(pos='j_rgb_btn_battle_start_pos',click_pos='c_btn_battle_start_pos')
            res_judge_rgb_battle_during_ui = game_func.judge_rgb_battle_during_ui(pos='j_rgb_battle_during_ui_pos')
            if focus:

                focus_dict = {1: 'c_btn_shisheng_first_position_pos',
                              2: 'c_btn_shisheng_second_position_pos',
                              3: 'c_btn_shisheng_third_position_pos',
                              4: 'c_btn_shisheng_fourth_position_pos',
                              5: 'c_btn_shisheng_fifth_position_pos',
                              }

                res_click_btn_ShiSheng = game_func.click_btn_ShiSheng(pos=focus_dict.get(focus))

            res_judge_rgb_battle_ending_ui = game_func.judge_rgb_battle_ending_ui(pos='j_rgb_battle_during_ui_pos')
            res_click_area_battle_ending = game_func.click_area_battle_ending(pos='j_rgb_background_ui_pos',click_pos='c_btn_battle_ending_area_pos')
            print('完结')

        else:
            res_battle_during = game_func.judge_rgb_team_ui(pos='p_multi_simhun_fire_pos')
            res_battle_end = game_func.click_btn_team_start(pos='p_background_pic_pos', click_pos='c_open_box_pos')
        if dry_run:
            if focus:
                res_list = [res_judge_rgb_team_ui, res_click_btn_team_start, res_judge_rgb_battle_pre_ui, res_judge_rgb_btn_battle_start, res_judge_rgb_battle_during_ui, res_judge_rgb_battle_ending_ui,res_click_area_battle_ending, res_click_btn_ShiSheng]
            else:
                res_list = [res_judge_rgb_team_ui, res_click_btn_team_start, res_judge_rgb_battle_pre_ui, res_judge_rgb_btn_battle_start, res_judge_rgb_battle_during_ui, res_judge_rgb_battle_ending_ui,res_click_area_battle_ending]

            res_list = list(filter(lambda i: i[0] == 1, res_list))
            # error_info = [ i[0]==0 for i in res_list ]
            if res_list:
                error_info = str([i[1] for i in res_list])
                return (1, error_info)
            else:
                return (0, '配置正常')
        t_exec_count -= 1
