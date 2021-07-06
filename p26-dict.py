customer = {

    "Name" : "Dhruvin Soni",
    "Age" : 30,
    "is_verified" : True,
 }
print(customer["Name"])
print(customer.get("birthdate", "30th Dec 1997"))

customer["Job"] = "SRE"
print(customer["Job"])