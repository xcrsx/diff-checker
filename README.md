# DiffChecker

DiffChecker is a Qt-based GUI application that allows users to compare the contents of two text files. It highlights differences, showing added and removed lines with color coding. This tool is useful for developers and anyone needing to visually compare file contents.

## Features

- **File Comparison**: Load two files and compare their contents line by line.
- **Syntax Highlighting**: Automatically detects the programming language of the files and applies syntax highlighting using the "Dracula" theme.
- **Visual Diff**: Highlights added lines in green and removed lines in red, making it easy to identify differences.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/xcrsx/diff-checker.git
    cd diff-checker
    ```

2. Set a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Ensure the ui_main.py file is in the directory. This file should be generated from a Qt Designer .ui file using pyside6-uic.

5. ##### (Optional) Create a Standalone Executable

    If you want to create a standalone executable, you can do so with the following steps:
    - Run the build script:

    ```sh
    python build_script.py
    ```

    - This command will generate an executable file in the build directory. This standalone executable can be used to run the application without needing Python or the dependencies installed on the target machine.

### Usage

- #### Run the Application Using Python

    ```sh
    python main.py
    ```

- #### Run the Standalone Executable

    If you created a standalone executable in the setup process, you can run it directly from the `build` directory. The executable is platform-specific:

  - On Windows: `DiffChecker.exe`
  - On macOS/Linux: `DiffChecker` (you may need to make it executable with `chmod +x DiffChecker`)

#### How to Use

1. Open File 1: Click the "Open File 1" button to select the first file for comparison.
2. Open File 2: Click the "Open File 2" button to select the second file.
3. View Differences: The differences between the two files will be displayed in the "Diff View" area.
4. Clear Forms: Click the "Clear" button to reset the forms and start a new comparison.
5. Exit: Click the "Exit" button to close the application.

#### Code Structure

- main.py: The main script that initializes the GUI and handles file comparison.
- ui_main.py: The auto-generated file from the Qt Designer .ui file, setting up the UI layout.

### Acknowledgements

- [Qt for Python (PySide6)](https://pypi.org/project/PySide6/)
- [superqt](https://pypi.org/project/superqt/) for utility functions and syntax highlighting
