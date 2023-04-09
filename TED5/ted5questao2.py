numtabuada = [1,2,3,4,5,6,7,8,9,10] #array
multiplicador = [1,2,3,4,5,6,7,8,9,10] #array
for n in numtabuada:
    print('Tabuada do ' , n)
    for m in multiplicador:
        print(n, " x ",m,": ", n * m)

# Outra forma de ser fazer:
# for tabuada in range(1, 11):
#     for valor in range(1, 11):
#         print(tabuada, " x ",valor,": ", tabuada * valor)