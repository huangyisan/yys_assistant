from yys_functions import game_func
import time

def action_delay(sleep=1):
    time.sleep(sleep)

def soul(focus: int = 1, exec_count: int = 1, team_leader: bool = True, auto: bool = True, reward: bool = True, dry_run=True):
    '''
    类魂十执行行为，从组队界面开始到开箱后过场背景图片，为一个结算过程
    :param focus: 式神位置
    :param exec_count: 执行次数
    :param team_leader: 是否为队长
    :param auto: 是否开启自动
    :param reward: 悬赏封印是否接受
    :param dry_run: dry run mode
    :return:
    '''

    if dry_run:
        t_exec_count = 1
    else:
        t_exec_count = exec_count if exec_count else True

        res_judge_rgb_team_ui = res_click_btn_team_start = res_judge_rgb_battle_pre_ui = res_judge_rgb_btn_battle_start = res_judge_rgb_battle_during_ui = res_judge_rgb_battle_ending_ui = res_click_area_battle_ending = (
            None, None)

    while t_exec_count:
        # 如果是队长情况下
        if team_leader:
            # 未开启自动情况
            if not auto:
                res_judge_rgb_team_ui = game_func.judge_rgb_team_ui(pos='j_rgb_team_ui_pos')
                res_click_btn_team_start = game_func.click_btn_team_start(pos='j_btn_team_start_pos', click_pos='c_btn_team_start_pos')
                res_judge_rgb_battle_pre_ui = game_func.judge_rgb_battle_pre_ui(pos='j_rgb_battle_pre_ui_pos')
                res_judge_rgb_btn_battle_start = game_func.judge_rgb_btn_battle_start(pos='j_rgb_btn_battle_start_pos',click_pos='c_btn_battle_start_pos')
                res_judge_rgb_battle_during_ui = game_func.judge_rgb_battle_during_ui(pos='j_rgb_battle_during_ui_pos')
                # 设定式神点选情况
                if focus:
                    focus_dict = {1: 'c_btn_shisheng_first_position_pos',
                                  2: 'c_btn_shisheng_second_position_pos',
                                  3: 'c_btn_shisheng_third_position_pos',
                                  4: 'c_btn_shisheng_fourth_position_pos',
                                  5: 'c_btn_shisheng_fifth_position_pos',
                                  }
                    action_delay()
                    res_click_btn_ShiSheng = game_func.click_btn_ShiSheng(pos=focus_dict.get(focus))
                res_judge_rgb_battle_ending_ui = game_func.judge_rgb_battle_ending_ui(pos='j_rgb_battle_during_ui_pos')
                res_click_area_battle_ending = game_func.click_area_battle_ending(pos='j_rgb_background_ui_pos',click_pos='c_btn_battle_ending_area_pos')


            # 开启自动情况，只进行式神点选
            else:
                res_judge_rgb_team_ui = game_func.judge_rgb_team_ui(pos='j_rgb_team_ui_pos')
                res_judge_rgb_battle_pre_ui = game_func.judge_rgb_battle_pre_ui(pos='j_rgb_battle_pre_ui_pos')
                res_judge_rgb_battle_during_ui = game_func.judge_rgb_battle_during_ui(
                    pos='j_rgb_battle_during_ui_pos')
                if focus:
                    action_delay()
                    focus_dict = {1: 'c_btn_shisheng_first_position_pos',
                                  2: 'c_btn_shisheng_second_position_pos',
                                  3: 'c_btn_shisheng_third_position_pos',
                                  4: 'c_btn_shisheng_fourth_position_pos',
                                  5: 'c_btn_shisheng_fifth_position_pos',
                                  }
                    res_click_btn_ShiSheng = game_func.click_btn_ShiSheng(pos=focus_dict.get(focus))
                res_judge_rgb_battle_ending_ui = game_func.judge_rgb_battle_ending_ui(pos='j_rgb_battle_during_ui_pos')

        # 非队长情况,无需考虑组队界面
        else:
            # 非自动情况
            if not auto:
                res_judge_rgb_battle_pre_ui = game_func.judge_rgb_battle_pre_ui(pos='j_rgb_battle_pre_ui_pos')
                res_judge_rgb_btn_battle_start = game_func.judge_rgb_btn_battle_start(pos='j_rgb_btn_battle_start_pos',click_pos='c_btn_battle_start_pos')
                res_judge_rgb_battle_during_ui = game_func.judge_rgb_battle_during_ui(pos='j_rgb_battle_during_ui_pos')
                # 设定式神点选情况
                if focus:
                    focus_dict = {1: 'c_btn_shisheng_first_position_pos',
                                  2: 'c_btn_shisheng_second_position_pos',
                                  3: 'c_btn_shisheng_third_position_pos',
                                  4: 'c_btn_shisheng_fourth_position_pos',
                                  5: 'c_btn_shisheng_fifth_position_pos',
                                  }
                    action_delay()
                    res_click_btn_ShiSheng = game_func.click_btn_ShiSheng(pos=focus_dict.get(focus))
                res_judge_rgb_battle_ending_ui = game_func.judge_rgb_battle_ending_ui(pos='j_rgb_battle_during_ui_pos')
                res_click_area_battle_ending = game_func.click_area_battle_ending(pos='j_rgb_background_ui_pos',click_pos='c_btn_battle_ending_area_pos')

            # 自动情况
            else:
                res_judge_rgb_team_ui = game_func.judge_rgb_team_ui(pos='j_rgb_team_ui_pos')
                res_judge_rgb_battle_pre_ui = game_func.judge_rgb_battle_pre_ui(pos='j_rgb_battle_pre_ui_pos')
                res_judge_rgb_battle_during_ui = game_func.judge_rgb_battle_during_ui(
                    pos='j_rgb_battle_during_ui_pos')
                if focus:
                    action_delay()
                    focus_dict = {1: 'c_btn_shisheng_first_position_pos',
                                  2: 'c_btn_shisheng_second_position_pos',
                                  3: 'c_btn_shisheng_third_position_pos',
                                  4: 'c_btn_shisheng_fourth_position_pos',
                                  5: 'c_btn_shisheng_fifth_position_pos',
                                  }
                    res_click_btn_ShiSheng = game_func.click_btn_ShiSheng(pos=focus_dict.get(focus))
                res_judge_rgb_battle_ending_ui = game_func.judge_rgb_battle_ending_ui(pos='j_rgb_battle_during_ui_pos')

        if dry_run:
            if team_leader:
                if not auto:
                    if focus:
                        res_list = [
                            res_judge_rgb_team_ui,
                            res_click_btn_team_start,
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_btn_battle_start,
                            res_judge_rgb_battle_during_ui,
                            res_click_btn_ShiSheng,
                            res_judge_rgb_battle_ending_ui,
                            res_click_area_battle_ending,
                        ]
                    else:
                        res_list = [
                            res_judge_rgb_team_ui,
                            res_click_btn_team_start,
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_btn_battle_start,
                            res_judge_rgb_battle_during_ui,
                            res_judge_rgb_battle_ending_ui,
                            res_click_area_battle_ending,
                        ]
                else:
                    if focus:
                        res_list = [
                            res_judge_rgb_team_ui,
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_battle_during_ui,
                            res_click_btn_ShiSheng,
                            res_judge_rgb_battle_ending_ui,
                        ]
                    else:
                        res_list = [
                            res_judge_rgb_team_ui,
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_battle_during_ui,
                            res_judge_rgb_battle_ending_ui,
                        ]
            else:
                if not auto:
                    if focus:
                        res_list = [
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_btn_battle_start,
                            res_judge_rgb_battle_during_ui,
                            res_click_btn_ShiSheng,
                            res_judge_rgb_battle_ending_ui,
                            res_click_area_battle_ending,
                        ]
                    else:
                        res_list = [
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_btn_battle_start,
                            res_judge_rgb_battle_during_ui,
                            res_judge_rgb_battle_ending_ui,
                            res_click_area_battle_ending,
                        ]
                else:
                    if focus:
                        res_list = [
                            res_judge_rgb_team_ui,
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_battle_during_ui,
                            res_click_btn_ShiSheng,
                            res_judge_rgb_battle_ending_ui,
                        ]
                    else:
                        res_list = [
                            res_judge_rgb_team_ui,
                            res_judge_rgb_battle_pre_ui,
                            res_judge_rgb_battle_during_ui,
                            res_judge_rgb_battle_ending_ui,
                        ]

            # [(0, '配置正确'), (0, '配置正确'), (0, '配置正确'), (1, '点_战斗中界面_式神第一_位置 缺失该坐标配置'), (0, '配置正确')]

            res_list = list(filter(lambda i: i[0] == 1, res_list))
            if res_list:
                error = '以下坐标存在缺失：\n'
                error_info = '{}\n'
                for i in res_list:
                    error += error_info.format(i[1])
                # print([i[1] for i in res_list])
                # error_info = str([i[1] for i in res_list])
                return 1, error
            else:
                return 0, '配置正常'
        t_exec_count -= 1
