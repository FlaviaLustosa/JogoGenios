#!/usr/bin/env python
# coding: utf-8
# In[ ]:

import random  # necessário para utilizar o módulo random
from IPython.display import clear_output # necessário para limpar o display
import time # necessário para contar o tempo
from os import system, name
import os

botao = [] # cria a lista de entrada do usuario
fim_jogo =0 # cria variavel que verifica se a pessoa acertou ou errou a seguencia de numeros
num_aleatorio =[] # cria lista de numeros randomicos


    
def def_num_aleatorio(num_aleatorio):
    '''Função cria um numero aleatorio de 1 a 4 e adiciona esse numero a uma lista
    Argumentos: num_aleatorio- list
    Retorno: o argumento de entrada adicionando um elemento
    Exemplo: def_num_aleatorio([1,2]) 
             retorno [1,2,3]'''
    num = random.sample(range(1,5), k=1)
    num_aleatorio += num
    #num_aleatorio.append(num)
  
    return num_aleatorio

def def_entrada_usuario(num_aleatorio,botao):
    '''Função limpa a lista botao. Solicita entrada de usuario enquanto não for igual
    a quantidade de elemento na lista de numeros randomicos.
    Argumentos: num_aleatorio- list
                botao - list
    Retorno: a lista botao com todos os numeros digitados pelo usuario
    Exemplo: def_num_aleatorio([1,2],[1]) 
             retorno [1,2,1]'''
    botao.clear()
    for i in range (len(num_aleatorio)) :
        test_botao = botao.append(int(input()))
 
    return botao

def def_verifica (botao,num_aleatorio):
    '''Função verifica se os numeros de entrada do usuario sao igual aos gerados de forma aleatoria.
    Argumentos: botao -list
                num_aleatorio- list
    Retorno: a lista botao com todos os numeros digitados pelo usuario
    Exemplo: def_num_aleatorio([1,2],[1]) 
             retorno [1,2,1]'''
    for item in num_aleatorio:
        if botao == num_aleatorio:
            fim_jogo=0 
        else:
            print ('voce perdeu', botao,num_aleatorio)
            fim_jogo=1
            return fim_jogo
    return fim_jogo
            
print('''Bem vindo, ao Jogo Genios! 

     OBJETIVO: Repetir corretamente a sequência de números, cada vez mais longa.
     
    O jogo começou: digite o numero mostrado na tela, pressionando o numero de 1-4 e prescione enter. 
    GENIUS repetirá o primeiro número e vai acrescentar mais um. 
    Repita então esses dois números, pressionando o primeiro numero de 1-4 e prescione enter e depois o segundo numero e enter. 
    Genius repetirá os dois números e, na mesma sequência, aumentará mais um. 
    Continue desta forma, enquanto você conseguir repetir cada sequência de números corretamente.''')

print('Podemos comecar? S/N')
start = input()
if start == 'S':
    print('Ok,vamos começar!')
elif start == 'N':
    print('Ok, Jogamos depois!')
else :
    print( 'Favor digitar s para se SIM! Voce deseja comecar a jogar ou N para se não, você não quer jogar agora!')
    
while fim_jogo == 0 and start == 'S':
    print(def_num_aleatorio(num_aleatorio))
    time.sleep(5)
    clear = lambda: os.system('cls')
    clear()
    print('Agora é a sua vez')
    botao = def_entrada_usuario(num_aleatorio,botao)
    fim_jogo= def_verifica(botao,num_aleatorio)    