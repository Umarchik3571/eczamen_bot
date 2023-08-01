import sqlite3 as sql


async def create_tables():
    con = sql.connect("music.db")
    cur = con.cursor

    cur.execute("""CREATE TEABLE IF NOT EXISTS music(
                title TEXT,
                music_id TEXT
    )""")


async def insert_data(name,music_id):
        con = sql.connect("music.db")
        cur = con.cursor

        cur.execute("""INSERT INTO music (title,music_id) VALUES (?, ?)""",)

        con.commit()


async def get_all_music():
    con = sql.connect("music.db")
    cur =con.cursor()

    data = cur.execute("SELECT * FROM music").fetchall
    return data