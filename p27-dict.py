phone = input("Please enter the phone number:")
number = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for char in phone:
    output += number.get(char, "!") + " "
print(output)