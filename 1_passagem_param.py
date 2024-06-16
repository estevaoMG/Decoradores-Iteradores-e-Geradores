def mensagem(nome):
    print("executando mensagem")
    return f"Oi, {nome}!"


def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá! Tudo bem com você {nome}?"


def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

print(executar(mensagem, "Estevão"))
print(executar(mensagem_longa, "Estevão"))