# setup代码
from cx_Freeze import setup, Executable

executables = [
    Executable(
        script=' C:/Users/eanki/Desktop/python-2019/main.py',  # 目标引用脚本
        # base="win32gui",  # GUI程序需要隐藏控制台
        targetName='poem_2019.exe',  # 生成exe的名字
        icon=" C:/Users/eanki/Desktop/python-2019/Poet.ico"  # 生成exe的的图标
    )]