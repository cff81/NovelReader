from subprocess import call
import sys
import threading
import time

import pyautogui
from pynput import keyboard
from pynput.keyboard import Key
from PyQt5.QtWidgets import QApplication

from Novel import *
from interface import *

app = QApplication(sys.argv)
NOVEL: Novel = Novel(book="Readme.txt", index=0, reader=Reader())

hotkey_pressed = False

hotkey = settings.hotkey
window_on_show = True


def flip(novel: Novel):
    global window_on_show
    if window_on_show:
        time.sleep(settings.automaticFlip - 1)
        novel.next_page()


def Exit():
    PID = os.getpid()
    call(f"taskkill /PID {PID} /f")


def home():
    path = os.path.abspath('')
    path1 = os.path.join(path, "NovelReader.pyw")
    path2 = os.path.join(path, "NovelReader.exe")
    if sys.argv[0][-4:] == ".pyw":
        call(f"pythonw {path1}")
    else:
        call(path2)
    Exit()


def hide():
    global NOVEL
    global window_on_show
    if window_on_show:
        NOVEL.reader.hide()
    else:
        NOVEL.reader.show()
    window_on_show = not window_on_show


def on_press1(key):
    """按下按键时执行。"""
    global hotkey_pressed
    global window_on_show
    global NOVEL
    if key == Key.ctrl_l or key == Key.ctrl_r:
        hotkey_pressed = True
    elif hotkey_pressed:
        if str(key) == "Key.up":
            write_record(NOVEL.path, NOVEL.name, NOVEL.index)
            threading.Thread(target=home).start()
            time.sleep(0.5)
        elif str(key) == "Key.down":
            hide()
            write_record(NOVEL.path, NOVEL.name, NOVEL.index)
        elif str(key) == r"'\x0b'":
            write_record(NOVEL.path, NOVEL.name, NOVEL.index)
            Exit()
        elif window_on_show:
            if str(key) == "Key.left":
                NOVEL.last_page()
            if str(key) == "Key.right":
                NOVEL.next_page()
            if str(key) == "<96>":
                pass


def on_press2(key):
    """按下按键时执行。"""
    global hotkey_pressed
    global window_on_show
    global NOVEL
    if key == Key.alt_l or key == Key.alt_gr:
        hotkey_pressed = True
    elif hotkey_pressed:
        if str(key) == "Key.up":
            write_record(NOVEL.path, NOVEL.name, NOVEL.index)
            threading.Thread(target=home).start()
            Exit()
        elif str(key) == "Key.down":
            hide()
            write_record(NOVEL.path, NOVEL.name, NOVEL.index)
        elif str(key) == r"'k'":
            write_record(NOVEL.path, NOVEL.name, NOVEL.index)
            Exit()
        elif window_on_show:
            if str(key) == "Key.left":
                NOVEL.last_page()
            if str(key) == "Key.right":
                NOVEL.next_page()
            if str(key) == "<96>":
                pass


def on_release1(key):
    """松开按键时执行。"""
    global hotkey_pressed
    if key == Key.ctrl_l or key == Key.ctrl_r:
        hotkey_pressed = False


def on_release2(key):
    """松开按键时执行。"""
    global hotkey_pressed
    if key == Key.alt_l or key == Key.alt_gr:
        hotkey_pressed = False


def listen(novel: Novel):
    global NOVEL
    global hotkey
    NOVEL = novel
    if hotkey == "ctrl":
        with keyboard.Listener(on_press=on_press1, on_release=on_release1) as listener:
            listener.join()
    elif hotkey == "alt":
        with keyboard.Listener(on_press=on_press2, on_release=on_release2) as listener:
            listener.join()


def read_records():
    if not os.path.exists('records/record.txt'):
        with open('records/record.txt', 'w') as record:
            record.write("")
    with open('records/record.txt') as record:
        novel_list = record.readlines()
    _l = []
    if len(novel_list) == 0:
        pyautogui.alert(text='无文件', title='Message')
        return list()
    for novel in novel_list:
        novel = novel.replace('\n', '')
        _l.append(novel)
    return _l


def add_novel(novel_path):
    """添加文件"""
    if not os.path.exists('records/record.txt'):
        with open('records/record.txt', 'w') as record:
            record.write("")
    # 检测文件是否不存在
    try:
        open(novel_path)
    except FileNotFoundError:
        pyautogui.alert(text='文件不存在', title='FileNotFoundError')
        return

    # 获取novel的name
    name = novel_path
    if name.count('\\') != 0:
        name = name[name.rfind('\\') + 1:name.find('.txt')]
    elif name.count('/') != 0:
        name = name[name.rfind('/') + 1:name.find('.txt')]

    # 检测文件是否已存在
    with open('records/record.txt') as record:
        record = record.read()
        if record.count(name) != 0:
            pyautogui.alert(text='文件已存在', title='Message')
            return

    # 将文件加入record
    with open('records/record.txt', 'a+') as record:
        record.write(name + '\n')

    write_record(novel_path, name)
    pyautogui.alert(text='添加成功', title='Message')


def write_record(novel_path, name, index=0):
    """创建阅读记录"""
    with open(f'records/{name}_record.txt', 'w') as novel_record:
        data = name + '\n' + novel_path + '\n' + str(index)
        novel_record.write(data)


def start() -> tuple[str, int]:
    a = pyautogui.confirm('选择一项', buttons=['添加文件', '打开文件', '删除文件', '设置'])
    if a == '添加文件':
        b = pyautogui.prompt('请输入一个TXT文件名：')
        if b:
            b = "G:/NOVEL/" + b
            if b[-4:] != ".txt":
                b += ".txt"
            add_novel(b)
    elif a == '打开文件':
        novel_list = read_records()
        if novel_list:
            b = pyautogui.confirm('选择一个文件打开', buttons=novel_list)
        else:
            b = None
        if b:
            with open(f'records/{b}_record.txt') as novel_record:
                novel_record.readline()
                novel_path = novel_record.readline().replace('\n', '')
                novel_index = int(novel_record.readline().replace('\n', ''))
            return novel_path, novel_index
    elif a == '删除文件':
        novel_list = read_records()
        if novel_list:
            b = pyautogui.confirm('选择一个文件删除', buttons=novel_list)
        else:
            b = None
        if b:
            novel_list.remove(b)
            with open("records/record.txt", "w") as record:
                for novel in novel_list:
                    record.write(novel+"\n")
            os.remove(f'records/{b}_record.txt')
    elif a == '设置':
        setting_page(settings)
    else:
        Exit()
