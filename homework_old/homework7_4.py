import sqlite3


def task_1(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Shops(
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        address VARCHAR NULL,
        staff_amount INTEGER
                      )
    """)
    cursor.execute("""CREATE TABLE Departments(
        id INTEGER PRIMARY KEY,
        sphere VARCHAR,
        staff_amount INTEGER,
        shop VARCHAR,
        FOREIGN KEY (shop) REFERENCES Shops(id)
                    )
    """)
    cursor.execute("""CREATE TABLE Items(
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        description TEXT NULL,
        price INTEGER,
        department VARCHAR,
        FOREIGN KEY (department) REFERENCES Departments(id)
                      )
    """)
    conn.commit()


def task_2(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Shops(name, address, staff_amount)
            VALUES ('Auchan', NULL , 250)
    """)
    cursor.execute("""INSERT INTO Shops(name, address, staff_amount)
            VALUES ('IKEA', 'Street Žirnių g. 56, Vilnius, Lithuania.' , 500)
    """)
    cursor.execute("""INSERT INTO Departments(sphere, staff_amount, shop)
            VALUES ('Furniture', 250 , 1)
    """)
    cursor.execute("""INSERT INTO Departments(sphere, staff_amount, shop)
            VALUES ('Furniture', 300 , 2)
    """)
    cursor.execute("""INSERT INTO Departments(sphere, staff_amount, shop)
            VALUES ('Dishes', 200 , 2)
    """)
    cursor.execute("""INSERT INTO Items(name, description, price, department)
            VALUES ('Table', 'Cheap wooden table', 300, 1)
    """)
    cursor.execute("""INSERT INTO Items(name, description, price, department)
            VALUES ('Table', NULL , 750, 2)
    """)
    cursor.execute("""INSERT INTO Items(name, description, price, department)
            VALUES ('Bed', 'Amazing wooden bed', 1200, 2)
    """)
    cursor.execute("""INSERT INTO Items(name, description, price, department)
            VALUES ('Cup', NULL , 10, 3)
    """)
    cursor.execute("""INSERT INTO Items(name, description, price, department)
            VALUES ('Plate', 'Glass plate', 20, 3)
    """)
    conn.commit()


def task_3(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    sql_a = "SELECT * FROM Items WHERE description IS NOT NULL"
    cursor.execute(sql_a)
    a = cursor.fetchall()
    sql_b = "SELECT DISTINCT sphere FROM Departments WHERE staff_amount > 200"
    cursor.execute(sql_b)
    b = cursor.fetchall()
    sql_c = "SELECT address FROM Shops WHERE name LIKE 'I_%'"
    cursor.execute(sql_c)
    c = cursor.fetchall()
    sql_d = """
    SELECT Items.name FROM Items
    JOIN Departments D ON D.id = department WHERE  department != 3
    """
    cursor.execute(sql_d)
    d = cursor.fetchall()
    sql_e = """
    SELECT DISTINCT Shops.name FROM Shops
    JOIN Departments ON shop = Shops.id
    JOIN Items ON Departments.id = department
    WHERE description IS NOT NULL
    """
    cursor.execute(sql_e)
    e = cursor.fetchall()
    sql_f = """
    SELECT
    Items.name,
    description,
    price,
    department,
    D.sphere as Departments_sphere,
    D.staff_amount as Departments_staff_amount,
    shop,
    S.name as shop_name,
    S.address as shop_address,
    S.staff_amount as shop_staff_amount
    FROM Items JOIN Departments D on Items.department = D.id
               JOIN Shops S on D.shop = S.id
    """
    cursor.execute(sql_f)
    f = cursor.fetchall()
    return tuple(a), tuple(b), tuple(c), tuple(d), tuple(e), tuple(f)


def task_4(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    sql_del = """
    DELETE FROM Items
    WHERE price > 500 and description IS NULL
    """
    cursor.execute(sql_del)
    conn.commit()


def task_5(path_db):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    sql_del_last = """
    DELETE FROM Items WHERE Items.id in (
    SELECT Items.id FROM Items
    JOIN Departments D on Items.department = D.id
    JOIN Shops S on D.shop = S.id
    WHERE address IS NULL
    )
    """
    cursor.execute(sql_del_last)
    conn.commit()
