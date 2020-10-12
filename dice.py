import random 

choice = "j"

while choice == "j":

    roll = random.randint(1, 6)
    print(f"du slår {roll:1}")

    choice = input("Vill du rulla en tärning[J/N]: ").lower()[0]
    print("Hejdå")