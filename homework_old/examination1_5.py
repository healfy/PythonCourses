def task_1(array, count_letters=False):
    return tuple(
        [name.title() + ' ' + surname.title() + (' (' + str(len(name) + len(surname)) + ')' if count_letters else '') for
         surname, name, in array.items() if len(name) >= 4 and len(surname) >= 4])


task_3 = lambda n: n % 3 == 0 and n % 2 == 1 if isinstance(n, int) and not isinstance(n, bool) else n[::-1]


def task_4(func):
    def new_func(*args, **kwargs):
        if func.__name__.startswith('__'):
            return None
        else:
            return func(*args, **kwargs)

    return new_func
