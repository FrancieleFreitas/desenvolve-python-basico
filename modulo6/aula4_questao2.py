# Exercício 2 

# solicita ao usuário que digite um frase
frase = input("Digite uma frase: ").lower()
#.lower() deixa tudo minusculo

# lista das vogais da frase
vogais = [letra for letra in frase if letra in 'aeiou']
print("Vogais da frase:", vogais)

# lista das consoantes (sem espaços)
consoantes = [letra for letra in frase if letra.isalpha() and letra not in 'aeiou']
print("Consoantes d frase:", consoantes)