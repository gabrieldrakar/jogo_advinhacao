

import random
numero = random.randrange(1, 100)
recebimento_de_dados = str(input("você quer jogar um jogo de adivinhação? ")).lower()
if recebimento_de_dados == 'sim' or recebimento_de_dados == 's':
    print('vamos jogar')
    tente = int(input('tente adivinhar o numero escolhendo entre 1 até 100 '))
    try:

        while (tente != numero):
            if (tente > numero):
                tente = int(input('tente novamente, agora um numero menor! '))
            elif (tente < numero):
                tente = int(input('tente novamente, agora um numero maior! '))
        if (tente == numero):
            print('você ganhou!!')
    except ValueError:
        print('você só pode colocar numeros inteiros entre 1 até 100! ')
elif recebimento_de_dados == 'não' or recebimento_de_dados == 'n':
    print('que pena')
else:
    print(('você só pode colocar: , \'não\', \'n\', \'s\' ou \'sim\''))


