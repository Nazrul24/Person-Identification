from http.server import executable
from cx_Freeze import setup, Executable
from importlib_metadata import version

setup(name="Person Identifacion",
    version="0.1",
    description="Identifies person from webcam",
    executables = [Executable("main.py")]
)