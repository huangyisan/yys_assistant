# 像素点combbox内容
'''
s = 单人模式
m = 多人(两人)组队模式
s/m_场景_标记性图
example: s_魂土_鬼火
'''
default_combobox_pixel_pos = ['s_魂土_鬼火','s_魂十_鬼火','g_魂土_时钟','1','3','2','开始按钮','准备按钮']
# 追加像素点combbox内容
add_combobox_pixel_pos = ['c',]
default_combobox_pixel_pos.extend(add_combobox_pixel_pos)
default_combobox_pixel_pos.sort()

# 采点内容，kv方式
pixel_pos_dict = {}
