from time import sleep
import random 
import os 

tent = 0
print('\033[36mIrei pensar em um valor entre 0 e 9\nTente adivinhar qual é..\033[m')

pc = random.randint(0, 9)
jogador = int(input('qual seu palpite: '))
tent += 1
os.system('cls')
while True:
    try:
        while jogador > 9 or jogador < 0:
            print('\033[31mError, o valor digitado não está entre 0 e 9'
            '\n\033[33mTente novamente')
            jogador = int(input('\033[34mQual seu palpite: '))

        if jogador > pc:
            print('Menos, tente novamente')
            jogador = int(input('qual seu palpite: '))
            tent += 1
        
        elif jogador < pc:
            print('Mais, tente novamente')
            jogador = int(input('qual seu palpite: '))
            tent += 1

        elif jogador == pc:
            print('Você \033[32mVENCEU\033[m')
            break
        sleep(0.5)
        os.system('cls')
    except ValueError or TypeError:
        print('\033[31mErro na digitação, tente novamente..\033[m')

sleep(1)
print('O numero sorteado foi: ',pc)
print(f'Você obteve a vitoria com {tent} palpites')
sleep(4)
os.system('cls')
