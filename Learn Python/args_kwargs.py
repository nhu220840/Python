def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    for value in kwargs.values():
        print(value, end = " ")
    print()

    # using single quote instead of double quote
    # if the key does not in kwargs, it will print 'None' in the screen
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}") 
    else:
        print(f"{kwargs.get('street')}")
    
shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
                street = "123 Fake St.",
                apt = "100",
                city = "Detroit",
                state = "MI",
                zip = "54321")