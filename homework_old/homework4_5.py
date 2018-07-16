from decimal import Decimal
import random


class Task1B:
    x = 1


class Task1A(Task1B):
    x = 2


class Task1D:
    x = 3


class Task1C(Task1B, Task1D):
    pass


class Task1E(Task1D):
    pass


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
        self.full_name = self.name + ' ' + self.surname

    def _check_subject(self, subject):
        if subject not in self.marks and subject is not None:
            raise ValueError

    def get_average_mark(self, subject=None):
        self._check_subject(subject)
        if subject is None:
            mark1 = [sum(mark)/len(mark) for mark in self.marks.values()]
            return Decimal(sum(mark1)) / Decimal(len(mark1))
        elif subject in self.marks:
            mark2 = self.marks.get(subject)
            return Decimal(sum(mark2)) / Decimal(len(mark2))

    @property
    def subjects(self):
        return [subject for subject in self.marks]

    def change_mark(self, subject, position, value):
        self._check_subject(subject)
        numbers = self.marks.get(subject)
        del numbers[position]
        numbers.insert(position, value)

    @staticmethod
    def compare_students(student_1, student_2, subject=None):
        if student_1.get_average_mark(subject) > student_2.get_average_mark(subject):
            return 1
        elif student_1.get_average_mark(subject) == student_2.get_average_mark(subject):
            return 0
        else:
            return 2


class TicTacToe:
    def __init__(self, name_1, name_2):
        self.name_1 = name_1
        self.name_2 = name_2
        self.__map = [[None for _ in range(3)] for _ in range(3)]
        self._player = bool(random.randint(0, 1))
        self._player_1_symbol = 'X' if self._player is False else 0
        self._player_2_symbol = 'X' if self._player is True else 0
        self._is_finished = False

    def _check_row(self, row):
        row = self.__map[row]
        if row == [True, True, True]:
            return True
        elif row == [False, False, False]:
            return False
        else:
            return None

    def _check_column(self, column):
        column = [self.__map[0][column], self.__map[1][column], self.__map[2][column]]
        if column == [True, True, True]:
            return True
        if column == [False, False, False]:
            return False
        else:
            return None

    def check_winner(self):
        array_1 = [self.__map[0][0], self.__map[1][1], self.__map[2][2]]
        array_2 = [self.__map[0][2], self.__map[1][1], self.__map[2][0]]
        if array_1 == [True, True, True]:
            x = True
        else:
            x = False
        if array_2 == [True, True, True]:
            y = True
        else:
            y = False
        if self._check_row is False or self._check_column is False or x is False or y is False:
            self._is_finished = True
            return False
        elif self._check_row is True or self._check_column is True or x is True or y is True:
            self._is_finished = True
            return True
        else:
            return None

    def next_move(self, row, column):
        if self._is_finished is True:
            return
        else:
            if self.__map[row][column] is None:
                self.__map[row][column] = self._player
                self.check_winner()
                if self.check_winner is False:
                    return False
                elif self.check_winner is True:
                    return True
                elif self.check_winner is None:
                    self._player = not self._player

    def print_map(self):
        array = [i == self._player_1_symbol if i is False else
                 (i == self._player_2_symbol if i is True else ' ') for i in self.__map]
        print(' '.join(array[0]))
        print(' '.join(array[1]))
        print(' '.join(array[2]))







