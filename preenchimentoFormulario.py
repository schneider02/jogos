# Função para exibir o menu e capturar dados do usuário
def cadastro():
    print("=== Ficha de Cadastro ===")
    
    # Captura dos dados
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    
    # Armazenando as informações em um dicionário
    ficha_cadastro = {
        "Nome": nome,
        "Idade": idade,
        "E-mail": email,
        "Telefone": telefone,
        "Endereço": endereco
    }
    
    # Exibindo as informações cadastradas
    print("\n=== Ficha Cadastral ===")
    for chave, valor in ficha_cadastro.items():
        print(f"{chave}: {valor}")

# Chama a função de cadastro
cadastro()
