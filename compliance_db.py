import sqlite3

conn = sqlite3.connect("compliance_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        amount REAL,
        currency TEXT,
        country TEXT,
        risk TEXT
    )
""")
conn.commit()
