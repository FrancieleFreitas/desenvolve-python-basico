#Produto1
nome1 = input("Digite o nome do produto 1: ")
preco1 = float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

#Produto2
nome2 = input("Digite o nome do produto 2: ")
preco2 = float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

#Produto3
nome3 = input("Digite o nome do produto 3: ")
preco3 = float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

#Cálculo total
total = (preco1 * quantidade1) + (preco2 * quantidade2) + (preco3 * quantidade3)

#Saída formatada com separador de milhar e duas casas decimais
print(f"Total: R${total:,.2f}".replace(",","x").replace(".",",").replace("x","."))