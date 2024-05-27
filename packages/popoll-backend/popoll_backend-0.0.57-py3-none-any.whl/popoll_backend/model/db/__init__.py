import sqlite3

def fetchall(cursor: sqlite3.Cursor, ttype: type):
    return [ttype(row) for row in cursor.fetchall()]

def fetchone(cursor: sqlite3.Cursor, ttype: type):
    return fetchall(cursor, ttype)[-1]
