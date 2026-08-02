x = "Awesome"  #global variable works anywhere in the program
print("Python is " + x)

def myfunc():
    print("Python is", x)
myfunc()







def myfunc():
    x = "great" #local variable works only inside the function
    print("Python is " + x)
myfunc()
