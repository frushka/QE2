import time
cost, sum = int(input('Введите сумму заказа и нажмите Enter->')), int(input('Введите, внесенную сумму и нажмите Enter->'))
s = sum-cost
mylist = [[5000, 0], [2000, 0], [1000, 0], [500, 0], [200, 0], [100, 0], [50, 0], [10, 0], [5, 0], [2, 0], [1, 0]]

for i in range(len(mylist)):
    mylist[i][1]=s//mylist[i][0]
    s = s-mylist[i][0]*mylist[i][1]
rub=' руб: '
num = ' шт.'
buf = False # проверка суммы заказа - равна или меньше внесенной сумме
newlist = []
for i in range(len(mylist)):
    if mylist[i][1]!=0:
        s = str(mylist[i][0]) + rub + str(mylist[i][1]) + num
        newlist.append(s)
        buf = True
        del s
if buf:
    answer=', '.join(newlist)
    print(answer)
else:
    print('Внесенная сумма клиента соответствует сумме заказа - сдача 0 рублей. ')
print('Консоль закроется через 20 секунд...')
time.sleep(20)

