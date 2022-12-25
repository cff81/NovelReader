from Reader import *


class Novel:
    def __init__(self, book: str, index: int, reader: Reader):
        self.name = Novel.get_book_name(book)
        self.path = book
        self.reader = reader
        with open(book, encoding="utf-8", errors="replace") as NOVEL:
            self.content = NOVEL.read().replace(" ", "").replace("\n", "  ")
        self.length = len(self.content) - 1
        self.index = index
        self.on_show = ""
        self.set_text()

    def get_page(self):
        """根据self.index确定self.on_show"""
        if self.index > self.length:
            self.index = self.length
            return "已经是最后一页"
        index = self.index + settings.perPage
        index2 = index if index < self.length else self.length
        result = self.content[self.index: index2]
        if settings.column > 1:
            if settings.column == 2:
                enter = int(settings.perPage / 2)
                result = "{0}\n{1}".format(result[:enter], result[enter:])
            else:
                enter1 = int(settings.perPage / 3)
                enter2 = enter1 * 2
                result = "{0}\n{1}\n{2}".format(result[:enter1],
                                                result[enter1:enter2],
                                                result[enter2:])
        return result

    def last_page(self):
        if self.index >= settings.perPage:
            self.index -= settings.perPage
            self.set_text()

        elif self.index == 0:
            pass
        else:
            self.index = 0
            self.set_text()

    def next_page(self):
        if self.index <= self.length:
            self.index += settings.perPage
            self.set_text()

    def set_text(self):
        self.on_show = self.get_page()
        self.reader.setText(self.on_show)

    @staticmethod
    def get_book_name(book_path: str):
        name = book_path
        if name.count('\\') != 0:
            name = name[name.rfind('\\') + 1:name.find('.txt')]
        elif name.count('/') != 0:
            name = name[name.rfind('/') + 1:name.find('.txt')]
        return name
