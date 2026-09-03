def latir():
    print("Au Au!")

def latir_retorno():
    return "au au", "meow"

discurso_canhorro = latir_retorno()[0]

print(discurso_canhorro)