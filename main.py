class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Preço: R${self.preco:.2f}"


class Concessionaria:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self):
        marca = input("Digite a marca do carro: ")
        modelo = input("Digite o modelo do carro: ")
        ano = int(input("Digite o ano do carro: "))
        preco = float(input("Digite o preço do carro: "))
        carro = Carro(marca, modelo, ano, preco)
        self.carros.append(carro)
        print("Carro adicionado com sucesso!")

    def listar_carros(self):
        if not self.carros:
            print("Nenhum carro cadastrado.")
            return
        for idx, carro in enumerate(self.carros, 1):
            print(f"\nCarro {idx}:")
            print(carro)

    def editar_carro(self):
        self.listar_carros()
        if not self.carros:
            return
        index = int(input("Digite o número do carro que deseja editar: ")) - 1
        if 0 <= index < len(self.carros):
            marca = input("Digite a nova marca do carro: ")
            modelo = input("Digite o novo modelo do carro: ")
            ano = int(input("Digite o novo ano do carro: "))
            preco = float(input("Digite o novo preço do carro: "))
            self.carros[index] = Carro(marca, modelo, ano, preco)
            print("Carro atualizado com sucesso!")
        else:
            print("Número de carro inválido!")

    def excluir_carro(self):
        self.listar_carros()
        if not self.carros:
            return
        index = int(input("Digite o número do carro que deseja excluir: ")) - 1
        if 0 <= index < len(self.carros):
            del self.carros[index]
            print("Carro excluído com sucesso!")
        else:
            print("Número de carro inválido!")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar carro")
            print("2. Listar carros")
            print("3. Editar carro")
            print("4. Excluir carro")
            print("5. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.adicionar_carro()
            elif escolha == "2":
                self.listar_carros()
            elif escolha == "3":
                self.editar_carro()
            elif escolha == "4":
                self.excluir_carro()
            elif escolha == "5":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    concessionaria = Concessionaria()
    concessionaria.menu()
