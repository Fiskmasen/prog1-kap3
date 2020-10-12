print("Välj mellan:\n\tolles\n\tcoop\n\tmax")
eat = input("Var vill du äta? ").lower()

if eat == "olles":
    print("Du äter, grattis")
elif eat == "max":
    print("Du sparar inte på studiebidraget")
elif eat == "coop":
    print("Dagens motion!")
    coop = input("2 vitlöksbröd för 20kr? [ja/nej]").lower()

    if coop[0] == "j":
        print("Evigt ätande")
    elif coop[0] == "n":
        print("NÄHÄ!")
    else:
        print("hungrig")

else:
    print("Sadface ")