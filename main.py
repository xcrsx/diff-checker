import difflib
import sys

from pygments.lexers import guess_lexer_for_filename
from PySide6.QtGui import (QColor, QTextBlockFormat, QTextCharFormat,
                           QTextCursor)
from PySide6.QtWidgets import QApplication, QFileDialog, QWidget
from superqt.utils import CodeSyntaxHighlight

from ui_main import Ui_DiffChecker


class FileDiffChecker(QWidget):
    """
    A class for comparing the contents of two files and displaying the differences
    in a user interface.

    This widget provides functionality to open two text files, highlight syntax based
    on file type, and visually compare the contents by showing added and removed lines.
    """

    def __init__(self):
        """
        Initializes the FileDiffChecker widget, setting up the UI and connecting signals.
        """
        super().__init__()
        self.ui = Ui_DiffChecker()
        self.ui.setupUi(self)

        self.file1_content = ""
        self.file2_content = ""

        # Connecting buttons to their respective slots
        self.ui.openFile1_btn.clicked.connect(self.open_file1)
        self.ui.openFile2_btn.clicked.connect(self.open_file2)
        self.ui.clear_btn.clicked.connect(self.clear_forms)
        self.ui.exit_btn.clicked.connect(self.close)

        self.highlighter1 = None
        self.highlighter2 = None
        self.highlighter3 = None

    def open_file1(self):
        """
        Opens a file dialog to select and read the first file. It displays the file content
        in the corresponding text form and applies syntax highlighting.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File 1")
        if file_name:
            with open(file_name, "r") as file:
                self.file1_content = file.read()
                self.ui.file1_form.setPlainText(self.file1_content)
            # Detect language for syntax highlighting
            language = self.detect_language(file_name, self.file1_content)
            CodeSyntaxHighlight(self.ui.file1_form.document(), language, "dracula")
            CodeSyntaxHighlight(self.ui.diff_view_form.document(), language, "dracula")
            # Compare files after loading the first one
            self.compare_files()

    def open_file2(self):
        """
        Opens a file dialog to select and read the second file. It displays the file content
        in the corresponding text form and applies syntax highlighting.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File 2")
        if file_name:
            with open(file_name, "r") as file:
                self.file2_content = file.read()
                self.ui.file2_form.setPlainText(self.file2_content)
            # Detect language for syntax highlighting
            language = self.detect_language(file_name, self.file2_content)
            CodeSyntaxHighlight(self.ui.file2_form.document(), language, "dracula")
            # Compare files after loading the second one
            self.compare_files()

    def clear_forms(self):
        """
        Clears the content of all text forms (file1, file2, and diff view).
        """
        self.ui.file1_form.clear()
        self.ui.file2_form.clear()
        self.ui.diff_view_form.clear()

    def compare_files(self):
        """
        Compares the contents of the two loaded files and displays the differences.
        Added lines are highlighted in green, removed lines in red, and unchanged lines are not highlighted.
        """
        if self.file1_content and self.file2_content:
            # Calculate the differences between two files
            diff = difflib.ndiff(
                self.file1_content.splitlines(), self.file2_content.splitlines()
            )

            self.ui.diff_view_form.clear()
            cursor = QTextCursor(self.ui.diff_view_form.document())
            file1_line_num = file2_line_num = 1

            # Iterate through the diff output and apply formatting
            for line in diff:
                if line.startswith("-"):
                    self.insert_diff_line(
                        cursor,
                        line[2:],
                        QColor(255, 85, 85, 50),
                        f"{file1_line_num:4} |    | - ",
                    )
                    file1_line_num += 1
                elif line.startswith("+"):
                    self.insert_diff_line(
                        cursor,
                        line[2:],
                        QColor(80, 250, 123, 50),
                        f"     | {file2_line_num:4} | + ",
                    )
                    file2_line_num += 1
                elif line.startswith(" "):
                    self.insert_diff_line(
                        cursor,
                        line[2:],
                        None,
                        f"{file1_line_num:4} | {file2_line_num:4} |   ",
                    )
                    file1_line_num += 1
                    file2_line_num += 1

    def insert_diff_line(self, cursor, code, background_color, prefix=""):
        """
        Inserts a line of code with optional background color into the diff view form.

        Args:
            cursor (QTextCursor): Cursor for the text document where the diff is displayed.
            code (str): The code line to be inserted.
            background_color (QColor): The background color for the line.
            prefix (str): A prefix indicating the type of change (e.g., "+", "-", " ").
        """
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

    def detect_language(self, file_name, file_content):
        """
        Detects the programming language of the given file content for syntax highlighting.

        Args:
            file_name (str): The name of the file.
            file_content (str): The content of the file.

        Returns:
            str: The name of the detected language.
        """
        language = guess_lexer_for_filename(file_name, file_content).name
        return language


if __name__ == "__main__":
    app = QApplication([])
    widget = FileDiffChecker()
    widget.show()
    app.exec()
