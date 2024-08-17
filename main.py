listagem_carros = []

def menu():
    while True:
        pergunta = int(input("""Menu:
                                 
1. Adicionar carro
2. Listar carros
3. Editar carro
4. Excluir carro
5. Sair

Digite aqui: """))
            
        if pergunta == 1:
                marca = input("Digite a marca do carro: ")
                modelo = input("Digite o modelo do carro: ")
                ano = int(input("Digite o ano do carro: "))
                preco = float(input("Digite o preço do carro: "))
                carro = (marca, modelo, ano, preco)
                listagem_carros.append(carro)
                print("Carro adicionado com sucesso!")
                
        elif pergunta == 2:
                if listagem_carros:
                    for i, carro in enumerate(listagem_carros):
                        i += 1
                        print(f"{i}. Marca: {carro[0]}, Modelo: {carro[1]}, Ano: {carro[2]}, Preço: R${carro[3]:.2f}")
                else:
                    print("Nenhum carro cadastrado.")
                
        elif pergunta == 3:
                if not listagem_carros:
                    print("Nenhum carro disponível na lista.")
                else:
                    for i, carro in enumerate(listagem_carros):
                        i += 1
                        print(f"{i}. Marca: {carro[0]}, Modelo: {carro[1]}, Ano: {carro[2]}, Preço: R${carro[3]:.2f}")
                    
                    editar = int(input("Digite o número do carro que deseja editar: ")) - 1
                    
                    if 0 <= editar < len(listagem_carros):
                        marca = input("Digite a nova marca do carro: ")
                        modelo = input("Digite o novo modelo do carro: ")
                        ano = int(input("Digite o novo ano do carro: "))
                        preco = float(input("Digite o novo preço do carro: "))
                        listagem_carros[editar] = (marca, modelo, ano, preco)
                        print("Carro atualizado com sucesso!")
                    else:
                        print("Número do carro inválido!")
                
        elif pergunta == 4:
                if not listagem_carros:
                    print("Nenhum carro disponível para excluir.")
                else:
                    for i, carro in enumerate(listagem_carros):
                        i += 1
                        print(f"{i}. Marca: {carro[0]}, Modelo: {carro[1]}, Ano: {carro[2]}, Preço: R${carro[3]:.2f}")
                    
                    excluir = int(input("Digite o número do carro que deseja excluir: ")) - 1
                    
                    if 0 <= excluir < len(listagem_carros):
                        del listagem_carros[excluir]
                        print("Carro excluído com sucesso!")
                    else:
                        print("Número do veículo inválido!")
                
        elif pergunta == 5:
                print("Saindo...")
                break               
        else:
                print("Opção inválida! Por favor, escolha as opções listadas no menu.")
        

menu()
