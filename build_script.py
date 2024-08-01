import os
import platform


def build_executable():
    if platform.system() == "Windows":
        os.system("python setup.py build")
    elif platform.system() == "Darwin":
        os.system("python3 setup.py build")
    elif platform.system() == "Linux":
        os.system("python3 setup.py build")
    else:
        print(f"Unsupported OS: {platform.system()}")


if __name__ == "__main__":
    build_executable()
