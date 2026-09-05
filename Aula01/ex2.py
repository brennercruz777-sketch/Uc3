username_cadastrado = "admin"
senha_cadastrada = "1234"

if input("Digite seu usuário\n\n") == username_cadastrado and input("Digite sua senha\n\n") == senha_cadastrada:
    print("Acesso concedido")
else:
    print("Credenciais inválidas")