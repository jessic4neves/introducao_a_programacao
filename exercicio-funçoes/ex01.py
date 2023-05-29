def conta_vogais(string):
    vogais = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vogais:
            count += 1
    return count

print(conta_vogais('Jessica'))