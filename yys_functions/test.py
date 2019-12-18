
from yys_functions.decorater import dry_run

flag = True
@dry_run(flag)
def test_func(a):
    print(a)