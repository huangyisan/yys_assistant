from configparser import ConfigParser,NoOptionError
from yys_functions.game_func import pixel_info

def dry_run(flag:bool=True):
    '''
    干跑装饰器，用来检测所用到的pos是否采集
    :param flag: True->enable dry run mode, False -> disable dry run mode
    :return:
    '''
    def decorate(func):
        def wrapper(*args):
            if flag:
                cfg = ConfigParser()
                config_file = '../yys_configurations/config.ini'
                cfg.read(config_file, encoding='utf-8')
                try:
                    for arg in args:
                        res = cfg.get('pos_name',arg)
                        # 异常触发检测
                        pixel_info[res]
                except (NoOptionError,KeyError):
                    print('error')
            else:
                func(*args)
        return wrapper
    return decorate