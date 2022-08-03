#Python - Capturing User Details Task

print ("Welcome")

first_name = input("first name"+" ")
middle_name = input ("middle name"+ " ")
last_name = input("last name"+"")
full_name: str = input(first_name.capitalize() + "" + middle_name.capitalize()+"" + last_name.capitalize())
print(full_name)

print("Your full name is...")

print("Please enter your age in years")
age = int(input("age"+" "))
print(full_name + " " +"is"+" "+str(age)+" "+"years old")

print("Enter your first line of address")
house_number = int(input('house_number'+" "))
street_name = str(input('street_name'+" "))
print("please enter your postcode")
postcode = input("postcode"+" ")
full_address = str(input(house_number()+" " +street_name()+" "+postcode))
print ("full_address")

print("please add your contact number")
contact_number = int(input())
print(contact_number.isdigit())

print("Please enter your salary in sterling (£) per year")
salary = int(input())
print(salary.isdigit())