import sqlite3
DATABASE_NAME = "kanban.sqlite3"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    print('fction create"')
    tables = [
        """CREATE TABLE IF NOT EXISTS test(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                rate INTEGER NOT NULL
            )
        """,
        """CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstName TEXT NOT NULL,
                lastName TEXT NOT NULL,
                mail TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)


