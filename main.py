while True:

    print("\n1. Fixed \n\n2. Provided")
    c = int(input("\n\nChoose one: "))
    
    if c == 1:
        import fixed 
        break

    elif c == 2:
        import provided
        break
    
    else:
        print("Invalid Input...")