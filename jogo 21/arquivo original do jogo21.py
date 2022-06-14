import random
import time

print('Bem-vindo ao jogo 21, as regas são simples')
time.sleep(1)
print('Vai funcionar da seginte forma, se vc quiser mais carta clique em (1), se quiser parar (2).')
time.sleep(1)
print('podendo sair numeros de 1 a 11, podendo repetir esses numeros.\nAgora sabendo das instruções BOM JOGO.')

pontos = 0
continuar = 1
while continuar == 1:
    class jogo_21:
        def __init__(self) -> None:
            self.num = 0
            self.num_adiversario = 0

        def seu_num (self):
            self.num = random.randint(1,11)
        
        def adiversario (self):
            self.num_adiversario = random.randint(16,25)

    jogo_21 = jogo_21()

    pedidas = 1
    pedindo_numero = 1
    while pedindo_numero == 1:
        
        if pedidas == 1:
            jogo_21.seu_num()
            num1 = jogo_21.num
            print('Esse é seu numero: {}'.format(num1))
            resultado = num1
            seu_resultado_final = resultado - 21
            if seu_resultado_final < 0:
                seu_resultado_final = seu_resultado_final * -1

            time.sleep(1)
            print('seu total é: {}.'.format(resultado))
            time.sleep(1)
            pedindo_numero = int(input('vc deseja mais numeros se SIM (1),se não (2):'))
            
            if pedindo_numero == 1:
                pedidas = pedidas + 1
            
            else:
                pedidas = 0

        if pedidas == 2:
            jogo_21.seu_num()
            num2 = jogo_21.num
            print('Esses são seus numeros: {}, {}'.format(num1,num2))
            resultado = num1+num2
            seu_resultado_final = resultado - 21
            
            if seu_resultado_final < 0:
                seu_resultado_final = seu_resultado_final * -1

            time.sleep(1)
            print('seu total é: {}.'.format(resultado))
            time.sleep(1)
            pedindo_numero = int(input('vc deseja mais numeros se SIM (1),se não (2):'))

            if pedindo_numero == 1:
                pedidas = pedidas + 1
            
            else:
                pedidas = 0
        
        if pedidas == 3:
            jogo_21.seu_num()
            num3 = jogo_21.num
            print('Esses são seus numeros: {},{},{}'.format(num1,num2,num3))
            resultado = num1+num2+num3
            seu_resultado_final = resultado - 21

            if seu_resultado_final < 0:
                seu_resultado_final = seu_resultado_final * -1

            time.sleep(1)
            print('seu total é: {}.'.format(resultado))
            time.sleep(1)
            pedindo_numero = int(input('vc deseja mais numeros se SIM (1),se não (2):'))

            if pedindo_numero == 1:
                pedidas = pedidas + 1
            
            else:
                pedidas = 0

        if pedidas == 4:
            jogo_21.seu_num()
            num4 = jogo_21.num
            print('Esses são seus numeros: {},{},{},{}'.format(num1,num2,num3,num4))
            resultado = num1+num2+num3+num4

            seu_resultado_final = resultado - 21
            if seu_resultado_final < 0:
                seu_resultado_final = seu_resultado_final * -1
            
            time.sleep(1)
            print('seu total é: {}.'.format(resultado))
            time.sleep(1)
            pedindo_numero = int(input('vc deseja mais numeros se SIM (1),se não (2):'))

            if pedindo_numero == 1:
                pedidas = pedidas + 1
            
            else:
                pedidas = 0

        if pedidas == 5:
            jogo_21.seu_num()
            num5 = jogo_21.num
            print('Esses são seus numeros: {},{},{},{},{}'.format(num1,num2,num3,num4,num5))
            resultado = num1+num2+num3+num4+num5
            seu_resultado_final = resultado - 21
                
            if seu_resultado_final < 0:
                seu_resultado_final = seu_resultado_final * -1
            
            time.sleep(1)
            print('seu total é: {}.'.format(resultado))
            pedindo_numero = 0
            print('Esse é o maximo de pedidas de numeros.')

    jogo_21.adiversario()
    
    resultado_final_do_adiversario = jogo_21.num_adiversario - 21
    

    if resultado_final_do_adiversario < 0:
        resultado_final_do_adiversario = resultado_final_do_adiversario * -1

    print('Em comparação ao seu adversário vc...')
    time.sleep(2)
    if resultado_final_do_adiversario > seu_resultado_final:
        pontos += 1
        time.sleep(1)
        print('Parabéns, vc ganhou :)')
        time.sleep(1)
        print('seus pontos: {}'.format(pontos))
        print('numero do adversário: {}.'.format(jogo_21.num_adiversario))
        print('seu numero: {}'.format(resultado))
    
    if resultado_final_do_adiversario < seu_resultado_final:
        pontos -= 1
        time.sleep(1)
        print('Que pena vc perdeu :(')
        time.sleep(1)
        print('seus pontos: {}'.format(pontos))
        print('numero do adversário: {}.'.format(jogo_21.num_adiversario))
        print('seu numero: {}'.format(resultado))

    if resultado_final_do_adiversario == seu_resultado_final:
        time.sleep(1)
        print('Vc empatou')
        time.sleep(1)
        print('seus pontos: {}'.format(pontos))
        print('numero do adversário: {}'.format(jogo_21.num_adiversario))
        print('seu numero: {}'.format(resultado))
    
    time.sleep(1)
    continuar = int(input('vc deseja continuar:\nSIM(1), NÃO(2).'))