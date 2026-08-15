Temp = []
Input = ""
while Input != "exit": #!means that the loop will continue until the user types "exit"
    T = float(input("Enter temperature value in Celsius or Fahrenheit: "))
    Unit = input("Enter the Unit (Celsius or Fahrenheit): ")
    print()
    if Unit == "C" or Unit == "c":
        F = (T * 9/5) + 32
        print(f"Temperature in Fahrenheit: {F}")
        Temp.append((F, Unit))
    elif Unit == "F" or Unit == "f":
        C = (T - 32) * 5/9
        print(f"Temperature in Celsius: {C}")
        Temp.append((C, Unit))
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit ")
    Input = input("Type 'exit' to quit or press Enter to continue: ")         
print(Temp)



    
    