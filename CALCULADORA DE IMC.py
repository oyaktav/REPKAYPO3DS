
def imc(ps, alt):
    #formula imc : peso sobre altura ao quadrado 
    imc = ps / (alt ** 2)
    return imc

ps = float(input("Informe seu peso (em kg): "))
alt = float(input("Informe sua altura (em metros): "))


imc = imc(ps, alt)


print(f"O resultado do seu  imc é: {imc:.2f}")
#".2f" reduz/limita a quant de casa decimal do result
