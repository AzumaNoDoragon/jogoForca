import random, re, os
partesForca = [
    """
     ___________
    |           |
    |
    |
    |
    |
    |
    |
    """,
    """
     ___________
    |           |
    |           O
    |
    |
    |
    |
    |
    """,
    """
     ___________
    |           |
    |           O
    |           |
    |
    |
    |
    |
    """,
    """
     ___________
    |           |
    |           O
    |           |\\
    |
    |
    |
    |
    """,
    """
     ___________
    |           |
    |           O
    |          /|\\
    |
    |
    |
    |
    """,
    """
     ___________
    |           |
    |           O
    |          /|\\
    |          /
    |
    |
    |
    """,
    """
     ___________
    |           |
    |           O
    |          /|\\
    |          / \\
    |
    |
    |
    """,
    """
     ___________
    |           |
    |           X
    |          /|\\
    |          / \\
    |
    |
    |
    """
    ]
num = random.randrange(1, 110)
erro = 0
letras_erradas = []

with open('palavras.txt', 'r', encoding='utf-8') as file:
    palavra = file.readlines()
    linha = palavra[num].strip().split(" - ", 1)
    palavra = linha[0].lower()
    tema = linha[1]

print(f'Palavra: {palavra}, Tema: {tema}')
letras_adivinhadas = set()
letras_erradas = set()

while erro < len(partesForca) - 1:
    os.system('cls')
    print(tema, partesForca[erro])
    for letra in palavra:
        if letra in letras_adivinhadas or letra == ' ':
            print(letra, end=' ')
        else:
            print('_', end=' ')

    if letras_erradas:
        print("Letras erradas:", ', '.join(letras_erradas))
    
    entrada = input("\nDigite uma letra: ").lower()

    if len(entrada) != 1 or not entrada.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue
    
    if entrada in palavra:
        letras_adivinhadas.add(entrada)
    else:
        if entrada not in letras_erradas:  # Adiciona a letra errada apenas se ainda não estiver na lista
            letras_erradas.add(entrada)
        erro += 1
    
    if all(letra in letras_adivinhadas or letra == ' ' for letra in palavra):
        os.system('cls')
        print(f"Parabéns! Você adivinhou a palavra '{palavra}'!")
        break

if erro == len(partesForca) - 1:
    os.system('cls')
    print(partesForca[erro])
    print(f"Você perdeu! A palavra era '{palavra}'")