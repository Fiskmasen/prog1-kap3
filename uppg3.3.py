p = int(input("Hur många poäng har eleven? "))
if p < 25:
    print("Du har F, du är misslyckad.")
elif p < 30:
    print("Du har ett E, du har godkänt iallafall...")
elif p < 35:
    print("Du har ett D.")
elif p < 40:
    print("Du har ett C.")
elif p < 45:
    print("Du har ett B, grattis.")
else:
    if p >= 45:
        print("Grattis! Du har A! Happy Face")