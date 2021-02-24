from colorama import Fore, Back, Style


class Text:

    # TODO: Истрия изменений

    def __init__(self, text):
        self.main_text = text
        self.link = None

    def __str__(self):
        return str(self.main_text)

    def rename(self, text):
        self.main_text = text

    def add_link(self, link):
        self.link = link


class List:
    def __init__(self):
        self.list = []

    def __str__(self):
        return self.list

    def add_point(self, obj):
        self.list.append(obj)

    def del_point(self, obj):
        self.list.remove(obj)


class Block:
    def __init__(self, main_name):
        self.main_name = main_name
        self.obj = []

    def __str__(self):
        for i in self.obj:
            return str(i)

    def add_obj(self, obj):
        self.obj.append(obj)

    def del_obj(self, obj):
        self.obj.remove()


def main():
    foo = Block('College')
    foo.add_obj(Text('todo1'))
    print(foo)


if __name__ == '__main__':
    main()
