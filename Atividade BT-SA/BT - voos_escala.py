'''
Projeto GRASP
Elaborado por Maria Tereza e Iago
tam LRC = 
Etapa Construtiva - VMP
Busca Local  - Hill Climbing (last)
Critério de parada - 10000
'''

import random

voos = []
PFG = []

with open("voosNovo.txt", "r") as arq:
    for linha in arq:
        voo = linha.strip().split(";")
        #strip - Remove espaços e quebras de linha
        #split(";") - separa os elementos sempre que encontrar ;
        #armazena toda a linha lida na lista voo, com os dados separados

        voos.append([
            int(voo[0]),
            voo[1],
            voo[2],
            voo[3],
            voo[4],
            int(voo[5])
        ])
        
        if (voo[1]=='PFG'):
            hora=voo[3]
        else:
            hora=voo[4]
        
        #armazena na lista PFG somente o ID e o horário em que a pista PFG será efetivamente usada
        PFG.append([
            int (voo[0]),
            hora
        ])



def calculaAtraso(hora1, hora2):
    h1, m1 = hora1.split(':')
    tempo1 = int(h1)*60 + int(m1)
    h2, m2 = hora2.split(':')
    tempo2 = int(h2)*60 + int(m2)
    atraso=tempo2-tempo1
    return(atraso)


def calculaIntervalo(hora): #passar como parâmetro o intervalo de segurança
    h, m = hora.split(':')
    h=int(h)
    m=int(m)#+5
    if m>=60:
        m-=60
        h+=1
    if h<10:
        hora='0'+ str(h) + ':'
    else:
        hora=str(h) + ':'
    if m<10:
        hora=hora + '0' + str(m)
    else:
        hora=hora + str(m)
    return(hora)

def calculaAptidao(P1, P2):
    total=0
    for i in range(len(P1)):
        total+=P1[i][2]
    for i in range(len(P2)):
        total+=P2[i][2]
    return(total)

def imprimeSolucao(P1, P2):
    print('Pista 1:')
    print("Voo\t\tHorario\tAtraso")
    for i in range(len(P1)):
        print(P1[i][0], '\t', P1[i][1], '\t', P1[i][2])

    print('Pista 2:')   
    print("Voo\t\tHorario\tAtraso")
    for i in range(len(P2)):
        print(P2[i][0], '\t', P2[i][1], '\t', P2[i][2])
    
    return()

'''
#Gerar solução aleatória e separar as alocações nas listas P1 e P2, conforme a pista a ser utilizada
P1=[]
P2=[]
lib1='06:00'
lib2='06:00'

PFG.sort(key=lambda x: x[1])

for i in range(len(PFG)):
    pista=random.randint(1,2)
    hora=PFG[i][1]
    if pista==1:
        real=max(lib1, hora)
        atraso=calculaAtraso(hora, real)
        P1.append([PFG[i][0], real, atraso])
        lib1=calculaIntervalo(real)
        #print(pista, PFG[i][0],real, lib1, atraso)
    if pista==2:
        real=max(lib2, hora)
        atraso=calculaAtraso(hora, real)
        P2.append([PFG[i][0], real, atraso])
        lib2=calculaIntervalo(real)
        #print(pista, PFG[i][0],real, lib2, atraso)


imprimeSolucao(P1, P2)
atraso=calculaAptidao(P1, P2)
print('Atraso total', atraso)
'''

