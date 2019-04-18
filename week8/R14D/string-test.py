#import strings
from strings import get_first_lowercase_pair as f

# input: 1
# output: -1

assert f('AAaaAA') == 2
assert f("") == -1
assert f(1) == -1
assert f('xyz') == 0
assert f('zzz') == 0
assert f('AAA') == -1
assert f('AhAjAjAjA') == -1
assert f(None) == -1

# if f(1) != -1:
#    raise AssertionError()
# else:
#    pass
