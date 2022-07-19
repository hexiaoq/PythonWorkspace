def add1(a, b):
    c = a + b
    return c


result = add1(10,20)
print(result)


class A:
    def __init__(self, name, age, loc):
        self.name = name
        self.age = age
        self.loc = loc



    @staticmethod
    def where():
        print("我在新余")

class B(A):
    def __init__(self, salary, workTime, name, age, loc):
        super().__init__(name, age, loc)
        self.salary = salary
        self.workTime = workTime


person = A("HXQ", 22, "新余市")
print(person.age)
person.where()
person2 = B(50000,10,3000)
person2.age = 20
print(person2.salary)
print(person2.age)