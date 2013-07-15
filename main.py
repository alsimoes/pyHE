#!/usr/bin/env python
# -*- coding: utf-8 -*-

__appname__ = "PyHE"
__module__ = "main"
__version__ = "0.1"
__build__ = "0001"
__autor__ = u"André Simões"
__organization__ = u"André Simões"
__domain__ = "http://github.com/alsimoes/pyHE"
__copyright__ = u"Copyright © 2013"
__license__ = "GPL v3"

from PySide.QtCore import *
from PySide.QtGui import *
from sqlite3 import *
from datetime import *
from ui_files import mainWindowGui
import sys
import os
import logging




"""
## MODELO ##
try:
    raise RuntimeError
except Exception, err:
    log.exception("Error!")
"""


"""
Path configuration
"""
if sys.platform == 'darwin':
    APPLICATION_PATH = os.path.join(os.getcwd())
elif sys.platform == 'win32':
    APPLICATION_PATH = os.path.join(environ['APPDATA'], __appname__)
else:
    #APPLICATION_PATH = os.path.expanduser(os.path.join("~", "." + __appname__))
    APPLICATION_PATH = os.path.join(os.getcwd())

"""
Logging configuration
"""
LOGGING_FILE = "".join([APPLICATION_PATH,"/",__appname__ ,".log"])

LOGGING_FORMAT = "".join(["%(asctime)s",
                         " %(name)s",
                         " %(levelname)s",
                         " %(module)s",
                         " %(funcName)s",
                         " %(lineno)d",
                         " %(message)s"
                        ])

logging.basicConfig(filename=LOGGING_FILE, format=LOGGING_FORMAT,)

logger = logging.getLogger(__appname__)


"""
Banco de dados
"""
DATA_FILE = "".join([APPLICATION_PATH, "/", __appname__,".db"])

class Main(QMainWindow, mainWindowGui.Ui_mainWindow):

    try:
        conn = connect(DATA_FILE)
        cur = conn.cursor()
    except Exception, err:
        logger.error(err)


    def __init__ (self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)


        self.sqlCmd = '''CREATE TABLE IF NOT EXISTS Dia (id INTEGER PRIMARY KEY
                                                        ,data TEXT
                                                        ,entrada_1 TEXT
                                                        ,saida_1 TEXT
                                                        ,entrada_2 TEXT
                                                        ,saida_2 TEXT
                                                        ,justificativa TEXT
                                                        ,desconsiderar NUMERIC
                                                        )'''

        try:
            self.cur.execute(sqlCmd)
            self.conn.commit()
        except Exception, err:
            logger.error(err)

        self.popular_treeview()

        """
        SIGNALS Connections
        """
        self.actionSair.triggered.connect(self.fechar_app)
        self.actionAbrir.triggered.connect(self.abre_arquivo)
        self.actionNovo.triggered.connect(self.novo_arquivo)
        self.actionBaterPonto.triggered.connect(self.bater_ponto)
        self.actionAdicionarHorarios.triggered.connect(self.adicionar_horario)
        self.actionEditarHorarios.triggered.connect(self.editar_horario)
        self.actionExcluirHorarios.triggered.connect(self.excluir_horario)
        self.actionConfiguracoes.triggered.connect(self.configuracoes)
        self.actionRelatorioMes.triggered.connect(self.gera_relario)
        self.actionImportarArquivo.triggered.connect(self.importar_arquivo)
        self.actionSobre.triggered.connect(self.sobre)



    def popular_treeview(self):
        """
        Obtém todos os anos e meses na base de dados e atualiza a QTreeVew.
        """
        qry_result = []
        qry_result = self.cur.execute("SELECT DISTINCT substr(data,1,7) FROM Dia ORDER BY data")
        resultado = []
        for item in qry_result:
            #splited_item = [int(x) for x in item[0].split("-")]
            #meses = datetime(splited_item[0],splited_item[1], splited_item[2])
            #data = datetime(splited_item[0],splited_item[1],1)
            #datas.append(data)
            splited_item = item[0].split("-")
            resultado.append(splited_item)

        #for dt in datas:
            #print str(dt)
        #print "--> begin debug <--"
        #for item in resultado:
        #    print item
        #print "--> end debug <--"


        #model = QFileSystemModel()
        #model.setRootPath(APPLICATION_PATH)
        #self.arvoreMeses.setModel(model)


        """
        model = QStandardItemModel()
        parentItem = model.invisibleRootItem()
        for i in range(4):
            item = QStandardItem("item %d" % i)
            parentItem.appendRow(item)
            parentItem = item
        """

        model = QStandardItemModel()
        parentItem = model.invisibleRootItem()

        ano = ""
        mes = ""


        for elemento in resultado:
            if ano != elemento[0]:
                ano = elemento[0]
                item_a = QStandardItem(ano)
                parentItem.appendRow(item_a)



        """
        for registro in resultado:
            for elemento in registro:
                if len(elemento) > 2:
                    if ano != elemento:
                        ano = elemento
                        item_ano = QStandardItem(ano)
                        parentItem.appendRow(item_ano)
                elif len(elemento) < 2:
                    mes = elemento
                    item = QStandardItem(mes)
                    parentItem.appendRow(item)
                    parentItem = item_ano
        """


        model.setHorizontalHeaderLabels([u"Mês",])
        self.arvoreMeses.setModel(model)

    def novo_arquivo(self):
        """
        Abre o diálogo para seleção do local do arquivo da base de dados.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre o diálogo para seleção do local do arquivo da base de dados.
        """)

    def abre_arquivo(self):
        """
        Abre o diálogo para seleção do arquivo da base de dados.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre o diálogo para seleção do arquivo da base de dados.
        """)

    def bater_ponto(self):
        """
        Obtem a hora e minutos atuais e inclui o horário na próxima marcação de horário livre do dia.
        """
        QMessageBox.information(self, __appname__, u"""
        Obtem a hora e minutos atuais e inclui o horário na próxima marcação de horário livre do dia.
        """)

    def adicionar_horario(self):
        """
        Abre o diálogo para adição dos horário do dia.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre o diálogo para adição dos horário do dia.
        """)

    def editar_horario(self):
        """
        Abre o diálogo edição dos horário do dia.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre o diálogo edição dos horário do dia.
        """)

    def excluir_horario(self):
        """
        Abre o diálogo para exclusão dos horário do dia.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre o diálogo para exclusão dos horário do dia.
        """)

    def configuracoes(self):
        """
        Abre o diálogo das configurações gerais do sistema.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre o diálogo das configurações gerais do sistema.
        """)

    def gera_relario(self):
        """
        Gera o relatório do mês selecionado na tela principal.
        """
        QMessageBox.information(self, __appname__, u"""
        Gera o relatório do mês selecionado na tela principal.
        """)

    def importar_arquivo(self):
        """
        Abre diálogo de seleção de arquivo para importção.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre diálogo de seleção de arquivo para importção.
        """)




    def sobre(self):
        """
        Abre o Diálogo Sobre.
        """
        texto_sobre = u'''<font size=13>{0}</font><br/>Versão {1} ({2})<br/><br/>
                          <a href="{3}">{3}</a><br/><br/>{4}, {5}.'''.format(
                            __appname__,
                            __version__,
                            __build__,
                            __domain__,
                            __copyright__,
                            __autor__)
        QMessageBox.about(self, "Sobre", texto_sobre)

    def marca_ponto(self):
        pass

    def fechar_app(self):
        """
        Fecha o aplicativo.

        # Some way to kill app.
        if sys.platform == "win32":
            # This works on Windows
            os.kill(os.getpid(), -9)
        else:
            # This works on Mac/Linux
            os.system("kill -9 %d" % os.getpid())
        """
        sys.exit(0)

if __name__ == "__main__":
    logger.info("Application started.")
    QCoreApplication.setApplicationName(__appname__)
    QCoreApplication.setApplicationVersion(__version__)
    QCoreApplication.setOrganizationName(__organization__)
    QCoreApplication.setOrganizationDomain(__domain__)

    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())
