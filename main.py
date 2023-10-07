from faker import Faker
from hash_table import TabelaHash
from utils import adicionar_tripulante, adicionar_tripulantes, consultar_tripulante

faker = Faker(locale='pt-BR')
Faker.seed(0)

navio_cruzeiro_hash = TabelaHash(50)

if __name__ == "__main__":
    while True:
        print()
        print("Menu:")
        print("1. Adicionar tripulante")
        print("2. Consultar tripulante")
        print("3. Adicionar tripulantes aleatoriamente")
        print("4. Imprimir tripulantes")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do tripulante: ")
            idade = int(input("Idade: "))
            adicionar_tripulante(navio_cruzeiro_hash, nome, idade)

        elif escolha == '2':
            nome = input("Nome do tripulante para buscar: ")
            consultar_tripulante(navio_cruzeiro_hash, nome)

        elif escolha == '3':
            quantidade = int(input("Quantidade que deseja inserir: "))
            navio_cruzeiro_hash = adicionar_tripulantes(
                navio_cruzeiro_hash, quantidade)

        elif escolha == '4':
            navio_cruzeiro_hash.imprimir_tripulantes()

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Digite uma opção entre 1 e 5.")
