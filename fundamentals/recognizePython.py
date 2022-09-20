num1 = 42  #variable declaration, number
num2 = 2.3  #variable declaration, float
boolean = True #variable declaration, boolean
string = 'Hello World'  #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list, initalize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana')  #variable declaration, tuple, initialize
print(type(fruit))  #log statement, type check
print(pizza_toppings[1])    #log statement list access value
pizza_toppings.append('Mushrooms')  #list add value
print(person['name']) #log statement dictionary access value
person['name'] = 'George'  #dictionary change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) #tuple access value

if num1 > 45:                   #conditional if
    print("It's greater")           #log statement  
else:                           #conditional else   
    print("It's lower")         #log statement

if len(string) < 5:             #conditional if 
    print("It's a short word!") #logstatemetn
elif len(string) > 15:              #conditional else if
    print("It's a long word!")      #log statment
else:                               #conditional else
    print("Just right!")

for x in range(5):          #for loop start 0 stop 5
    print(x)
for x in range(2,5):        #for loop start 2 stop 5
    print(x)
for x in range(2,10,3):     #for loop start 2 stop 10 increment by 3
    print(x)
x = 0                   #variable declaration
while(x < 5):       #while loop stop when x<5   
    print(x)
    x += 1          #increment x by 1

pizza_toppings.pop()    #list delete value  
pizza_toppings.pop(1)   #list delete value @ pos 1

print(person)           #log statement
person.pop('eye_color')     #dictionary delete value  
print(person)           #log statement

for topping in pizza_toppings:  #for loop start pizza_toppings[0]
    if topping == 'Pepperoni':  #conditional if
        continue                #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives':     #conditional if
        break               #for loop break

def print_hello_ten_times():    #function declaration
    for num in range(10):       #for loop 0-10  
        print('Hello')          #log statement

print_hello_ten_times()         #function call

def print_hello_x_times(x): #function declaration parameter x
    for num in range(x):    #for loop 0-parameter x
        print('Hello')      #log statement

print_hello_x_times(4)      #call function arg 4

def print_hello_x_or_ten_times(x = 10): #function delcaration parameter x=10
    for num in range(x):            #for loop 0-10
        print('Hello')          #log statement

print_hello_x_or_ten_times()        #function call
print_hello_x_or_ten_times(4)       # function call w argument


"""
Bonus section
"""

# print(num3)       name error num 3 not defined
# num3 = 72         variable declaration    
# fruit[0] = 'cranberry'    type error tuple does not support item assignment
# print(person['favorite_team'])    key error favorite team
# print(pizza_toppings[7])          index error out of range
#   print(boolean)          indentation error
# fruit.append('raspberry') attribute error
# fruit.pop(1)              attribute error