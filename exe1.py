carrinho = ['Notbook','Mouse','Teclado']

for item in carrinho:
    print(item)
    
carrinho.append('Headset')
carrinho.remove('Mouse')
carrinho.insert(1,'impressora')
carrinho[0] = 'mac'
print(carrinho[2])
print(carrinho)