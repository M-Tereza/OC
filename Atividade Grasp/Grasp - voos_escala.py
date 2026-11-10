'''
Projeto GRASP
Elaborado por Iago Almeida e Maria Tereza
tam LRC = 3
Etapa Construtiva - VMP
Busca Local  - Permutar horários próximos entre as pistas (last)
Critério de parada - 10000
'''

import random
import copy

voos = []
voosPFG = []

with open("voosNovo.txt", "r") as arq:
    for linha in arq:
        voo = linha.strip().split(";")

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
        
        voosPFG.append([
            int (voo[0]),
            hora,
            int (voo[5])
        ])

def converteHorarioParaMinutos(horario):
    h, m = horario.split(':')
    minutos = int(h)*60 + int(m)
    return(minutos)


def calculaAtrasoMinutos(horarioPrevisto, horarioReal):
    tempo1 = converteHorarioParaMinutos(horarioPrevisto)
    tempo2 = converteHorarioParaMinutos(horarioReal)
    atraso=tempo2-tempo1
    return(atraso)

def calculaHorarioLiberacaoPista(horario,intervaloSeguranca):
    h, m = horario.split(':')
    h=int(h)
    m=int(m)+intervaloSeguranca
    if m>=60:
        m-=60
        h+=1
    if h<10:
        horario='0'+ str(h) + ':'
    else:
        horario=str(h) + ':'
    if m<10:
        horario=horario + '0' + str(m)
    else:
        horario=horario + str(m)
    return(horario)

def calculaAtrasoTotal(S):
    total=0
    for i in range(len(S[0])):
        total+=S[0][i][2]
    for i in range(len(S[1])):
        total+=S[1][i][2]
    return(total)

def imprimeSolucao(S):
    print('Pista 1:')
    print("Voo\t\tHorario\tAtraso")
    for i in range(len(S[0])):
        print(S[0][i][0], '\t', S[0][i][1], '\t', S[0][i][2])

    print('Pista 2:')   
    print("Voo\t\tHorario\tAtraso")
    for i in range(len(S[1])):
        print(S[1][i][0], '\t', S[1][i][1], '\t', S[1][i][2])
    
    return()


#SOLUÇÃO GRASP

S=[[], []]
atrasoTotal=None
parada=1
tamLRC=3

#Etapa construtiva

voosPFG.sort(key= lambda x: x[1])

for i in range(parada):
    
    SAtual=[[], []]          #solução com os ids dos voos, o horário efetivo de entrada/saída (considerando atraso) e o atraso
    LC=voosPFG.copy()
    voosOrdemS = [[], []]    #é a lista de voos (contem id, horário previsto e intervalo de segurança), mas na mesma ordem que a solução
    horariosLiberacao=['06:00','06:00']
    
    while (len(SAtual[0])+len(SAtual[1])) < len(voosPFG):
                
        if len(LC) >= tamLRC:
            valorSorteado=random.randint(0, tamLRC-1)
        else:
            valorSorteado=random.randint(0, len(LC)-1)
        
        pista=random.randint(0,1)
        
        horarioPrevisto=LC[valorSorteado][1]
        horarioReal=max(horarioPrevisto,horariosLiberacao[pista])
        intervaloSeguranca=LC[valorSorteado][2]
    
        atraso=calculaAtrasoMinutos(horarioPrevisto, horarioReal)
        
        voosOrdemS[pista].append(LC[valorSorteado])
        SAtual[pista].append([LC[valorSorteado][0], horarioReal, atraso])
        horariosLiberacao[pista]=calculaHorarioLiberacaoPista(horarioReal, intervaloSeguranca)
        del LC[valorSorteado]
        
    atrasoTotalAtual=calculaAtrasoTotal(SAtual)
    
    if not atrasoTotal or atrasoTotalAtual < atrasoTotal:
        S=SAtual
        atrasoTotal=atrasoTotalAtual
        
        
    #Etapa Refinamento
    
    SRef=[[], []]
    posI=0
    posP=0
    posVooRefAtualI=0
    posVooRefAtualP=-1
    qtdPermutacoes=0
    horariosLiberacao=['06:00','06:00']
   
    if voosOrdemS[0][0][1] < voosOrdemS[1][0][1]:
        posP=1
    else:
        posI=1
        
    
    qtdPermutacoes = min(len(voosOrdemS[posI])-1, len(voosOrdemS[posP]))
    
    print(posI)
    print(len(voosOrdemS[posI]))
    print(len(voosOrdemS[posP]))
    print(qtdPermutacoes)
    
    
    for k in range (qtdPermutacoes-1):
        
        voosOrdemS[posI][posVooRefAtualI+1], voosOrdemS[posP][posVooRefAtualP+1] = voosOrdemS[posP][posVooRefAtualP+1], voosOrdemS[posI][posVooRefAtualI+1]
        
        SRef=copy.deepcopy(voosOrdemS)
        
        
        for j in range(len(SRef[posI])):
            horarioPrevistoI=voosOrdemS[posI][j][1]
            
            horarioRealI=max(horarioPrevistoI,horariosLiberacao[posI])
            intervaloSegurancaI=voosOrdemS[posI][j][2]
            atrasoI=calculaAtrasoMinutos(horarioPrevistoI, horarioRealI)
            SRef[posI][j]=[voosOrdemS[posI][j][0], horarioRealI, atrasoI]
            horariosLiberacao[posI]=calculaHorarioLiberacaoPista(horarioRealI, intervaloSegurancaI)
            
        for j in range(len(SRef[posP])):
            horarioPrevistoP=voosOrdemS[posP][j][1]
            horarioRealP=max(horarioPrevistoP,horariosLiberacao[posP])
            intervaloSegurancaP=voosOrdemS[posP][j][2]
            atrasoP=calculaAtrasoMinutos(horarioPrevistoP, horarioRealP)
            SRef[posP][j]=[voosOrdemS[posP][j][0], horarioRealP, atrasoP]
            horariosLiberacao[posP]=calculaHorarioLiberacaoPista(horarioRealP, intervaloSegurancaP)
        
        atrasoTotalRef=calculaAtrasoTotal(SRef)
        
        if atrasoTotalRef < atrasoTotal:
            S=SRef
            atrasoTotal=atrasoTotalRef
        
        posVooRefAtualI+=1
        posVooRefAtualP+=1
        
        


imprimeSolucao(S)

