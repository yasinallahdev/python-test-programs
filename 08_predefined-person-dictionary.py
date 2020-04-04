person = {"name": "Ya Sin Supreme Allah", "gender": "male", "age": 20, "address": "3 Walden Square Road, Apt 117, Cambridge MA, 02140", "phone": "617-852-7474"}
field = input("What would you like to know about this person? (name, gender, age, address, or phone number): ")
print(person.get(field,"I can't provide that information about the person."))