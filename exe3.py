estoque= {
    1 : {'nome':'notbook','preco' : 2222, 'qtd' : 12},
    2 : {'nome':'mouse','preco' : 200, 'qtd' : 1},
    3 : {'nome':'teclado','preco' : 450, 'qtd' :10 }
}
cod = 1 
quant = 10

if cod in estoque:
    estoque[cod]['qtd'] += quant
    
for cod,produto in estoque.items():
    print(f'{cod} - {produto['nome']} - {produto['qtd']}')