a=2
a=3.14
a='p'
a="texto"

print ('Saida', a[0])
print (a[2])

#Comentário de linha
''' Comentário de bloco
b=input('Digite um valor:')
b=int(b)
'''

dados=[1, 3.14, 'cinco', 7]

print (dados[2])

dados.append(9)

tam=len(dados)

vetor=[3, 4, 5, 0, 7, 8]

matriz=[[1, 2],
        [4, 3],
        [5, 7],
        [6, 2],
        [7, 8],
        [8, 0]]

if vetor[0]>vetor[3]:
    print('maior')
elif vetor[0]<vetor[3]:
    print('menor')
else:
    print ('igual')


while (vetor[0]>0):
    vetor[0]-=1

for i in range(4,10,2):
    print(i)

for i in range(len(vetor)):
    print(vetor[i])

pares=(1,2)

dic={0:'zero'}
print(dic[0])










