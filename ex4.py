
pedido = {
"cliente": "João Silva",
"prato": "Hambúrguer Artesanal",
"status": "em preparo"
}

pedido["status"] = "saiu para entrega"

print(f'Pedido do cliente {pedido["cliente"]}\n {pedido["prato"]}\n Status: {pedido["status"]}\n')

