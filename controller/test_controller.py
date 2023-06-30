from db import get_db


def insert_test(name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO test(name, price, rate) VALUES (?, ?, ?)"
    cursor.execute(statement, [name, price, rate])
    db.commit()
    return True


def update_test(id, name, price, rate):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE test SET name = ?, price = ?, rate = ? WHERE id = ?"
    cursor.execute(statement, [name, price, rate, id])
    db.commit()
    return True


def delete_test(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM test WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, price, rate FROM test WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_test():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, name, price, rate FROM test"
    cursor.execute(query)
    return cursor.fetchall()


