import os


class Settings:
    perPage = 60
    automaticFlip = 5
    column = 2
    color = "#0F0"
    fontSize = 16
    hotkey = "ctrl"  # 值为ctrl或alt字符串
    font = "楷体"

    def __init__(self):
        self.perPage = Settings.perPage
        self.automaticFlip = Settings.automaticFlip
        self.column = Settings.column
        self.color = Settings.color
        self.fontSize = Settings.fontSize
        self.hotkey = Settings.hotkey
        self.font = Settings.font

    def save(self):
        data = str(self.perPage) + "\n" + \
               str(self.automaticFlip) + "\n" + \
               str(self.column) + "\n" + \
               str(self.color) + "\n" + \
               str(self.fontSize) + "\n" + \
               str(self.hotkey) + "\n" + \
               str(self.font)
        with open("records/settings.txt", mode="w", encoding="utf-8") as set_file:
            set_file.write(data)

    def read(self):
        path = os.path.abspath('')
        records_path = os.path.join(path, "records")
        if not os.path.exists(records_path):
            os.mkdir(records_path)
        try:
            with open("records/settings.txt", mode="r", encoding="utf-8") as set_file:
                data = set_file.readlines()
            self.perPage = int(data[0].replace("\n", ""))
            self.automaticFlip = int(data[1].replace("\n", ""))
            self.column = int(data[2].replace("\n", ""))
            self.color = str(data[3].replace("\n", ""))
            self.fontSize = int(data[4].replace("\n", ""))
            self.hotkey = str(data[5].replace("\n", ""))
            self.font = str(data[6].replace("\n", ""))
        except FileNotFoundError:
            self.save()
        except Exception as e:
            print(type(e), e)
            self.perPage = Settings.perPage
            self.automaticFlip = Settings.automaticFlip
            self.column = Settings.column
            self.color = Settings.color
            self.fontSize = Settings.fontSize
            self.hotkey = Settings.hotkey
            self.font = Settings.font
            self.save()


settings = Settings()
settings.read()
