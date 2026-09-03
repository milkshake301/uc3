valor_total = 10
saldo_usuario = 9.0
pergunta =  input("você possui cupom de desconto? s/n\n: ")
if pergunta == "s":
    cupom_valido = True
else:
    cupom_valido = False

if cupom_valido:
    valor_total *= 0.9 
    
if saldo_usuario >= valor_total:
    print("201 Created - Compra realizada com sucesso!")
else:
    print("402 Payment Required - Saldo insuficiente para realizar a compra.")