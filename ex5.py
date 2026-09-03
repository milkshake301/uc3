usuarios = [
{"id": 1, "nome": "Ana", "email": "ana@email.com", "ativo": True},
{"id": 2, "nome": "Beatriz", "email": "bea@email.com", "ativo": False},
{"id": 3, "nome": "Carlos", "email": "car@email.com", "ativo": True}
]

email_ativos = []

for i in usuarios:
    if i["ativo"]:
        email_ativos.append(i["email"])
print("email_ativos:")
for i in email_ativos:
    print(i)