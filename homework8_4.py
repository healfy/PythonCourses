import sqlite3
from sqlalchemy import func
from sqlalchemy.sql.expression import literal, or_, and_
from model4 import *




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
    SELECT Items.id FROM Items GROUP BY Items.name OFFSET 2 LIMIT 2
    """
    cursor.execute(sql_a)
    a = cursor.fetchall()
    sql_b = """SELECT Items.name, D.sphere FROM Items
    JOIN Departments D on Items.department = D.id
    WHERE Items.department IS NOT NULL AND Items.name IS NOT NULL
    """
    cursor.execute(sql_b)
    b = cursor.fetchall()

    sql_c = """
    SELECT Items.name, D.sphere FROM Items
    LEFT JOIN Departments D on Items.department = D.id
    """
    cursor.execute(sql_c)
    c = cursor.fetchall()

    sql_d = """SELECT I.name, sphere From Departments
        LEFT JOIN Items I on Departments.id = I.department
        """
    cursor.execute(sql_d)
    d = cursor.fetchall()

    sql_e = """
    SELECT Items.name, D.sphere FROM Items
    LEFT JOIN Departments D on Items.department = D.id
    UNION
    SELECT I.name, sphere  From Departments
    LEFT JOIN Items I on Departments.id = I.department
    """
    cursor.execute(sql_e)
    e = cursor.fetchall()

    sql_f = """SELECT  Items.name, sphere  From Departments
    CROSS JOIN Items
    """
    cursor.execute(sql_f)
    f = cursor.fetchall()

    sql_g = """
    SELECT COUNT(Items.name) as item_count, SUM(price),
    max(price), min(price), AVG(price)
    FROM Items
    JOIN Departments D on D.id = Items.department    
    GROUP BY  shops
    HAVING item_count > 1
    """
    cursor.execute(sql_g)
    g = cursor.fetchall()
    return tuple(a), tuple(b), tuple(c), tuple(d), tuple(e), tuple(f), tuple(g)


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
            return self.session.query(Items).filter(
                Items.description.isnot(None)).all()
        elif number == 2:
            return [i for i in self.session.query(Departments.sphere).filter(
                Departments.staff_amount > 200
            ).distinct().all()]
        elif number == 3:
            return self.session.query(Shops.address).filter(
                Shops.name.startswith("I")).all()
        elif number == 4:
            return self.session.query(Items).join(Departments).filter(
                Departments.sphere == 'Furniture').all()
        elif number == 5:
            return self.session.query(Shops).join(Departments).join(
                Items).filter(Items.description.isnot(None)).distinct().all()
        elif number == 6:
            return self.session.query(
                Items, Departments, Shops).join(
                Departments).join(Shops).all()
        elif number == 7:
            return self.session.query(Items).group_by(
                Items.name).limit(2).offset(2).all()
        elif number == 8:
            return self.session.query(Items, Departments).join(
                Departments).filter(and_(Items.name.isnot(None),
                                         Departments.sphere.isnot(None))).all()
        elif number == 9:
            return self.session.query(Items, Departments). \
                select_from(Departments).outerjoin(Items).all()
        elif number == 10:
            return self.session.query(Items, Departments). \
                outerjoin(Departments).all()
        elif number == 11:
            return self.session.query(Items, Departments). \
                outerjoin(Departments).union_all(self.session.query(
                    Items, Departments).select_from(
                                            Departments).outerjoin(Items)).all()
        elif number == 12:
            return self.session.query(Items, Departments).join(
                Departments, literal(True)).all()
        elif number == 13:
            return self.session.query(
                func.count(Items.name),
                func.sum(Items.price),
                func.max(Items.price),
                func.min(Items.price),
                func.avg(Items.price)).join(Departments).group_by(
                Departments.shop_id).having(
                func.count(Items.name) > 1).all()
        else:
            raise ValueError

    def update_data(self):
        self.session.query(Items).filter(or_(
            Items.name.startswith('B'), Items.name.endswith('e'))). \
            update(
            {Items.price: Items.price + 100}, synchronize_session='fetch')
        self.session.commit()

    def delete_data_1(self):
        self.session.query(Items).filter(and_(
            Items.price > 500, Items.description.is_(None)
        )).delete()
        self.session.commit()

    def delete_data_2(self):
        self.session.query(Items).filter(Items.id.in_(
            self.session.query(Items.id).join(Departments).join(
                Shops).filter(Shops.address.is_(None)))
        ).delete(synchronize_session='fetch')
        self.session.commit()

    def clear_data(self):
        self.session.query(Shops).delete()
        self.session.query(Items).delete()
        self.session.query(Departments).delete()
        self.session.commit()

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)


