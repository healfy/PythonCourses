import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('arial', 10))

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(self.btn_clicked)

        qbtn = QPushButton('Quit', self)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 50)
        qbtn.clicked.connect(QCoreApplication.instance().quit)

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('My first class app')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def btn_clicked(self):
        sender = self.sender()
        self.stasuBar().showMessage('Button with text {}'.format(
            sender.txt()
        ))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
