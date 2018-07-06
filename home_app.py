import werded
from PyQt5 import QtWidgets
import sys
from PIL import Image


from PyQt5.QtWidgets import *


class HomeApp(QtWidgets.QMainWindow, werded.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.convert_button(
            self.image, self.lineEdit, self.lineEdit_2, self.checkBox))
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
            self, 'Open file', 'C:/tms/QT/')[0]
        image = Image.open(fname)
        self.image = image

    @staticmethod
    def convert_button(image, width, height, checkbox):

        if not height.text():
            width = int(width.text())
            ratio = width / image.size[0]
            height = int((float(image.size[1]) * float(ratio)))
            new_image = image.resize((width, height))
            new_image.show()
            if checkbox.isChecked():
                new_image.save('new_image.jpg')
        elif not width.text():
            height = int(height.text())
            ratio = height / image.size[1]
            width = int((float(image.size[0]) * float(ratio)))
            new_image = image.resize((width, height))
            new_image.show()
            if checkbox.isChecked():
                new_image.save('new_image.jpg')
        elif width.text() and height.text():
            new_image = image.resize((
                int(width.text()), int(height.text())))
            new_image.show()
            if checkbox.isChecked():
                new_image.save('new_image.jpg')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HomeApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
