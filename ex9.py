base_usuarios = [
{"id": 101, "nome": "Alice"},
{"id": 102, "nome": "Bruno"},
{"id": 103, "nome": "Carla"}
]


def encontrar_id(id):
    econtrado = False
    for i in base_usuarios:
        if id == i['id']:
            econtrado = True
            print(f"Usuário encontrado: {i['nome']}")
    if not econtrado:
        return "Usuário não encontrado"
    
encontrar_id(int(input("Digite o ID do usuário que deseja encontrar: ")))