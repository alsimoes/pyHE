#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from datetime import *
from sqlalchemy import *
from sqlalchemy.orm import *


class Main():

    db = create_engine('sqlite:///PyHE.db')

    db.echo = True

    meta = MetaData(db)

    def exec_(self):



        if self.db.has_table('Dia') == False:
            print 'Tabela Dia não existe.'
            self.tdia = Table('Dia', self.meta,
                        Column('id', Integer, primary_key=True),
                        Column('data', DateTime),
                        Column('entrada1', Time),
                        Column('saida1', Time),
                        Column('entrada2', Time),
                        Column('saida2', Time),
                        Column('justificativa', String(255)),
                        Column('desconsiderar', Boolean),
                        )
            self.meta.create_all()
        else:
            print 'Tabela Dia existe.'
            self.tdia = Table('Dia', self.meta)


        self._id = 1
        self.dt = date(2013, 5, 4)
        self.e1 = time(9,0)
        self.s1 = time(12,0)
        self.e2 = time(13,0)
        self.s2 = time(18,0)
        self.just = ''
        self.desc = False

        self.ins = self.tdia.insert()

        self.dados = {'id': self._id,
                 'data_marcacao': self.dt,
                 'entrada1': self.e1,
                 'saida1': self.s1,
                 'entrada2': self.e2,
                 'saida2': self.s2,
                 'justificativa': self.just,
                 'desconsiderar': self.desc}

        print 'dados -> ' + str(self.dados)

        print 'Antes insert.'

        self.ins.values(self.dados)
        #ins.values(id=id_, data=dt, entrada1=e1, saida1=s1, entrada2=e2, saida2=s2, justificativa=just, desconsiderar=desc)
        #ins.values(('id',id_), ('data',dt), ('entrada1',e1), ('saida1',s1), ('entrada2',e2), ('saida2',s2), ('justificativa',just), ('desconsiderar',desc))
        #ins.values((id=_id, data=dt, entrada1=e1, saida1=s1, entrada2=e2, saida2=s2, justificativa=just, desconsiderar=desc))

        '''ins.execute(
            data=dt,
            entrada1=e1,
            saida1=s1,
            entrada2=e2,
            saida2=s2,
            justificativa=just,
            desconsiderar=desc
            )'''

        print 'str(ins) -> ' + str(self.ins)

        self.ins.execute()


        #ins.execute()

        #print 'select -> '+ str(tdia.select().execute().fetchall()[0])

    '''
        s = dia.select()
        rs = s.execute()

        row = rs.fetchone()

        for row in rs:
            print 'Data {0} | Entrada: {1} | Saída: {2} | Entrada: {3} | Saída: {4} | Justificativa: {5} | Desconsiderar?: {6}'.format(
                row.data,
                row.entrada1,
                row.saida1,
                row.entrada2,
                row.saida2,
                row.justificativa,
                row.desconsiderar,
                )
    '''



if __name__ == '__main__':
    app = Main()
    app.exec_()

