valordamaca=""
quantidademaca= int(input("Digite a quantidade: "))

if quantidademaca >= 12:
    valordamaca= 1
    resultado=quantidademaca*valordamaca
    print(f"Você comprou {quantidademaca} maças irá pagar {resultado} reais")

else:
    valordamaca = 1.30
    resultado = quantidademaca * valordamaca
    print(f"Você comprou {quantidademaca} irá pagar {resultado} reais")



