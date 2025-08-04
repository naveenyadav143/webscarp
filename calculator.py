print("Welcome To CLI Calculator")
while(True):
    a = float(input("Enter first numbers: "))
    op = input("select operator (-,+,*,/,**,%):")
    b = float(input("Enter second numbers: "))

    match op:
        case "+" : print(a+b)
        case "-" : print(a-b)
        case "*" : print(a*b)
        case "/" : 
            if b==0:print("/,not divisible by zero") 
            else:print(a/b)
        case "%" : print(a%b)
        case "**" : print(a**b)
        case _ : print("Invalid operator")
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != 'y':
        print("Exiting calculator. Goodbye!")
        break
