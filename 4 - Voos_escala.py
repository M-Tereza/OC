#Estudo de Caso: Escalonamento de voos

#Importação de dados do arquivo voos.txt
#Informações constantes no arquivo
#IdVoo, origem, destino, partida, chegada, distância

voos = []

with open("voos.txt", "r") as arq:
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
            float(voo[5])
        ])

