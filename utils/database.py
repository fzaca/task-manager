import sqlite3

def create_connection():
    conn = sqlite3.connect('./database/tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE if not exists task(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL
        );
    ''')
    conn.commit()
    return conn