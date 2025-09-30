date = float(input("Enter a date in format MM.DD: "))  #ввести дату в формате месяц/год 
month = int(date)

if month in [12, 1, 2]: 
    print("Winter")    # если месяц 12, 1, 2, то выводим зима
elif month in [3, 4, 5]:
    print("Spring")    # если месяц 3, 4, 5, то выводим весна 
elif month in [6, 7, 8]:
    print("Summer")    # если месяц 6, 7, 8, то выводим лето 
elif month in [9, 10, 11]:
    print("Autumn")    # если месяц 9, 10, 11, то выводим осень 
else:
    print("Incorrect date input") # если дата неправильная 
