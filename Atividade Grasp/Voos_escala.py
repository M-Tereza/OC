#Estudo de Caso: Escalonamento de voos

#Importação de dados do arquivo voos.txt
#Informações constantes no arquivo
#IdVoo, origem, destino, partida, chegada, distância

import random

voos = []
PFG = []

with open('voos.txt', 'r') as arq:
    for linha in arq:
        voo = linha.strip().split(';')
        #strip - Remove espaços e quebras de linha
        #split(';') - separa os elementos sempre que encontrar ;
        #armazena toda a linha lida na lista voo, com os dados separados

        voos.append([
            int(voo[0]),
            voo[1],
            voo[2],
            voo[3],
            voo[4],
            float(voo[5])
        ])
        
        #PFG
        if(voo[1=='PFG']):
            hora=voo[3]
        else:
            hora=voo[4]
            
        # armazena na lista PFG somente o id e o horário em que a pista será efetivamente utilizada
        PFG.append([
            voo[0],
            hora
            ])
        

# for i in range (len(voo))

#Criando função para calcular atraso em minutros
def calculaAtraso (hora1, hora2):
    h1, m1 = hora1.split(':')               #separou hora em suas variáveis: o que tiver antes de : vai para h e o que tiver depois, para m
    h2, m2 = hora2.split(':')
    
    tempo1 = int(h1)*60 + int(m1)
    tempo2 = int(h2)*60 + int(m2)
    
    atraso = tempo2-tempo1
    
    return atraso
    
def calcularIntervalo(hora):
    m,h = hora.split(':')
    
    h=int(h)
    m= int(m) + 5
    
    if m>=60:
        m-=60
        h+=1
        
    
    if h<10:
        hora = '0'+str(h)+':'
    else:
        hora = str(h)+':'
        
    if m<10:
        hora = hora + '0' + str(m)
    else:
        hora = hora + str(m)
    
# Gerar solução aleatória e separar as alocações das pistas (sortera as pistas)
P1=[]
P2=[]
lib1='06:00'
lib2='06:00'

PFG.sort(key=lambda x: x[1])

for i in range (len(PFG)):
    
    pista=random.randint(1,2)
    
    hora=PFG[i][1]
    
    if pista==1:
        
        real=max(lib1, hora)
        
        atraso=calculaAtraso(hora, real)
        P1.append([PFG[i][0], real, atraso])
        
        lib1=calcularIntervalo(real)
        
        print([PFG[i][0], real, atraso])
                      
    else:
        
        real=max(lib2, hora)
        
        atraso=calculaAtraso(hora, real)
        P2.append([PFG[i][0], real, atraso])
        
        lib2=calcularIntervalo(real)
        
        print([PFG[i][0], real, atraso])
