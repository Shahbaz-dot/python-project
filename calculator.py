# the calculater for addition, subtrction, multipliction, division by two number

a = float(input("Enter first number :"))
b = float(input("Enter second number :"))

print("choose operation: +  -  *  / ")
op = input("Enter operator : ")

if op == '+':
    print("result : ", a + b)
elif op == '-':
    print("result : ", a - b)
elif op == '*' :
    print("result :", a * b)

elif op == '**':
    print("result :", a ** b)  # for squaree root
elif op == '/':
    if b != 0:
        print("result :", a / b)
    
    else :
        print("cannot divide by zero!")
    
else : 
    print(" Invalid operator")



# 2 CALCULATOR


a = 7
b = 5
print("enter the number", a + b)
print("enter the number", a - b)
print("enter the number", a * b)
print("enter the number", a / b)
print("enter the number", a % b)