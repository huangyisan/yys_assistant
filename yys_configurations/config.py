from .relations import pos_name
# 像素点combbox内容
'''
s = 单人模式
m = 多人(两人)组队模式
s/m_场景_标记性图
example: s_魂土_鬼火
'''

default_combobox_pixel_pos = [i for i in pos_name]
# 追加像素点combbox内容, 此功能待开发
add_combobox_pixel_pos = ['']
default_combobox_pixel_pos.extend(add_combobox_pixel_pos)
default_combobox_pixel_pos.sort()

# 采点内容，kv方式
pixel_info_dict = {}
pixel_rgb_dict = {}

