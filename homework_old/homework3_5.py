import time
from decimal import Decimal
task_2_a = lambda element: element % 2 == 0 and 1 < element < 100 and element % 10 != 0
task_2_b = lambda elem: elem // 2 if elem % 2 == 0 else elem * 2
task_2_c = lambda result, a: result + len([a for a in a if a.islower()])
task_2_d = lambda i: sum([i for i in i if i >= 0]) / len([i for i in i if i >= 0])


def task_3(is_slow=False):
    a, b = 0, 1
    while a < 1000000000:
        if is_slow:
            time.sleep(0.5)
        yield a
        a, b = b, a+b


def task_4(func):
    def new_func(*args, **kwargs):
        new_args = [arg for arg in args]
        arguments = []
        kwargs_keys = [key for key in kwargs]
        kwargs_values = []
        for i in new_args:
            if isinstance(i, (int, float, Decimal)) and not isinstance(i, bool):
                a = -i
                arguments.append(a)
            elif isinstance(i, (str, list)):
                a = i[::-1]
                arguments.append(a)
            elif isinstance(i, dict):
                a = {key[::-1]: value for key, value in i.items()}
                arguments.append(a)
            elif isinstance(i, bool):
                if i is True:
                    arguments.append(False)
                else:
                    arguments.append(True)
        for value in kwargs.values():
            if isinstance(value, (int, float, Decimal)) and not isinstance(value, bool):
                b = -value
                kwargs_values.append(b)
            elif isinstance(value, (str, list)):
                b = value[::-1]
                kwargs_values.append(b)
            elif isinstance(value, dict):
                b = {key[::-1]: value for key, value in value.items()}
                kwargs_values.append(b)
            elif isinstance(value, bool):
                if value is True:
                    kwargs_values.append(False)
                else:
                    kwargs_values.append(True)
        kwargs_dict = dict(zip(kwargs_keys, kwargs_values))
        dict3 = dict(sorted([(key, value) for (key, value) in kwargs_dict.items()])[:5])
        return func(*arguments[:5], **dict3)
    return new_func



