def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()  # Ignora espaços e deixa tudo minúsculo
    return palavra == palavra[::-1]
