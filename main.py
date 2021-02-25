class Text:
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
    def __init__(self, name):
        self.name = name
        self.obj = []

    def __str__(self):
        for i in self.obj:
            return str(i)

    def add_obj(self, obj):
        self.obj.append(obj)

    def del_obj(self, obj):
        self.obj.remove()

    def getBlockName(self):
        return self.name


class Engine:
    def __init__(self):
        self.globalBlock = []
        self.listFunc = {
            'addBlock': self.addBlock
        }

    def func(self, nameFunc):
        return self.listFunc[nameFunc]

    def addBlock(self, name):
        self.globalBlock.append(Block(name))

    def printBlock(self):
        for block in self.globalBlock:
            print("[] " + block.getBlockName())


def main():
    toDo = Engine()
    toDo.printBlock()
    toDo.func('addBlock')('asdasdasd')
    toDo.addBlock('ASDADS')
    toDo.printBlock()


if __name__ == '__main__':
    main()
