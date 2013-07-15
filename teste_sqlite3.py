#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import *
from datetime import *
from sqlite3 import *

def main():

    file_ = "PyHE.db"
    conn = connect(file_)

    cur = conn.cursor()

    sqlCmd = '''CREATE TABLE IF NOT EXISTS Dia (id INTEGER PRIMARY KEY
                                               ,data TEXT
                                               ,entrada_1 TEXT
                                               ,saida_1 TEXT
                                               ,entrada_2 TEXT
                                               ,saida_2 TEXT
                                               ,justificativa TEXT
                                               ,desconsiderar NUMERIC
                                               )'''
    cur.execute(sqlCmd)
    conn.commit()

    marcacoes = [(None, '2012-04-02', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-04-03', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-04-07', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-04-08', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-04-09', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-04-10', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-04-11', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-05-02', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-05-03', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-05-07', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-05-08', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-05-09', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-05-10', '09:00', '12:00', '13:00', '18:00', '', 0),
                 (None, '2012-05-11', '09:00', '12:00', '13:00', '18:00', '', 0),
                 ]
    #cur.executemany('INSERT INTO Dia VALUES (?,?,?,?,?,?,?,?)', marcacoes)

    #conn.commit()

    for row in cur.execute('SELECT * FROM Dia ORDER BY data'):
        print str(row) + ' - ok'

'''
horario = [int(x) for x in '09:15'.split(':')]
time(horario[0],horario[1])
'''


if __name__ == "__main__":
    main()