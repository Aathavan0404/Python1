print("Welcome to the Marks Calculator")
Marks = float(input("Enter your marks: "))
if 0<= Marks <= 100:
  if Marks >= 75:
    print("Result = A")
  elif Marks >= 65:
    print("Result = B")
  elif Marks >+ 50:
    print("Result = C")
  elif Marks >= 35:
    print("Result = S")
  else:
    print("Result = W")
else:
    print("Invalid Marks")
    