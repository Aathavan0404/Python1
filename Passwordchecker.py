while True:
    PW = input("Enter the password: ")
    Needs = ["@", "#"]
    if len(PW) < 8:
        print("Password is weaker. Type another password with at least 8 characters.")
    else:
        for char in PW:
            if char in Needs:
                print("Password is strong.")
                break
        else:
            print("Password is weaker. Type another password with at least 8 characters and include at least one special character (@,#)")
