'''Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
 números repetidos no vetor VET e em que posições se encontram'''

tamanho_vetor = 10
vet = []

for i in range(tamanho_vetor):
    num = int(input(f"Digite o {i+1}º número: "))
    vet.append(num)

repetidos = []
posicoes = []
for i in range(tamanho_vetor):
    for j in range(i+1, tamanho_vetor):
        if vet[i] == vet[j] and vet[i] not in repetidos:
            repetidos.append(vet[i])
            posicoes.append([i, j])

if not repetidos:
    print("Não há números repetidos no vetor.")
else:
    for i in range(len(repetidos)):
        print(f"O número {repetidos[i]} aparece nas posições {posicoes[i]} do vetor.")
