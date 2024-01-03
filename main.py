import time

#variaveis

fomeMax = 10
felicidadeMax = 10
energiaMax = 10

fome = 5
felicidade = 5
energia = 5

###################################################

# opcoes
def opcoes():
    print('\n')
    print('1- Alimentar')
    print('2- Brincar')
    print('3- Dormir')
    print('4- Status')

###################################################

#status

def status():
    divisoria()

    print('\nFome: '+ str(fome))
    
    print('Felicidade: '+ str(felicidade))
    
    print('Energia: '+ str(energia) + '\n')

    divisoria()

    input('Pressione ENTER para continuar...')


###################################################
def divisoria():
    print('###################################################')

###################################################

#selecionar opcao
    
def selecao():
    global fome
    global felicidade
    global energia

    
    opcao = int(input('\nEscolha uma opção: '))

####################

#funcao realizando ação
    
    def acaoWait(textoWait, textoFinal):
        print('\n')
        for i in range(4):
            print(textoWait)

            textoWait += '.'
            time.sleep(1)
        
        print(textoFinal+'\n')
        input('Pressione ENTER para continuar...')
    

####################   
    #Alimentação
    
    if opcao == 1:

        if fome != 0:
            fome -= 1
            acaoWait('Comendo', f'Acabou de comer! (fome = {fome})')


        else:
            print('\nNão está com fome!\n')
            input('Pressione ENTER para continuar...')

 ####################               
    #Brincar
            
    elif opcao == 2:

        if felicidade < felicidadeMax:
            felicidade += 1
            acaoWait('Brincando', f'Brincadeira acabou! (felicidade={felicidade})')

            felicidade += 1

        else:
            print('\nNão estou com vontade de brincar!!\n')

####################    
    #Dormir
        
    elif opcao == 3:

        if energia < energiaMax:

            acaoWait('Dormindo', f'Dormiu! (energia:{energia})')
            energia += 1

        else:
            print('\nNão estou com sono!!\n')

    elif opcao == 4:
        status()

    else:
        print('Opção inválida')
        

###################################################

#inicial
def inicial():
    print('\nBem vindo ao Tamagotchi')
    print('O que deseja fazer?')
    opcoes()
    selecao()

###################################################
    
inicial()
while True:
    opcoes()
    selecao()