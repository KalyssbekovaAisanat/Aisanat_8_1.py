import sqlite3

con = sqlite3.connect("hw.db")
cur = con.cursor()


def update_item_quantity_by_id(conn, ID,quantity):
    sql = '''UPDATE products SET ID = ?, quantity = ? WHERE ID = ? '''
    cursor = conn.cursor()
    cursor.execute(sql,products)
    conn.commit()

def update_product_price_by_ID(conn, ID, price):
    sql = '''UPDATE products SET ID = ?,price = ? WHERE ID = ? '''
    cursor = conn.cursor()
    cursor.execute(sql, products)
    conn.commit()

def delete_product(conn, ID):
    sql = '''DELETE FROM product WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (id,))
    conn.commit()

def print_all_products(conn):
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)


def search_by_price_and_quantity(conn):
        sql = '''SELECT * FROM products WHERE price < 100.00 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            print(row)


def search_by_word(conn, word):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    cursor = conn.cursor()
    cursor.execute(sql, ('%' + word + '%',))

    rows = cursor.fetchall()
    for row in rows:
        print(row)


def create_product(conn, product: tuple):
  sql = '''INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)'''
  cursor = conn.cursor()
  cursor.execute(sql, product)
  conn.commit()



create_product = '''CREATE TABLE products (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
product_title TEXT (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''


def create_products(conn):
    create_product(conn, ('dirol', 35.50, 5))  # 1
    create_product(conn, ('гномик', 25.00, 10))  # 2
    create_product(conn, ('кола 2л', 120.00, 8))  # 3
    create_product(conn, ('NITRO', 62.40, 12))  # 4
    create_product(conn, ('хлеб', 20, 5))  # 5
    create_product(conn, ('тоналка', 600.99, 2))  # 6
    create_product(conn, ('Мыло', 108.60, 7))  # 7
    create_product(conn, ('mascakara', 400, 20))  # 8
    create_product(conn, ('lipstick', 250.00, 6))  # 9
    create_product(conn, ('mackbook', 105000.00, 3))  # 10
    create_product(conn, ('Alpen Gold', 114.59, 4))  # 11
    create_product(conn, ('water', 19.40, 8))  # 12
    create_product(conn, ('Моющее средство', 73.70, 4))  # 13
    create_product(conn, ('Порошок', 250.00, 3))  # 14
    create_product(conn, ('Подсолнечное Масло', 240.00, 5))  # 15

