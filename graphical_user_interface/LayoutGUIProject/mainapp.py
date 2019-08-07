from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from mainwidegts import Ui_Form

## what inherit class from Appwindow is decided the ui file created type. I create the widgets type UI from GUI tool.
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

if __name__ =='__main__':
    ## follow implementation not use the GUI Design tool
    # app = QApplication([])
    # window = QWidget()
    # layout = QVBoxLayout()
    # layout.addWidget(QPushButton('Top'))
    # layout.addWidget(QPushButton('Bottom'))
    # window.setLayout(layout)
    # window.show()
    # app.exec_()
    app = QApplication([])
    window = AppWindow()
    window.show()
    app.exec_()