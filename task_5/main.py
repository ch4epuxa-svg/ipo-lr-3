x = float(input("Enter x: "))
y = float(input("Enter y: "))

if x == 0 and y == 0:
    print("Origin") 
elif x == 0:
    print("Abscissa") # ось абсцисс
elif y == 0:
    print("Ordinate") # ось ординат 

elif x > 0 and y > 0:
    print("1 quarter") # если x, y положительны, то первая четверть 
elif x<0 and y>0:
    print("2 quarter") # если x отрицательный, y положительный , то вторая четверть 
elif x<0 and y<0:
    print("3 quarter") # если x, y отрицательны, то третья четверть 
else:
    print("4 quarter") # оставшийся вариант четвертая четверть 
