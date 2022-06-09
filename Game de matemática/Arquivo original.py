from ast import operator
import random
import time

pergunta = 1
pontos = 0
while pergunta == 1:
    time.sleep(2)
    dificuldade = (int(input('qual é a dificuldade 1,2,3,4\n(1 mais facil, 4 mais dificil): ')))
    print('-'*30)
    time.sleep(2)
    print('você tem {} pontos.'.format(pontos))
    operação = 0
    class calculos:
        def __init__(self) -> None:
            self.valor1 = 0
            self.valor2 = 0
            self.resultado = 0 
            self.operação = 0 
            
        def num1 (self):
            if dificuldade == 1:
                self.valor1 = random.randint(1,10)

            elif dificuldade == 2:
                self.valor1 = random.randint(1,100)
            
            elif dificuldade == 3:
                self.valor1 = random.randint(1,1000)
            
            elif dificuldade == 4:
                self.valor1 = random.randint(1,10000)
        
        def num2 (self):
            if dificuldade == 1:
                self.valor2 = random.randint(1,10)
            
            elif dificuldade == 2:
                self.valor2 = random.randint(1,100)
            
            elif dificuldade == 3:
                self.valor2 = random.randint(1,1000)
            
            elif dificuldade == 4:
                self.valor2 = random.randint(1,10000)

        def opç (self):

            self.operação = random.randint(1,3)
            if self.operação == 1:
                self.operação = '+'
                self.resultado = self.valor1 + self.valor2
            
            elif self.operação == 2:
                self.operação = '-'
                self.resultado = self.valor1 - self.valor2

            elif self.operação == 3:
                self.operação = '*'
                self.resultado = self.valor1 * self.valor2

    calculos = calculos()
    calculos.num1()
    calculos.num2()
    calculos.opç()
    pergunta = 2
    print('-'*30)
    time.sleep(2)
    print('{} {} {} = ?'.format(calculos.valor1,calculos.operação,calculos.valor2))
    
    time.sleep(2)

    resultado_do_usuario = (int(input('Qual é o valor da conta acima: ')))    
    if resultado_do_usuario == calculos.resultado:
        pontos += 1
        print('-'*30)
        time.sleep(2)
        print(f'Parabéns você acertou o resultado.(:\nEssa é a sua pontuação ({pontos}) agora')
        print(f'\nresultado é : {calculos.resultado}')   
    else:
        print('-'*30)
        time.sleep(2)
        pontos -= 1
        print(f'Que pena você errou o resultado.):\nEssa é sua pontuação ({pontos}) agora')
        print(f'\nresultado é: {calculos.resultado}')
    
    print('-'*30)
    time.sleep(2)
    pergunta = (int(input('Se vc quiser continuar dijita 1, mas se quiser parar dijita 2\n')))
    print('-'*30)