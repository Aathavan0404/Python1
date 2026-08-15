while True:
    Name = input("Enter your name: ")
    if Name[0].islower():
        print("Your name is in lowercase.")     
        print("First letter should be in Capital. Reenter the Name")
    else:
        break
