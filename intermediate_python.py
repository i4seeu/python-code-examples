import pdb

def add(a, b):
    # pdb.set_trace()
    return a + b

print(add(2, 3))

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

mydog = Dog("Rex")
print(mydog.bark())