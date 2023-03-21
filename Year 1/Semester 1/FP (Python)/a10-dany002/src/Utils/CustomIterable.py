
class CustomIterable:
    def __init__(self):
        self.__list = []
        self.__index = -1

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __getitem__(self, item):
        return self.__list[item]

    def __delitem__(self, item):
        del self.__list[item]

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__list):
            raise StopIteration
        return self.__list[self.__index]

    def __len__(self):
        return len(self.__list)

    def append(self, item):
        self.__list.append(item)

    def __eq__(self, other):
        if self.__list == other.__list:
            return True
        return False


