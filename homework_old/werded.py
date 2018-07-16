# x={1,2,3,4,5,5} # тип данных - сет
# y={8,9}
# print(x|y) # сложение сетов
# rint(x-y) # вычитание сетов, удаляются одинаковые имена
# x.add(6)
# x.remove(6)
# x.clear()
# x.update() # в текущий сет добавляет новые элементы
# r = ['a','b''c','a']
# print(set(r)) # преобразовываем

# def task(a,b):
#     result = a/b
#     return result
# print(task(5, 0))

# def task(a,b):
# try:   # защита от падения программы
# result = a/b
#  return result
# except ZeroDivisionError: # можно добалять еще исключения различных типов
#    return "Деление на ноль запрещено"
# except Exception as error: # ловим глобальную ошибку и выводим ее в переменную error
#  print(error)
#  result = 0
# finally:# однозначно исполняемый код,т.е независимо от того будут ошибки или нет
#   result += 1
# return result
# print(task(5, 0))


#def task_1(t, y):
 #   assert isinstance(y, int)  # ломаем программу локально
#    return t / y


#print(task_1(5, 'hello'))
# x=[1,2,3,4,5,-1,-2,-3]
# result = [element for element in x if element >= 0] - генератор списков
# print(result)
# y = [['a', 1],['b', 2], ['c',3],['dd', 1]]
# result = {key + ' )': value for key,value in y if len(key) == 1}
# print(result)
#round reversed sorted
#print(round(5.234234234, 2))# округление
#x = list(reversed([1,2,3]))
# x = sorted(([3,2,1]))
# print(x)
# x = [1,2,3]
# for i in reversed(x):
#     print(i)
#all, any - функции позволяющие работать с большим числом булевых переменных
# all это тоже самое что поставить между всеми переменными and
# any работает также, только or
# ord  - узнать код символа
# chr  наоборот, по коду выдает символ
# isinstance( 5, int) булевая проверка типа символа
#type тоже проверка, но не особо используемая и просто для получения названия типа символа
# атрибуты dir, getattr, setattr
# enumerate - пронумеровывает каждый элемент массива
# journal = {}
# students = ['a','b''c','d']
# for number, name in enumerate(sorted(students)):
#     journal[number] = name
# import, модули
# import random
# print(random.random() * 9 + 1)
#print(random.randint(1, 4))
# print(bool(random.randint(0, 1)))
# from module_1 import inc as inc.function, x as number
# print(inc.function, number) импорт готового модуля из другого файла
# from decimal import Decimal
# x = Decimal('4.99999999999999999')
# print(x)
# import datetime
# today = datetime.datetime.now()
# yesterday = today - datetime.timedelta(days = 1)
# print(yesterday)
# print((today - yesterday).total_seconds())
# print(today > yesterday)
# from collections import  defaultdict
# x = defaultdict(list)
# x['a'].append(1)
# print((dict(x)))
# from  collections import  namedtuple
# AmazingTuple = namedtuple('AmazingTuple', ['name', 'surname', 'mark'])
# data = [['Vasy', 'Ivanov',4],['Ivan', 'Petrov', 10]]
# students = []
# for n,s,m in data:
#     student = AmazingTuple(n, s, m)
#     students.append(student)
# print(students[0].mark) #струкрутрирование
# import copy
# x  = [1,2,3,[4,5,[6,7]]]
# y = copy.copy(x[-1])
# y[-1].pop()
# print(x)
# print(y)
#copy копирует текущий уровень
# deepcopy все уровни

