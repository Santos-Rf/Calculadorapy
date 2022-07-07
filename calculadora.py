def calcular():
    operadores = input('''Escolha qual operação será utilizada:
                    [+] para soma
                    [-] para subtração
                    [*] para multiplicação
                    [/] para divisão
                    ''')

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

    if operadores == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operadores == '-':
        print('{} - {} ='.format(num1, num2))
        print(num1 - num2)
        
    elif operadores == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)
        
    elif operadores == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)
        
    else:
        print('Operador não reconhecido! Por favor, Utilizar um dos quatro operadores especificados!')
     
    novamente()   
def novamente():
    calc_nov = input('Você gostaria de fazer um novo cálculo? Sim [S] ou Não [N]? ')
    
    if calc_nov.upper() == 'S':
        calcular()
        
    elif calc_nov.upper() == 'N':
        print('Espero ter ajudado! Até a próxima! ^.^')
        
    else:
        novamente()

calcular()

