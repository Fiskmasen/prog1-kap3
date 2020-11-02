t = float(input("Temp? "))
if t < 18:
    print("Det är kallt")
    print("Sätt på värmen")
    if t <= -30:
            print("Grattis, du är nu en isbit!")
    else:
        if t < 12:
            print("Sätt på jackan")
        if t <= -10:
            print("Det är svinkallt")
            print("Sätt på en till jacka")

else:
    print("Det är varmt")
    if t > 40:
        print("Du är redan död!")
    elif t >= 22:
        print("Stäng av värmen")
    elif t > 30:
        print("Det är Öken hett")
   
    
print(f"Det är {t:.1f} grader")