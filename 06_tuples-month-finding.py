months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
birthday = input("Enter your birthday (Format: DD-MM-YYYY): ")
birthMonth = months[int(birthday[3:5])-1]
print("You were born in", birthMonth)