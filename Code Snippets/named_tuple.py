from collections import namedtuple

Person = namedtuple("Person", "age")

John = Person('John', 56)
Kate = Person('Kate', 42)

print(John)

print(Kate.name)
