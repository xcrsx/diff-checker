from cx_Freeze import setup, Executable
import platform

main_script = "main.py" 


base = None
if platform.system() == "Windows":
    base = "Win32GUI"


options = {
    "build_exe": {
        "packages": [],
        "include_files": [],
    }
}


setup(
    name="DiffChecker",
    version="1.0",
    description="A file comparison tool",
    options=options,
    executables=[Executable(main_script, base=base, target_name="DiffChecker")],
)
