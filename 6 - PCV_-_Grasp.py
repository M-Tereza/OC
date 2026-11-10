import random

'''
Projeto GRASP
Elaborado por []
Proposta
tam LRC = 3
Etapa Construtiva - VMP
Busca Local - Hill Climbing
Critério de parada - 100
#Improving: Last

'''

#PCV 5 cidades
cidades = {0:'Belo Horizonte', 1:'Governador Valadares', 2:'Juiz de Fora', 3:'Montes Claros', 4:'Uberlandia'}

distancias = [[9999.99, 63.60, 53.20, 90.40, 159.40],
              [63.60, 9999.99, 90.80, 106.80, 169.40],
              [53.20, 90.80, 9999.99, 135.40, 157.60],
              [90.40, 106.80, 135.40, 9999.99, 125.40],
              [159.40, 169.40, 157.60, 125.40, 9999.99]]

'''
#PCV 20 cidades
cidades = {0:'Belo Horizonte', 1:'Governador Valadares', 2:'Juiz de Fora', 3:'Montes Claros', 4:'Uberlandia', 5:'Araxa', 6:'Capitolio', 7:'Congonhas', 8:'Diamantina', 9:'Leopoldina', 10:'Divinopolis', 11:'Ervalia', 12:'Formiga', 13:'Ibituruna', 14:'Ipatinga', 15:'Januaria', 16:'Lavras', 17:'Manhumirim', 18:'Ouro Branco', 19:'Paracatu'}

distancias = [[99999,63.60,53.20,90.40,159.40,73.40,55.20,86.20,106.60,99.00,46.60,122.00,48.80,84.80,115.40,138.00,71.40,132.80,90.20,71.80],
[63.60,99999,90.80,106.80,169.40,134.80,123.80,79.20,61.00,71.80,92.60,35.00,103.80,61.00,20.80,133.00,109.40,44.00,74.40,148.40],
[53.20,90.80,99999,135.40,157.60,120.40,91.00,37.40,108.60,19.60,65.80,34.60,72.00,44.80,85.80,169.40,49.00,58.40,37.60,150.80],
[90.40,106.80,135.40,99999,125.40,113.20,127.60,98.00,45.40,146.40,93.40,134.00,89.40,138.60,104.40,34.00,126.40,143.60,138.40,93.40],
[159.40,169.40,157.60,125.40,99999,35.40,84.80,119.00,130.60,160.60,91.80,156.40,83.60,83.40,150.20,150.00,106.00,167.40,124.40,67.20],
[73.40,134.80,120.40,113.20,35.40,99999,55.20,86.00,106.60,132.00,57.20,122.00,49.00,84.80,115.40,138.00,71.40,132.80,90.20,71.80],
[55.20,123.80,91.00,127.60,84.80,55.20,99999,75.40,99.40,103.60,34.00,111.40,18.20,50.60,104.80,158.60,42.40,122.20,79.60,104.60],
[86.20,79.20,37.40,98.00,119.00,86.00,75.40,99999,72.20,49.00,45.00,36.60,59.80,36.80,60.40,133.40,40.80,57.00,4.80,114.80],
[106.60,61.00,108.60,45.40,130.60,106.60,99.40,72.20,99999,120.40,68.80,108.00,86.60,96.80,58.80,79.40,100.60,105.60,76.20,98.60],
[99.00,71.80,19.60,146.40,160.60,132.00,103.60,49.00,120.40,99999,77.40,23.20,84.80,56.40,66.60,181.00,60.60,39.20,49.20,162.40],
[46.60,92.60,65.80,93.40,91.80,57.20,34.00,45.00,68.80,77.40,99999,80.40,17.20,30.20,72.60,126.60,34.00,899.80,47.20,103.00],
[122.00,35.00,34.60,134.00,156.40,122.00,111.40,36.60,108.00,23.20,80.40,99999,89.40,60.80,47.20,166.80,65.00,37.40,34.00,150.20],
[48.80,103.80,72.00,89.40,83.60,49.00,18.20,59.80,86.60,84.80,17.20,89.40,99999,30.80,87.20,145.80,22.80,105.80,63.20,96.00],
[84.80,61.00,44.80,138.60,83.40,84.80,50.60,36.80,96.80,56.40,30.20,60.80,30.80,99999,86.40,157.60,11.20,91.00,38.80,126.60],
[115.40,20.80,85.80,104.40,150.20,115.40,104.80,60.40,58.80,66.60,72.60,47.20,87.20,86.40,99999,138.40,89.00,38.40,50.60,141.40],
[138.00,133.00,169.40,34.00,150.00,138.00,158.60,133.40,79.40,181.00,126.60,166.80,145.80,157.60,138.40,99999,161.60,178.40,137.00,118.40],
[71.40,109.40,49.00,126.40,106.00,71.40,42.40,40.80,100.60,60.60,34.00,65.00,22.80,11.20,89.00,161.60,99999,107.60,43.00,118.60],
[132.80,44.00,58.40,143.60,167.40,132.80,122.20,57.00,105.60,39.20,899.80,37.40,105.80,91.00,38.40,178.40,107.60,99999,52.00,160.00],
[90.20,74.40,37.60,138.40,124.40,90.20,79.60,4.80,76.20,49.20,47.20,34.00,63.20,38.80,50.60,137.00,43.00,52.00,99999,118.40],
[71.80,148.40,150.80,93.40,67.20,71.80,104.60,114.80,98.60,162.40,103.00,150.20,96.00,126.60,141.40,118.40,118.60,160.00,118.40,99999]] 
'''

def calculaCusto(Sol):
    custo=0
    for i in range(len(cidades)):
        atual=Sol[i]
        prox=Sol[i+1]
        d=distancias[atual][prox]
        custo+=d
    return(custo)

def imprimeSolucao(Sol):
    for i in range(len(Sol)):
        atual=Sol[i]
        print(cidades[atual])

# Iplementação GRASP
tamLRC = 3
parada = 100

for i in range(1):      #roda uma vez, se nãp for boa, roda 100 vezes
    S=[0]
    LC=[]
    #Sempre que for colocar elemento lista de candidatos, ver se ele está dentro ou fora da solução antes
    # Duas formas
    #   Procura na lista testando se está dentro ou fora
    #   Cria uma lista ACHOU em que, para cada vértice, coloca 1 se estiver na solução e 0 se não tiver. Sempre que colocar um vértica na solução, troca o estado para 1
    achou = []
    ult = 0  # ultimo vértice percorrido
    
    for j in range(len(cidades)):
        achou.append(0)
    achou[0]=1

    while len(S) < len(cidades): 
        LC=[]
        for j in range(len(cidades)):
            if(achou[j]==0): # se for 0, vértice netra na solução
                LC.append([j, distancias(ult, j)])
        
        LC.sort(key=lambda x: x[1])       #Lista ordenada
        
        # Não precisa criar uma lista nova para o LRC, só testar antes se a lista não é menor que o tamanho escolhido
        # Tendo tamanho menor: só sortear entre os primeiros X elementos da lista
        
        lim = min(tamLRC, len(LC))
        pos=random.randint(0, lim-1)
        ult=LC[pos][0]
        achou[ult]=1
        S.append(ult)
    
    S.append(0)  # volta à origem
    custo = calculaCusto(S)
    if(i==0):
        Best=S[:]
        custoBest=custo
    if(custo<custoBest):
        custoBest=custo    
   
    
   #BuscaLocal
   for k in range (1, len(S)-2):
       for l in range (k+1, len(S)-2):
           S[k], S[l] = S[l], S[k]    #swap simples, permuta esses elementos
           custo = calculaCusto(S)
           if (custo<custoBest):
               Best=S[:]
               custoBest=custo
           S[k], S[l]=S[l], S[k]
    









