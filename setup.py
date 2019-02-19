
from cx_Freeze import setup, Executable
r'''C:\Users\pk\AppData\Local\Programs\Python\Python36\python.exe setup.py build'''

import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
	base = "Win32GUI"


target = Executable(
		script="theMarketRush.py",
		icon="obladaet.ico",
		base= base	
		)


setup(  name = "The Market Rush",
		version = "0.0.1",
		description = "A game is made by request of OBLADAUN ",
		options = {"build_exe": build_exe_options},
		author="Serghom",
		executables = [target])


