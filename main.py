print("Bienvenido este programa calcula tu IMC (indice de masa corporal)") 
print()

weight = float(input("Ingresa tu peso en kg: "))
heigth = float(input("Ingresa tu altura en metros: "))

bmi = weight / (heigth ** 2)

print()
print("Tu indice de masa corporal (IMC) es :", round(bmi,2))