# Exercício 3

# lista com as horas trabalhadas por cada funcionário
horas_trabalhadas = [40, 37, 45, 40, 40, 48]

# valor pago por hora de trabalho
valor_hora = 25

# lista de pagamentos calculada com compreensão de listas
# se trabalhou ate 40h paga normal, se passou de 40h calcula horas extras com 50% a mais
pagamentos = [
    (h * valor_hora) if h <= 40 
    else (40 * valor_hora + (h - 40) * valor_hora * 1.5)
    for h in horas_trabalhadas
]

# mostra o resultado
print("Pagamentos:", pagamentos)
