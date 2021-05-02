import sqlite3


def connect():
    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS storage (itemId INTEGER PRIMARY KEY,itemName TEXT,itemPrice INTEGER,itemQ INTEGER)")
    conn.commit()
    conn.close()


def insert(itemName, itemPrice, itemQ):
    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO storage VALUES (NULL,?,?,?)", (itemName, itemPrice, itemQ))
    conn.commit()
    conn.close()
    view()


def view():
    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM storage")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(itemName="", itemPrice="", itemQ=""):
    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM storage WHERE itemName=? OR itemPrice=? OR itemQ=?', (itemName, itemPrice, itemQ))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(itemId):
    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM storage WHERE itemId=?', itemId)
    conn.commit()
    conn.close()


def update(itemName,itemPrice,itemQ):
    conn = sqlite3.connect("storage.db")
    cur = conn.cursor()
    cur.execute("UPDATE storage SET itemQ=itemQ+?, itemPrice =? WHERE itemName=?",( itemQ,itemPrice,itemName))
    conn.commit()
    conn.close()


def sellItem(itemName, sellQ):
    conn = sqlite3.connect("storage.db")
    cur = conn.cursor()
    cur.execute("UPDATE storage SET itemQ=itemQ-? where itemName=?", (sellQ, itemName))
    conn.commit()
    conn.close()


connect()
