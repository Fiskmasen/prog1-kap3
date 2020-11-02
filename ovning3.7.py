import math
r = float (input("Cirkelns Radie Är:" ))
if  r <= 0: #if-satser använder man när man ska välja mellan olika vägar i ett program
    raise Exception("Tyvärr, inga negativa radier tillåts")
else: 
    a = math.pi*r**2
    o = 2*math.pi*r

print(f"Cirkelns Area: {a:.3f}")
print(f"Cirkelns Omkrets: {o:.3f}")