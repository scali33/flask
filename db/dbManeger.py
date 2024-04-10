from .dbcontext import *

DATA_BASE = 'NOTES.db'

class DataBase:
    def __init__(self):
        with DataBaseConnection(DATA_BASE)as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS POSTS(Post_id integer Primary key, Name text, Post_content text)')
    def instert_post(self,title,post):
        with DataBaseConnection(DATA_BASE) as con:
            cur = con.cursor()
            cur.execute('INSERT INTO POSTS(Name, Post_content) VALUES(?,?)',(title,post))
            last_id = cur.lastrowid
        return last_id

    def retrive_one_post(self,id) -> list:
        with DataBaseConnection(DATA_BASE) as con:
            cur = con.cursor()
            cur.execute(f'SELECT Name,Post_content FROM POSTS where Post_id =? ',(id,))
            res = cur.fetchone()
            return res
    def post_lsit(self):
        with DataBaseConnection(DATA_BASE) as con:
            cur = con.cursor()
            cur.execute('select Post_id,Name from Posts')
            res = cur.fetchall()
            return res