import types
import re


class Task1:
    def __init__(self, array):
        self.array = array

    def __getitem__(self, item):
        return self.array[item]

    def __delitem__(self, key):
        x = self.array[key]
        self.array.remove(x)
        return self.array

    def __setitem__(self, key, value):
        self.array[key] = value
        return self.array

    def __mul__(self, other):
        i = 0
        array_new = []
        d = len(self.array) - len(other)
        if d > 0:
            while i < len(other):
                k = self.array[i] * other[i]
                array_new.append(k)
                i += 1
                array_new.extend(self.array[i:])
        elif d < 0:

            while i < len(self.array):
                k = self.array[i] * other[i]
                array_new.append(k)
                i += 1
                array_new.extend(other[i:])
        else:
            while i < len(self.array):
                k = self.array[i] * other[i]
                array_new.append(k)
                i += 1
        return array_new

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return 'Мой лист со значением' + '[' + ','.join(map(str, self.array)) + ']'

    def __ne__(self, other):
        return self.array != other.array


class Task2(type):
    def __new__(cls, name, bases, dct):
        for bases_name in bases:
            if bases_name.__name__.startswith('_'):
                del bases_name
        array = []
        for name, value in dct.items():
            if not name.startwith('__') and not isinstance(cls, types.FunctionType) and not isinstance(cls, type):
                array.append(name)
                array.append(value)
            elif name is isinstance(cls, types.FunctionType) and not name.startwith('__') and not isinstance(cls, type):
                array.append(name)
                array.append(value)
        array_upper = dict((name.upper(), value) for name, value in array)
        return type.__new__(cls, 'Task2_' + name, bases, array_upper)


with open('task3_input.txt', 'r') as my_file_old:
    text = str(my_file_old.read())
    regex_number = re.compile(r'\+375[ |-]?(\d{2})[ |-]?(\d{3})[ |-]?(\d{2})[ |-]?(\d{2})$', re.MULTILINE)
    words = re.findall(r'(?:(?<=\n)|(?<= )|(?<=\A))([A-Z][a-z]{2,9})(?=:| |;|,|\.|\Z|\n)', text)
    address = re.findall(r'(?:Беларусь, )?(?:г\.|город|Город)?[ ](?:Минск, )(?:ул|улица|Улица|пр.|проспект|Проспект)(?:[,|:][ ])([А-Яа-я]+)(?:[,][ ])(?:д|Дом|дом)(?:[.|:][ ])(\d)(?:/|, кв. |, квартира |, Квартира )(\d)', text)

    numbers = regex_number.findall(text)
    array = [''.join(number) for number in numbers]
    string_number = ' '.join(array)
with open('task3_output.txt', 'w', encoding='utf-8') as my_file_new:
    my_file_new.write('Слова: ' + ', '.join(words))
with open('task3_output.txt', 'a', encoding='utf-8') as my_file_new:
    my_file_new.write('\nНомера: ' + ''.join(string_number))


# object = Task1([1, 2, 3])
# print(object.__getitem__(1))
# print(object.__len__())
# print(object.__str__())
# print(object.__delitem__(0))
# print(object.__setitem__(2, 4))
# print(object.__ne__(Task1([1, 2, 3])))
print(words)
print(address)
