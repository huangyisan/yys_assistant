from win32_func import compare_rgb,click_mouse
from configparser import ConfigParser,NoOptionError
from game_func import dry_run

# cfg = ConfigParser()
# config_file = '../yys_configurations/config.ini'
# cfg.read(config_file, encoding='utf-8')
# try:
#     res = cfg.get('pixel_info','123')
#     print(res)
# except NoOptionError as e:
#     print(e)

@dry_run(flag=False)
def test_func(a,b):
    print(a)
    print(b)

test_func(str(1),str(2))