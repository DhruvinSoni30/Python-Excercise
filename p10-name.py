name = raw_input("Enter your name:")
length = len(name)

if (length < 3):
    print ("Name must be >3 characters long")
elif (length > 50):
    print ("Name can not be >50 characters long")
else:
    print ("Name is perfect")
