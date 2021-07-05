weight = int(input("Please enter you weight:"))
unit = input("(L)bs or (K)gs:")

if unit.upper() == "L":
    new_weight = weight * 0.45
    print(f"You are {new_weight} kilos")
else:
    new_weight = weight / 0.45
    print(f"You are {new_weight} pound")