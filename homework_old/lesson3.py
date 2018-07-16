# def my_function(a, b, c=5, *args, **kwargs):
#     return a,b,c, args, kwargs
#
#
# print(my_function(1,2,3, name = 'Anton', age = 22))

    # """
    #
    # :param number: int
    # :param boolean: bool
    # :type number: int
    # :type boolean: bool
    # :rtype: int
    # """
#     return number + 1
# parametr_1 = 100
# parametr_2 = True
# a, b = my_function([1,2,3], {})
#
# def func():
#     return 1
# if __name__ == '__name__':
#     print('JFLKJHSDF')
#     x= 100
#
# from time import sleep
# sleep(10)
# print(list(zip([1,2,3], [3,4,5],[1,2,3])))
# def global_function():
#     def local_function(number):
#         print('local')
#         return number + 1
#     print('global')
#     return local_function
#
# func = global_function()
# print(func(1))
# my_func = lambda elelment:elelment % 2 ==1
# print(list((filter(my_func,[1,2,3,4,5]))))
# from functools import reduce
#
# array = [1,2,3,4,5]

# print(list(map(lambda number: number + 1, array)))

# print(reduce(lambda result, new_element: result + new_element, array))


# def generator():
#     result = 1
#     x = 1
#     yield result
#     while x <10 :
#         x += 1
#         result *= x
#         yield result
#
#
# for elem in generator():
#     print(elem)
# def func(group, student, mark):
#     return group + '(' + student + '):' + str(mark)
#
# def group_f_gen( group):
#     def new_func(student, mark):
#         return func(group, student, mark)
#     return new_func
#
# group_func = group_f_gen('23123123')
#
#
# print(group_func('Ivan Ivanov' , 9.5))
# def decorator(func):
#     def new_func(a, b):
#         print('a = ' + str(a) + ' b = ' + str(b))
#         return -func(a, b)
#     return new_func
#
# @decorator
# def add(a, b):
#     return a+b
# def test(a,b,c):
#     pass
# x = [1,2,3]
# test(*x)# в функциию пойдут аргументы а = 1 и т.д
# x = {'a' : 1,'b' :2, 'c' :3}
# test(**x) #
#
#
# print(add(1, 2))
def bool_killer(func):
    def new_func(*args, **kwargs):
        for arg in args:
            if isinstance(arg, bool):
                return( 'func' + func.__name__ + 'upala iz za args')
        for kwarg in kwargs.values():
            if isinstance(kwarg, bool):
                return('func' + func.__name__ + 'upala iz za kwargs')
        return func(*args, **kwargs)
    return new_func

@bool_killer
def add(a,b):
    return a+b

@bool_killer
def minus(a, b, c):
    return a - b - c

@bool_killer
def dict_gen(**kwargs):
    return kwargs

print(add(1, True))
print(minus(1, 2, 3))
print(dict_gen(a = 1, b = 3, c = False))

dict3 = dict(sorted([(key,value) for (key, value) in dict2.items()])[:5])