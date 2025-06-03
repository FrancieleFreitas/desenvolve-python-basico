# Exercício 1

# todos números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]
print("Números pares entre 20 e 50:", pares)

# todos números ímpares entre 20 e 50
impares = [x for x in range(20, 51) if x % 2 != 0]
print("Números ímpares entre 20 e 50:", impares)

# todos os números entre 1 e 10 elevados ao quadrado 
quadrados = [x**2 for x in range(1, 11)]
print("Quadrados de 1 a 10:", quadrados)

# todos os números com 1 casa decimal entre 0 e 1
# range(10) gera os números de 0 até 9
# dividi por 10 para obter valores decimais
decimais = [x / 10 for x in range(10)]
print("Números decimais de 0.0 a 0.9:", decimais)


