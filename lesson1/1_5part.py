class MyObject:
    def __init__(self):
        self.__attribute = 0   #приватный атрибут

    @property
    def attribute(self):
        return self.attribute

    @attribute.setter
    def attribute(self, value):
        if value < 100:
            self.__attribute = value

