def tela_cadastro():
    print("=== Tela de Cadastro ===")
    
    nome_cliente = input('Nome do cliente: ')
  
    endereco = input('Endereço da rua: ')
   
    print("\n=== Dados Cadastrados ===")
    print(f"Nome do Cliente: {nome_cliente}")
    print(f"Endereço: {endereco}")

tela_cadastro()