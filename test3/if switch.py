name = '1exiaoqiang'
if len(name)>=12:
    print('你的名字是:')
    print(name[0:len(name)])
elif name[0:2] == 'he':
    print('此人姓何')
else:
    print('该名字过短')
    print('wrong name')

count = 1
while count<=100:
    print(count)
    count+=10

m = 100
n = 40
print('1 到 %d 之和为 %d %d'%(n, m, count))

lis = [1,2,3,4,5]
for i in lis:
    print(i)
    if(type(i) == int and i<4):
        print('%d是数字' %i)
        continue
    print("%d是字符串" %i)


