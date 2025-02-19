
def celpfah(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = float(input("Informe a temperatura em graus celsius : "))


fahrenheit = celpfah(celsius)


print(f"A temperatura informada em Fahrenheit é: {fahrenheit:.2f}")