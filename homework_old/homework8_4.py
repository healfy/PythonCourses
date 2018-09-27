import sqlite3
from models import *


def task_1(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    sql_1 = """
    UPDATE Items SET price = price + 100
    WHERE
    Items.name LIKE '%e' or Items.name LIKE 'B%'
    """
    cursor.execute(sql_1)
    conn.commit()


def task_2(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    sql_a = """
    SELECT GROUP_CONCAT(Items.name) as name FROM Items WHERE id>=3 AND id<=4
    """
    cursor.execute(sql_a)
    a = cursor.fetchall()
    sql_b = """SELECT D.sphere,  Items.name   FROM Items
    JOIN Departments D on Items.department = D.id
    WHERE Items.department IS NOT NULL AND Items.name IS NOT NULL
    """
    cursor.execute(sql_b)
    b = cursor.fetchall()

    sql_c = """SELECT sphere, I.name From Departments
    LEFT JOIN Items I on Departments.id = I.department
    """
    cursor.execute(sql_c)
    c = cursor.fetchall()

    sql_d = """
    SELECT D.sphere,  Items.name FROM Items
    LEFT JOIN Departments D on Items.department = D.id
    """
    cursor.execute(sql_d)
    d = cursor.fetchall()

    sql_e = """
    SELECT D.sphere,  Items.name FROM Items
    LEFT JOIN Departments D on Items.department = D.id
    UNION
    SELECT sphere, I.name From Departments
    LEFT JOIN Items I on Departments.id = I.department
    """
    cursor.execute(sql_e)
    e = cursor.fetchall()

    sql_f = """SELECT DISTINCT sphere, Items.name From Departments
    CROSS JOIN Items
    """
    cursor.execute(sql_f)
    f = cursor.fetchall()
    return tuple(a), tuple(b), tuple(c), tuple(d), tuple(e), tuple(f)


class Task3:
    def __init__(self, path_db):
        self.path_db = path_db
        self.engine = engine
        self.session = session

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def insert_data(self):
        shop_1 = Shops(
            name='Auchan',
            staff_amount=250)
        shop_2 = Shops(
            name='IKEA',
            address='Street Žirnių g. 56, Vilnius, Lithuania',
            staff_amount=500
        )
        departament_1 = Departments(
            sphere='Furniture',
            staff_amount=250,
            shop=shop_1
        )
        departament_2 = Departments(
            sphere='Furniture',
            staff_amount=300,
            shop=shop_2
        )
        departament_3 = Departments(
            sphere='Dishes',
            staff_amount=200,
            shop=shop_2
        )
        item_1 = Items(
            name='Table',
            description='Cheap wooden table',
            price=300,
            department=departament_1
        )
        item_2 = Items(
            name='Table',
            price=750,
            department=departament_2
        )
        item_3 = Items(
            name='Bed',
            description='Amazing wooden bed',
            price=1200,
            department=departament_2
        )
        item_4 = Items(
            name='Cup',
            price=10,
            department=departament_3
        )
        item_5 = Items(
            name='Plate',
            description='Glass plate',
            price=20,
            department=departament_3
        )
        self.session.add_all([
            shop_1, shop_2,
            departament_1, departament_2, departament_3,
            item_1, item_2, item_3, item_4, item_5
        ])

        self.session.commit()

    def select_data(self, number):
        if number == 1:
            return self.session.query(Items.name).filter(
                Items.description is not '<null>').all()
        elif number == 2:
            return [i for i in self.session.query(Departments.sphere).filter(
                Departments.staff_amount > 200
            ).all()]
        elif number == 3:
            return self.session.query(Shops.address).filter(
                Shops.name.startswith("I")).all()
        elif number == 4:
            return self.session.query(Items.name).join(Departments).filter(
                Departments.sphere == 'Furniture').all()
        elif number == 5:
            return self.session.query(Shops.name).join(Departments).join(
                Items).filter(Items.description is not None).all()
        elif number == 6:
            return self.session.query(
                Items.name, Departments.sphere, Shops.name).join(
                Departments).join(Shops).all()
        elif number == 7:
            return self.session.query(Items.name).group_by(
                Items.name).all()

        else:
            pass


o = Task3('new_file.db')
y = o.select_data(6)
print(y)

