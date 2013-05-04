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
import sys
from os import path, environ, getcwd
import logging

from ui_files import mainWindowGui

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
    APPLICATION_PATH = path.join(getcwd())
elif sys.platform == 'win32':
    APPLICATION_PATH = path.join(environ['APPDATA'], __appname__)
else:
    APPLICATION_PATH = path.expanduser(path.join("~", "." + __appname__))

"""
Logging configuration
"""
formato_log = "".join(["%(asctime)s: ",
    "%(name)s - ",
    "%(levelname)s - ",
    "%(module)s - ",
    "%(funcName)s - ",
    "%(lineno)d - ",
    "%(message)s"])

logging.basicConfig(filename="".join([APPLICATION_PATH,"/",__appname__ ,".log"]), format=formato_log,)

logger = logging.getLogger(__appname__)

logger.info("".join(["APPLICATION_PATH: ", APPLICATION_PATH]))


class Main(QMainWindow, mainWindowGui.Ui_mainWindow):

    def __init__ (self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        """
        SIGNALS Connections
        """
        self.actionSair.triggered.connect(self.fechar_app)
        self.actionAbrir.triggered.connect(self.abre_arquivo)
        self.actionMarcaPonto.triggered.connect(self.marca_ponto)
        self.actionAdicionarHorarios.triggered.connect(self.adicionar_horario)
        self.actionEditarHorarios.triggered.connect(self.editar_horario)
        self.actionExcluirHorarios.triggered.connect(self.excluir_horario)
        self.actionConfiguracoes.triggered.connect(self.configuracoes)
        self.actionRelatorioMes.triggered.connect(self.gera_relario)
        self.actionImportarArquivo.triggered.connect(self.importar_arquivo)
        self.actionSobre.triggered.connect(self.sobre)

    def abre_arquivo(self):
        """
        Abre o diálogo para seleção do arquivo da base de dados.
        """
        QMessageBox.information(self, __appname__, u"""
        Abre o diálogo para seleção do arquivo da base de dados.
        """)

    def marca_ponto(self):
        """
        Obtem a hora e minutos atuais e inclui o horário
        na próxima marcação de horário livre do dia.
        """
        QMessageBox.information(self, __appname__, u"""
        Obtem a hora e minutos atuais e inclui o horário
        na próxima marcação de horário livre do dia.
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
        """
        try:
            logger.info("Application finished wrong way.")
            sys.exit(0)
        except IOError as e:
            logger.Exception("I/O error({0}): {1}".format(e.errno, e.strerror))


def main():
    logger.info("Application started.")
    QCoreApplication.setApplicationName(__appname__)
    QCoreApplication.setApplicationVersion(__version__)
    QCoreApplication.setOrganizationName(__organization__)
    QCoreApplication.setOrganizationDomain(__domain__)

    app = QApplication(sys.argv)
    form = Main()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
