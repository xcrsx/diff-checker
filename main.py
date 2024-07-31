import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

from ui_main import Ui_DiffChecker


class FileDiffChecker(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_DiffChecker()
        self.ui.setupUi(self)

        self.file1_content = ""
        self.file2_content = ""

        # Buttons
        self.ui.openFile1_btn.clicked.connect(self.open_file1)
        self.ui.openFile2_btn.clicked.connect(self.open_file2)


    def open_file1(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File 1")
        if file_name:
            with open(file_name, 'r') as file:
                self.file1_content = file.read()
                self.ui.file1_form.setPlainText(self.file1_content)


    def open_file2(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File 2")
        if file_name:
            with open(file_name, 'r') as file:
                self.file2_content = file.read()
                self.ui.file2_form.setPlainText(self.file2_content)


if __name__ == "__main__":
    app = QApplication([])
    widget = FileDiffChecker()
    widget.show()
    app.exec()