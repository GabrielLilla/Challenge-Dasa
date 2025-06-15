def garante_numero():
    if numero_estoque.isnumeric():
        return numero_estoque
    
while True:
    nomeProduto = input("Diga o nome do produto: ")
    garante_numero(numero_estoque)
    numero_estoque = input("Diga o estoque do produto: ")

estoque = ()
