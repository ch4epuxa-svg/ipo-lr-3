number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

if number1 == number2 == number3:
    print(f"all number both:{number1}") #  все числа равнозначны 

elif number1 >= number2 and number1 >= number3: # если первое число больше 
    if number1 == number2:
        print(f"larger number:{number1} and {number2},both(1,2)") 
    elif number1 == number3:
        print(f"larger number:{number1} and {number3},both(1,3)")
    else:
        print(f"larger number:{number1}(1)")

elif number2 >= number1 and number2 >= number3:  # если второе число больше 
    if number2 == number3:
        print(f"larger number:{number2} and {number3},both(2,3)")
    else:
        print(f"larger number:{number2}(2)")
else:
    print(f"larger number:{number3}(3)") # если третье число больше 
