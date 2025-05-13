#Entrada de dados
valor = int(input())

#Lista com os valores das notas possíveis
notas = [100, 50, 20, 10, 5, 2, 1]

#Cálculo e saída formatada
for nota in notas:
    qtd = valor // nota
    print(f"{qtd} nota(s) de R$ {nota},00")
    valor %= nota