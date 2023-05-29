def encontra_palavras(lista_palavras, letra):
 return [palavra for palavra in lista_palavras if palavra.startswith(letra)]

palavras = ["mamão", "tangerina", "morango", "acerola"]
letra = "m"

print(encontra_palavras(palavras, letra))