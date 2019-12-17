# 采点名称对应关系
pos_name = {
    # 单人类似魂十界面，右边五个式神加一个阴阳师，鬼火位置
    '单人_类魂十_鬼火_位置':'Single_SimHun_Fire_Pos',
    # 多人类似魂十界面，右边两个式神加一个阴阳师，鬼火位置
    '多人_类魂十_鬼火_位置':'Multi_SimHun_Fire_Pos',
    # 类魂十，时钟位置
    '类魂十_时钟_位置':'SimHun_Clock_Pos',
    # 类魂十，准备鼓位置
    '类魂十_准备_位置':'SimHun_Ready_Pos',


    # 战斗式神位置
    # 横向排列式神位置
    '横向_第一位置':'Line_First_Pos',
    '横向_第二位置':'Line_Second_Pos',
    '横向_第三位置':'Line_Third_Pos',
    '横向_第四位置':'Line_Fourth_Pos',
    '横向_第五位置':'Line_Fifth_Pos',

    # 弧形排列式神位置
    '弧形_第一位置':'Arc_First_Pos',
    '弧形_第二位置':'Arc_Second_Pos',
    '弧形_第三位置':'Arc_Third_Pos',
    '弧形_第四位置':'Arc_Fourth_Pos',
    '弧形_第五位置':'Arc_Fifth_Pos',


    # 意外情况
    '悬赏封印标示位置':'Reward_Detect_Pos',
    '悬赏封印接受位置':'Reward_Accept_Pos',
    '悬赏封印拒绝位置':'Reward_Reject_Pos',

}

# 追加像素点combbox内容, 此功能待开发
add_combobox_pixel_pos = []

def get_pos_name():
    '''
    像素点combbox内容
    :return:
    '''

    default_combobox_pixel_pos = [i for i in pos_name]

    default_combobox_pixel_pos.extend(add_combobox_pixel_pos)
    return sorted(default_combobox_pixel_pos)