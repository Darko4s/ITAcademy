visina = float(input("Unesite vasu visinu "))
tezina = int(input("Unesite vasu tezinu "))
bmi = tezina/visina**2

if bmi <= 18.5:
    print("Vas BMI iznosi: " + str(bmi) + "Vi ste mrzavi.")
elif bmi >= 18.5 and bmi < 25.0:
    print("Vas BMI iznosi:" + str(bmi) + "Vi ste taman :D")
elif bmi >= 25.0 and bmi < 30.0:
    print("Vas BMI iznosi:" + str(bmi) + "Vi ste gojazni ")
elif bmi >= 30.0:
    print("Vas BMI iznosi:" + str(bmi) + "TERETANA!")
else:
    print("Unijeli ste pogresne podatke." + str(bmi))
