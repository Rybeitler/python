#countdown
def countdown(num):
    ls = []
    for i in range(num,-1,-1):
        ls.append(i)
    return ls

print(countdown(5))

#print and return

def print_and_return(ls):
    if type(ls)==list:
        print(ls[0])
        return ls[len(ls)-1]
    else:
        print("not a list!")

print_and_return(1)

#first plus lenght

def first_plus_length(ls):
    if type(ls)==list:
        return ls[0] + len(ls)
    else:
        print("not a list!")

print(first_plus_length([1,2,3,4,5]))

#values greater than second

def values_greater_than_second(ls):
    count =0
    newLs=[]
    if len(ls) > 2:
        for x in ls:
            if x > ls[1]:
                newLs.append(x)
                count+=1
        print(count)
        return(newLs)
    else:
        return False

print(values_greater_than_second([5,2,3,2,1,4]))

#this length, that value

def lenght_and_value(a,b):
    ls =[]
    for i in range(a):
        ls.append(b)
    return ls
print(lenght_and_value(6,2))