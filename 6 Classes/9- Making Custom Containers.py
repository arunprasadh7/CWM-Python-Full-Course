# 9- Making Custom Containers

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(),0)

    def __setitem(self,tag,count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

t1 = TagCloud()
t1.add('Python')
t1.add('python')
t1.add('python')
print(t1.tags)

print(t1['python'])

#setting number of given tag
# t1['python']  = 10

print(len(t1))
