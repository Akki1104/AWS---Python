def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def modulous(num1, num2):
    return num1 % num2

print("Please select operations - \n" \
        "1. Add \n" \
        "2. Subtract \n" \
        "3. Multiply \n" \
        "4. Divide \n" \
        "5. Modulous\n")

select = int(input("Select Operation from the above options: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number 2: "))

if select == 1: 
    print(num1,"+",num2,"=",add(num1,num2))

if select == 2: 
    print(num1,"-",num2,"=",subtract(num1,num2))

if select == 3: 
    print(num1,"*",num2,"=",multiply(num1,num2))

if select == 4: 
    print(num1,"/",num2,"=",divide(num1,num2))
    
if select == 5: 
    print(num1,"%",num2,"=",modulous(num1,num2))