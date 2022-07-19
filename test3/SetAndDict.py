set1 = {'hxq','hxq',1,2,3,3.0}
set1.add('hhh')
print(set1)

dict1 = {1:'hxq', 2:'wr', 3:'ljy', 4:'fao', 'sb':'wy'}
print(dict1[1], dict1['sb'])

num = 'q'
print(ord(num))

mul = [i for i in range(100) if i % 5 == 0]
print(mul)

class Person:
    name = 'hxq'
    age = 23
    salary = 10000

    def my_salry(self):
        print('你的月收入为:%d' %self.salary)

hxq = Person()
print(hxq.age)
hxq.my_salry()

