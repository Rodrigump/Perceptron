# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:20:13 2019

@author: Rodrigo Rossi
"""

import math
import numpy as np

def sigmoide (x):
    return 1 / (1 + math.exp(-x))

def d_sigmoide (x):
    return (1-sigmoide(x))*sigmoide(x)

def setEQM (erros):
    soma = 0
    for i in range(len(erros)):
        soma = soma + (erros[i]**2)
    resultado = soma / 2
    return resultado

def setAtivacao (soma):
    ativacao = soma
    for i in range (len(ativacao)):
        for j in range(len(ativacao[i])):
            ativacao[i][j] = sigmoide(soma[i][j])
    return ativacao

taxa_aprendizado = 0.5

entradas = np.array([[0.0,0.0,1.0],[0.0,1.0,1.0],[1.0,0.0,1.0],[1.0,1.0,1.0]])
saidas = np.array([[0.0],[0.0],[0.0],[1.0]])
pesos = np.array([[1.0],[1.0],[1.5]])
soma = np.dot(entradas,pesos)
ativacao = setAtivacao(soma)
erros = saidas - ativacao
eqm = setEQM(erros)

for k in range(10000):
    for i in range(len(entradas)): #linhas 4
        for j in range(len(entradas[i])): #colunas 3
            pesos[j] = pesos[j] + (taxa_aprendizado * erros[i] * d_sigmoide(soma[i]) * entradas[i][j])
            soma = np.dot(entradas,pesos)
            ativacao = setAtivacao(soma)
            erros = saidas - ativacao
            eqm = setEQM(erros)
