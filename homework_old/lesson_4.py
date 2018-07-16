
# class Studetnt(People): # 4to-to tipa fabrici, ona sozdaet objects
    # university = 'HSCC'
    # def __init__(self, name, group):# метод как должен создаваться объект класса
        # self.name = name
        # self.group = group   # self vozvras4at ne nado

    # def get_name(self):
    #     return self.name # mi eto uje berem iz roditelskogo classa
# class People:
#     def __init__(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
# class Studetnt(People):
#     def __init__(self, name, group):
#         self.group = group
#         super(Studetnt,self).__init__(name)
#
# student_1 = Studetnt('Anton', 234324)
# hasattr(student_1,'name')
# setattr(student_1, 'lol', 666)
# print(student_1.lol)
# class A:
#     x = 1
# class B:
#     x = 2
# class C(A, B):
#     pass
# obj = C()
# print(obj.x)
# class A:
#     def add(self):
#         return self.a + self.b
#     def sub(self):
#         return self.a - self.b
#
#
# class B1(A):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# class C1(A):
#     def __init__(self, a ,b):
#         self.a = a
#         self.b = b


# obj = C1(1, 2)
# print(obj.sub())
# print(obj.add())

# class A:
#     a = 0
#     b = 0
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#    # @classmethod
#    #  @staticmethod
#    #  def get_sum(cls):
#    #      return A.a
#         #return cls.a + cls.b # vsegda budet ravno 0
#
#     @property
#     def y(self):
#         return self.a + self.b
#
# obj = A(1, 2)
# print(obj.y)

# class A:
#     n = 2
#     def __init__(self, a):
#         self.a = a *self.n

# def  __init__(self,a):
#     self.a = a * self.n
# A = type('A',(), {'__init__':__init__, 'n': 2})       # - sozdanie klassa

#x = eval('3**5') # - kak budto v konsole pishehs
# exec ("""
# print('Hello')
# x = 1
# print (x)
# """)