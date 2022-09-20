def fizz_buzz(num):
    output = []
    for i in range(1,num+1):
        if i%5==0 and i%3==0:
            output.append("fizzbuzz")
        elif i%5==0:
            output.append("buzz")
        elif i%3==0:
            output.append("fizz")
        else:
            output.append(i)
    return output

print(fizz_buzz(15))