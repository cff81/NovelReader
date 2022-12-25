from os import system

# py_file = input('请输入需要打包的py文件：（无需后缀）\n')
py_file = "NovelReader"
if py_file[-3:] != ".py":
    py_file += ".py"
command = str(f"pyinstaller {py_file}")

# console = input('是否显示控制台窗口：（1/0）\n')
console = "0"
while console != '1' and console != '0':
    print('请重新输入')
    console = input('是否显示控制台窗口：（1/0）\n')
else:
    if console == '0':
        command = str(f"pyinstaller -w {py_file}")

# name = input('请输入打包后的程序名称：（可忽略）\n
name = ""
if name:
    command += str(f" -n {name}")

# icon = input('请输入打包后的程序图标（ico文件路径）：（可忽略）\n')
icon = ""
if icon:
    command += str(f" -i {icon}")

command += " -y"

print("即将执行以下命令：")
print(command)
print()

system('pause')
system(command)
system('pause')
