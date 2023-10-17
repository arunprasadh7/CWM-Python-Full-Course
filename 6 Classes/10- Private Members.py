# 10- Private Members- prefix with __ double underscore


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

t1 = TagCloud()
t1.add('Python')
t1.add('python')
t1.add('python')

# print(t1.__tags['PYTHON'])
print(t1.__dict__)
print(t1._TagCloud__tags)