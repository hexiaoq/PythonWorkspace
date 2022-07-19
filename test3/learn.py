name = 'hexiaoqiang'
print(name[0:11])
print(name*3)
print(name+' is a hero')
print(r'he\nxiaoq')
print(name[10])

list = ['list','game of throne j',12.3,11,13j]
print(list[1])
list[1][0:len(list[1])]
a=list[1]
print(a)
list[1] = len(list[0])
print(list)
print(type(a))
print(isinstance(a,int))
if isinstance(a, str):
   print(a)
   print('这是正确的')
else:
   print(1)
