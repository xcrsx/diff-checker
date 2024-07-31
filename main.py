import sys
import difflib

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtGui import QColor, QTextCursor, QTextCharFormat, QTextBlockFormat

from superqt.utils import CodeSyntaxHighlight
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
        self.ui.clear_btn.clicked.connect(self.clear_forms)
        self.ui.exit_btn.clicked.connect(self.close)


        self.highlighter1 = None
        self.highlighter2 = None


    def open_file1(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File 1")
        if file_name:
            with open(file_name, 'r') as file:
                self.file1_content = file.read()
                self.ui.file1_form.setPlainText(self.file1_content)
            self.highlighter1 = CodeSyntaxHighlight(self.ui.file1_form.document(), "python", "dracula")
            self.compare_files()


    def open_file2(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File 2")
        if file_name:
            with open(file_name, 'r') as file:
                self.file2_content = file.read()
                self.ui.file2_form.setPlainText(self.file2_content)
            self.highlighter1 = CodeSyntaxHighlight(self.ui.file2_form.document(), "python", "dracula")
            self.compare_files()


    def clear_forms(self):
        self.ui.file1_form.clear()
        self.ui.file2_form.clear()


    def compare_files(self):
        if self.file1_content and self.file2_content:
            diff = difflib.ndiff(
                self.file1_content.splitlines(), 
                self.file2_content.splitlines()
            )

            self.ui.diff_view_form.clear()
            cursor = QTextCursor(self.ui.diff_view_form.document())
            file1_line_num = file2_line_num = 1

            for line in diff:
                if line.startswith('-'):
                    self.insert_diff_line(cursor, line[2:], QColor(255, 200, 200), f"{file1_line_num:4} |    | - ")
                    file1_line_num += 1
                elif line.startswith('+'):
                    self.insert_diff_line(cursor, line[2:], QColor(200, 255, 200), f"     | {file2_line_num:4} | + ")
                    file2_line_num += 1
                elif line.startswith(' '):
                    self.insert_diff_line(cursor, line[2:], None, f"{file1_line_num:4} | {file2_line_num:4} |   ")
                    file1_line_num += 1
                    file2_line_num += 1


    def insert_diff_line(self, cursor, code, background_color, prefix=""):
        fmt_prefix = QTextCharFormat()
        cursor.insertText(prefix, fmt_prefix)

        if background_color:
            block_fmt = QTextBlockFormat()
            block_fmt.setBackground(background_color)
            cursor.setBlockFormat(block_fmt)
        else:
            block_fmt = QTextBlockFormat()
            cursor.setBlockFormat(block_fmt)

        cursor.insertText(code)
        cursor.insertText("\n")



if __name__ == "__main__":
    app = QApplication([])
    widget = FileDiffChecker()
    widget.show()
    app.exec()
