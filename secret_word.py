import os

os.system('cls')
palavra_secreta = 'constitucional'
letras_acertadas = ''
numero_tentativas = 0
numero_erros = 0

while True:
    letra = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra
    else:
        numero_erros += 1
    
    if numero_erros == 6:
        print('VOCÊ PERDEU!')
        numero_tentativas = 0
        palavra_formada = ''
        numero_erros = 0
        break
    
    palavra_formada = ''
    for letras_secretas in palavra_secreta:
        if letras_secretas in letras_acertadas:
            palavra_formada += letras_secretas
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS! VOCÊ GANHOU!')
        print(f'A palavra era: {palavra_formada}')
        print(f'Número de tentativas: {numero_tentativas}')
        break



