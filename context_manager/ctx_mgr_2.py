# -*- coding: UTF-8 -*-

import psycopg2

class DBConnection(object):
    def __init__(self, dbname=None,
                 user=None, password=None, host='localhost'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            host=self.host,
            user=self.user,
            password=self.password,
        )
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_instance, traceback):
        self.connection.close()

if __name__ == '__main__':
    with DBConnection(user='postgres', dbname='test1_db', password='123456') as db:
        db.execute('SELECT * FROM public.employees')
        print (db.fetchall())
