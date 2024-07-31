import sys

from PySide6.QtWidgets import QApplication, QWidget

from ui_main import Ui_DiffChecker


class FileDiffChecker(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DiffChecker()
        self.ui.setupUi(self)



if __name__ == "__main__":
    app = QApplication([])
    widget = FileDiffChecker()
    widget.show()
    app.exec()