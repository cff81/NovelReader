from functions import *


def main():
    result = None
    while result is None:
        result = start()
    novel_path, novel_index = result

    READER = Reader()
    novel = Novel(novel_path, novel_index, READER)

    READER.show()

    t1 = threading.Thread(target=listen, args=(novel, ))
    t1.daemon = True
    t1.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        Title = str(type(e)) + "错误"
        pyautogui.alert(text=e, title=Title)
