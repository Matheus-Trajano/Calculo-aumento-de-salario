salario = float(input("digite seu salário atual: "))

if salario <= 500:
    aumento = salario * 0.25
    print("seu aumento será de 25%")
    print(f" seu salário com aumento será: R${aumento + salario}")

elif salario <= 1000:
    aumento = salario * 0.20
    print("seu aumento será de 20%")
    print(f" seu salário com aumento será: R${aumento + salario}")

elif salario <= 1500:
    aumento = salario * 0.15
    print("seu aumento será de 15%")
    print(f" seu salário com aumento será: R${aumento + salario}")

elif salario <= 2000:
    aumento = salario * 0.10
    print("seu aumento será de 10%")
    print(f" seu salário com aumento será: R${aumento + salario}")

else:
    aumento = 0
    print("sem aumento")

tempo = float(input(
    "digite quanto tempo de serviço você tem na empresa( caso seja um valor quebrado, como por exemplo um ano e meio, "
    "utilize 1.5 ):"))
serv = tempo * 12

if serv < 12:
    bonus = 0
    print("sem bônus")

elif serv <= 36:
    bonus = 100
    print(f"seu bônus será de: R${bonus}")

elif serv <= 72:
    bonus = 200
    print(f"seu bônus será de: R${bonus}")

elif serv <= 120:
    bonus = 300
    print(f"seu bônus será de: R${bonus}")

else:
    bonus = 500
    print(f"seu bônus será de: R${bonus}")

print(f"seu ganho total será de: R${salario + aumento + bonus}")
