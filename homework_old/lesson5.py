# x = 1
# y = 3
# s = x + y
# print('{x} + {y} = {s}'.format(x=y, y=x, s=s))

# array = [1, 2, 3, 4, 5]
# result = ', '.join(map(str, array))
# print(result)
# # метод replace(что меняем, на что меняем)
# print('123'.startswith('1'))
# array = ['', 'a', '', 'c', '']
# print(''.join(array).lstrip())
# print(str(5.5).zfill(5))
# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(list(string.whitespace))
# print(bytes('hello', encoding='utf8'))
# b = (bytes('афвы', encoding='utf8'))
# print(str(b, encoding='utf8'))
# with open('my_first_file', 'w') as my_file:
#     my_file.write('Hello\n')
#     my_file.write('Hello\n')
#     my_file.writelines(['1', '2', '3'])
# with open('my_first_file', 'r') as my_file:
#     text = my_file.read()
#     my_file.seek(0)
#     lines = my_file.readlines()
#     print(text)
#     print(lines)
#
#
# with open('my_first_file', 'a') as my_file:
#     my_file.write('\n\nNEw text\n')
# import pickle
#
#
# class A:
#     x = 1
#     y = 2
#
#     @classmethod
#     def sum(cls):
#         return cls.x + cls.y
#
#
# with open('my_first_file.b', 'wb') as my_file:
#     my_file.write(pickle.dumps(A))
#
# with open('my_first_file.b', 'rb') as my_file:
#     B = pickle.loads(my_file.read())
#
# print(B.x, B.sum())
# import os
#
# roots = 'C:\\Users\TMS\PycharmProjects\courses'
# elements = os.listdir(roots)
# folders = []
# files = []
# for element in elements:
#     if os.path.isfile(os.path.join(roots, element)):
#         files.append(element)
#     elif os.path.isdir(os.path.join(roots, element)):
#         folders.append(element)
# print(folders, files)
import re
x = 'hello anton, hello world, hello Dima'
print(re.findall(r'he(\w{2})o (\w+)', x))
