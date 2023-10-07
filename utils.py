import random
from faker import Faker
from crew import Tripulante
from hash_table import TabelaHash

faker = Faker(locale='pt-BR')
Faker.seed(0)


def adicionar_tripulantes(navio, quantidade):
    for i in range(quantidade):
        tripulante = Tripulante(faker.name(), random.randint(20, 60))
        navio.inserir(tripulante)
    return navio


def adicionar_tripulante(navio: TabelaHash, nome, idade, ):
    tripulante = Tripulante(nome, idade)
    navio.inserir(tripulante)
    return navio


def consultar_tripulante(navio: TabelaHash, nome):
    tripulante = navio.buscar(nome)

    if tripulante:
        print(
            f"Código: {tripulante.codigo}, Nome: {tripulante.nome}, Idade: {tripulante.idade}")

    else:
        print(f"{nome} não está no navio!")
