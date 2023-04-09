convidados = ["Taylor Swift", "Harry Styles", "Chris Martin", "Tom Ellis", "Demi Lovato"]
for convidado in convidados:
    print('Olá',convidado, 'você está convidado para o meu aniversário!')

print('A',convidados[4], 'não poderá comparecer!')

newlista = convidados[4] = "Rihanna"
print('Nova lista de convidados', convidados)
for convidado in convidados:
    print ('Olá', convidado, 'compareça ao meu aniversário!')