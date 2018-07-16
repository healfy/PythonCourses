# import sqlite3
# conn = sqlite3.connect('mydatabase.db')
# cursor = conn.cursor()
# # sql_1 = """
# UPDATE Items SET price = price + 100
# WHERE
# Items.name LIKE '%e' or Items.name LIKE 'B%'
# """
# cursor.execute(sql_1)
# conn.commit()

# sql_a = """
# SELECT GROUP_CONCAT(Items.name) as name FROM Items WHERE id>=3 AND id<=4
# """
# cursor.execute(sql_a)
# a = cursor.fetchall()
# print(a)

# sql_b = """SELECT D.sphere,  Items.name   FROM Items
# JOIN Departments D on Items.department = D.id
# WHERE Items.department IS NOT NULL AND Items.name IS NOT NULL
# """
# cursor.execute(sql_b)
# b = cursor.fetchall()
# print(b)
#
# sql_c = """SELECT sphere, I.name From Departments
# LEFT JOIN Items I on Departments.id = I.department
#
# """
# cursor.execute(sql_c)
# c = cursor.fetchall()
# print(c)
#
# sql_d = """
# SELECT D.sphere,  Items.name FROM Items
# LEFT JOIN Departments D on Items.department = D.id
# """
# cursor.execute(sql_d)
# d = cursor.fetchall()
# print(d)
# sql_e = """
# SELECT D.sphere,  Items.name FROM Items
# LEFT JOIN Departments D on Items.department = D.id
# UNION
# SELECT sphere, I.name From Departments
# LEFT JOIN Items I on Departments.id = I.department
# """
# cursor.execute(sql_e)
# e = cursor.fetchall()
# print(e)
#
# sql_f = """SELECT DISTINCT sphere, Items.name From Departments
# CROSS JOIN Items
# """
# cursor.execute(sql_f)
# f = cursor.fetchall()
# print(f)



