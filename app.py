# Calculadora de Consumo Elétrico Inteligente
# Autor: Crysan Araújo

aparelho = input("Nome do aparelho: ")
potencia = float(input("Potência em Watts (W): "))
horas = float(input("Horas de uso por dia: "))

if potencia <= 0 or horas <= 0 or horas > 24:
    print("Valor inválido!")
else:
    consumo = (potencia * horas * 30) / 1000
    custo = consumo * 0.75
    print(f"\nAparelho: {aparelho}")
    print(f"Consumo estimado: {consumo:.2f} kWh/mês")
    print(f"Custo estimado: R$ {custo:.2f}/mês")