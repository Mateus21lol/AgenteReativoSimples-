# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:14:11 2020

@author: Mateus Nobre Silva Almeida
"""
#imports
from random import randint
import random
import matplotlib.pyplot as plt
import numpy as np

#Variaveis Globais
estadoUn = randint(0,1)
estadoDeux = randint(0,1)
#estado = 0 limpo
#estado = 1 sujo
Direita  = "Direita"
Esquerda = "Esquerda"
Mapa = "ED"
Estados = [1, 1]
estadoDireita = 5
estadoEsquerda = 5

#funções
def AgenteAspiradorDePoReativo():
    global flag
    global Estados
    MapaLocalizacao = random.choice(Mapa)
    if(MapaLocalizacao == "D"):
        estadoDireita = limpaDireita() 
        estadoEsquerda = limpaEsquerda()
    if(MapaLocalizacao == "E"):
        estadoEsquerda = limpaEsquerda()
        estadoDireita = limpaDireita()
    
def limpaDireita():
    global flag
    global Estados
    flag = [Direita, estadoUn]
    if(flag[0] == Direita and flag[1] == 0):
        print("Direita limpo")
        Estados[1] = 0
    else:
        print("Direita Suja")
        flag = [Direita, 0]
        Estados[1] = 0

def limpaEsquerda():
    global flag
    global Estados
    flag = [Esquerda, estadoDeux]
    if(flag[0] == Esquerda and flag[1] == 0):
        print("Esquerda limpo")
        Estados[0] = 0
    else:
        print("Esquerda Suja")
        flag = [Esquerda, 0]
        Estados[0] = 0

def VisualizacaoGrafica():
    labels = ['Esquerda', 'Direita']
    Peso = [50, 50]
    cores = ['green', 'green']
    explode = (0, 0,)  # somente explode primeiro pedaço
    total = sum(Peso)
    plt.pie(Peso, explode=explode, labels=labels, colors=cores, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90)
    plt.axis('equal') 
    plt.show()
    

# ici commence
AgenteAspiradorDePoReativo()
print("estadoUn ", estadoUn)
print("estadoDeux ", estadoDeux)
global flag
if(Estados[0] == 0 and Estados[1] == 0):
    print("Todos os estados limpos")
    VisualizacaoGrafica()
else:
    AgenteAspiradorDePoReativo()

"""
função AGENTE-REATIVO-SIMPLES (percepção) retorna uma ação
variáveis estáticas
 regras // conjunto de regras condição-ação
estado  INTERPRETAR-ENTRADA(percepção)
regra  REGRA-CORRESPONDENTE(estado, regras)
ação  AÇÃO-DA-REGRA(regra)
retornar ação

///////////////////////////////////////////////////////////////////////////////

função AGENTE-ASPIRADOR-DE-PÓ-REATIVO ([posição, estado)]
retorna uma ação
se estado = Sujo então retornar Aspirar
senão se posição = A então retornar Direita
senão se posição = B então retornar Esquerda

"""