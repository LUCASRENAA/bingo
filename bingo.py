import xml.etree.ElementTree as ET
from sys import argv as arg
import os
from random import randint
global contar,contar1
contar1= 0
contar = 0

meuArquivo = open('Valores.txt', 'w')
meuArquivo.write("")
meuArquivo.close()

lista = []
print("comecou")
terminar = 0
contador = 1
quantidade = int(input("Digite se é um os dois jogadores "))
while (quantidade != 1 and quantidade != 2):
    quantidade = int(input("Digite se é um ou dois"))

jogador1 = input("Digite o nome do jogador1 ")
jogador2 = input("Digite o nome do jogador2 ")


def my_class(lista1):
    lista1 = []
    while len(lista1) != 10:
        a = randint(1,100)
        while (a in lista1):
            a = randint(1,100)
        lista1.append(a)
    print(lista1)
    meuArquivo = open('Valores.txt', 'a')
    meuArquivo.write(str(lista1))
    meuArquivo.close()
    return lista1
for variavel in range(quantidade):
    contador3 = "lista" + str(variavel)
    my_class("lista" + str(variavel)) 
    #print(contador3)
    contador3 = "lista" + str(variavel)


open_file = open('Valores.txt','r')
read_file = open_file.read()
#print(read_file)
read_file = read_file.replace('[','')
read_file = read_file.replace(']',',')
#print(read_file)
open_file.close()
meuArquivo = open('Valores1.txt', 'w')
meuArquivo.write(read_file)
meuArquivo.close()

index = quantidade * 9 
f = open("Valores1.txt",'r')
texto = f.readlines()

x = 0

while x < len(texto):
    if texto[x] == "\n":
        local = texto.index(texto[x])
        texto.pop(local)
    else:
        texto[x] = texto[x].split(',')
        x += 1

    # Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.

for i in texto:
    local = texto.index(i) # Local do i em texto
    for b in i:
        local2 = texto[local].index(b) # Local2 do b em i ( local )
        if "\n" in b:
            texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"



    
while (terminar != 1):
    nao_passar = 0
    input("aperte enter para sortear o numero\n")
    b = 0
    a = randint(1,100)
    while (a in lista):
         a = randint(1,100)
    print(a)
    #print(read_file)
 
    lista.append(a)
    #print(lista)
    #print(contador)
    contar = 0
    contar1 = 0
    p = -1
    
    for variavel in range(quantidade * 10):
        
        p = p + 1
        #print(variavel) começa em zero
        for testando2 in lista:
            
            #print(texto[0][p])
            #print(lista)
            #print(texto)
            if (int(texto[0][p]) == testando2):
                if (p < 10):
                    #print("jogador1 acertou em cheio com o valor" + texto[0][p])
                    contar = contar + 1

                if (p > 10):
                    #print("jogador" + p % 9 + " acertou em cheio com o valor")
                    contar1 =contar1 + 1

                    

    contador = contador + 1
    intem = 1
    print(jogador1 + " tem " + str(contar) + " acerto(s)" )
    print(jogador2 + " tem " + str(contar1) + " acerto(s)" )


    if (contar == 10):
        print("Parabéns, " + jogador1 + " Você ganhou!")
        quit()
    if (contar1 == 10):
        print("Parabéns, " + jogador2 + " Você ganhou!")
        quit()

    for intem in range(100):
        if (intem in lista):
            continue
        else:
            nao_passar = 1

        if (intem == 100):
            if (intem in lista != true):
                if (nao_passar == 1):
                    terminar = 0
                else: 
                    input("acabou")
                    terminar = 1