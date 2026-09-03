estoque = [         
{"id": 1, "nome": "Notebook", "preco": 3500.00, "quantidade": 20},
{"id": 2, "nome": "Mouse", "preco": 80.00, "quantidade": 100},
{"id": 3, "nome": "Teclado", "preco": 150.00, "quantidade": 50},
]

estoque.append({"id": len(estoque)+1, "nome": "Monitor", "preco": 1200.00, "quantidade": 30})

print(estoque[1]["nome"])
print(len(estoque))

