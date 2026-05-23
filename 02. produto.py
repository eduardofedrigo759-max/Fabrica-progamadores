#criando as variáveis e solicitando os valores ao usuário
nome_produto = input("digite o nome do produto: ")
preco= float(input("digite o preço do produto: "))
desconto = float(input("digite o percentual do desconto: "))

#calculando o desconto e o preço fianl
valor_desconto = preco * desconto / 100
preco_final= preco - valor_desconto

#apresentando o preço final ao usario 
print(f"produto: {nome_produto} - preco final: R${preco_final}" )