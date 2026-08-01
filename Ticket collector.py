print("Welcome to Ticket Calculating system")
Age = int(input("Enter your age "))
Price = float
if 0 < Age <= 5:
    print("Ticket is free")
elif 5 < Age <= 18:
    print("Ticket costs Rs.500")
elif 18 < Age <= 60:
    print("Ticket costs Rs.1000")
elif Age > 60:
    print("You have an offer now according to your age")
    Price = 1000 - ((Age - 60)*1000*2/100)
    print("Ticket costs Rs.", Price)
else:
    print("Invalid age, Please Enter the Age Correctly ")