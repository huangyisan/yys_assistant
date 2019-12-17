from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('../yys_configurations/config.ini',encoding='utf-8')
pos_name_list = [k for k,v in cfg.items('pos_name')]
for k,v in pos_name_list.