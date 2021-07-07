try:
    age = int(input("Age:"))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Please enter valid age")
