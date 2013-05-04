#!/usr/bin/env python
# -*- coding: utf-8 -*-

__appname__ = "PyHE"
__module__ = "main"
__version__ = "1.0"
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
        self.actionSobre.triggered.connect(self.sobre)


    def sobre(self):
        """
        Abre o tela sobre.
        """
        dialog = Sobre()
        dialog.exec_()

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


class Sobre(QDialog):

    def __init__ (self, parent=None):
        super(Sobre, self).__init__(parent)

        self.setWindowTitle("Sobre")
        self.setSizeGripEnabled(False)


        self.nome_app = QLabel("".join(["<font size=14>", __appname__, "</font>"]), self)
        self.versao = QLabel("".join([u"Versão ", __version__, " (", __build__, ")"]), self)
        self.link = QLabel("".join(['<a href="', __domain__, '">', __domain__[7:], "</a>"]), self)
        self.licenca = QLabel("".join([__copyright__,", ",__autor__, "."]), self)

        self.link.linkActivated.connect(self.abre_link)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.nome_app)
        self.layout.addWidget(self.versao)
        self.layout.addWidget(self.link)
        self.layout.addWidget(self.licenca)
        self.setLayout(self.layout)

    def abre_link(self):
        QDesktopServices.openUrl(QUrl(__domain__))

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


"""
## TODO - Lista das coisas que precisa ser programadas:

[ ] Definir um tamanho para as janelas.

"""