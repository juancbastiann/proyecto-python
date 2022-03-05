#EJEMPLO 1
x = 5

if x > 4:
    print("¡La condición era verdadera!")

#EJEMPLO 2
y = (10 - 45)
x = 20
a = 40

if y >= 10:
    print("continuemos")
    if x == 10:
        print("incorrecto")
    elif x == 20:
        print("continuemos")
        if a > 41:
            print("incorrecto")
        elif a > 10:
            print("las condiciones son correctas")
elif y < 10:
    print("las condiciones son incorrectas")

#EJEMPLO 3
x = 34
if x %  2 == 0:
    if x > 10:
        print("Este número es par y es mayor que 10")
    else:
        print("Este número es par, pero no mayor 10")
else:
    print ("El número no es par.")