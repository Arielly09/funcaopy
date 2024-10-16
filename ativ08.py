def contar_vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador
