#print integers 0-150
for i in range(151):
    print(i)
#print multiples of 5, from 5-1000
for i in range(5,1001,5):
    print(i)
#print integers 1-100, multiples of 5 are rpl w "coding", 10 with "coding Dojo"
for i in range(1,101):
    if i%10==0:
        print("coding dojo")
    elif i%5 ==0:
        print("coding")
    else:
        print(i)
#add odd integers from 0-500,000
x=0
for i in range(500001):
    x+=i
print(x)
#print positive nums starting @ 2018 counting down
for i in range(2018, 0, -4):
    print(i)
#set 3 vars lowNum, highNum mult, count from low to high by multi
lowNum = 20
highNum = 1000
mult =5

for i in range(lowNum, highNum+1):
    if i % mult ==0:
        print(i)
