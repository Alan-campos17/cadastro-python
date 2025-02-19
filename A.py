def tela_cadastro():
    print("=== Tela de Cadastro ===")
    
    nome_cliente = input('Nome do cliente: ')
  
    endereco = input('Endereço da rua: ')

    numero_telefone = input('numero telefone: ')

    cpf = input('cadastro do cpf: ')

    Email = input('cadastro email:')

    data_nascimento = input('data de nascimento: ')
   
    print("\n=== Dados Cadastrados ===")
    print(f"Nome do Cliente: {nome_cliente}")
    print(f"Endereço: {endereco}")
    print(f"numero telefone: {numero_telefone}")
    print(f"cpf: {cpf}")
    print(f"Email: {Email}")
    print(f"data de nascimento{data_nascimento}")

tela_cadastro()