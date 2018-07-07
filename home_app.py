import werded
from PyQt5 import QtWidgets
import sys
from PIL import Image


from PyQt5.QtWidgets import *


class HomeApp(QtWidgets.QMainWindow, werded.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.convert_button)
        self.findButton.clicked.connect(self.show_dialog)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def show_dialog(self):

        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'C:/Users/Mitrandir/PycharmProjects/QT/')[0]

        self.image = Image.open(fname)

    def convert_button(self):
        if not self.lineEdit_2.text():
            width = int(self.lineEdit.text())
            ratio = width / self.image.size[0]
            height = int((float(self.image.size[1]) * float(ratio)))
            new_image = self.image.resize((width, height))
            new_image.show()
            if self.checkBox.isChecked():
                new_image.save('new_image.jpg')
        elif not self.lineEdit.text():
            height = int(self.lineEdit_2.text())
            ratio = height / self.image.size[1]
            width = int((float(self.image.size[0]) * float(ratio)))
            new_image = self.image.resize((width, height))
            new_image.show()
            if self.checkBox.isChecked():
                new_image.save('new_image.jpg')
        elif self.lineEdit.text() and self.lineEdit_2.text():
            new_image = self.image.resize((
                int(self.lineEdit.text()), int(self.lineEdit_2.text())))
            new_image.show()
            if self.checkBox.isChecked():
                new_image.save('new_image.jpg')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HomeApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
