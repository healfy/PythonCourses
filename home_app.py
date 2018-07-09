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

    def convert_button(self, event):
        try:
            result = self.convert_image(self.image,
                                        self.lineEdit.text(),
                                        self.lineEdit_2.text())
            result.show()
            self.result = result

        except ValueError:
            reply = QMessageBox.warning(self, 'Message',
                                        'Введите ширину или высоту',
                                        QMessageBox.Ok, QMessageBox.No)
            if reply == QMessageBox.Ok:
                pass
            else:
                event.ignore()

    @staticmethod
    def convert_image(image, width, height):
        if not height and width:
            ratio = int(width) / image.size[0]
            height1 = int((float(image.size[1]) * float(ratio)))
            new_image = image.resize((int(width), height1))
            return new_image
        elif not width and height:
            ratio = int(height) / image.size[1]
            width1 = int((float(image.size[0]) * float(ratio)))
            new_image = image.resize((width1, int(height)))
            return new_image
        elif width and height:
            new_image = image.resize((int(width), int(height)))
            return new_image
        elif not width and not height:
            raise ValueError


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HomeApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
