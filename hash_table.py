class TabelaHash:
    def __init__(self, tamanho_max):
        self.tamanho = 0
        self.tamanho_max = tamanho_max
        self.tabela = [[] for _ in range(250)]

    def hash(self, nome):
        nome_sem_espacos = str(nome).replace(' ', '')
        hash_value = sum(ord(letra) for letra in nome_sem_espacos)
        return (hash_value % 250)

    def inserir(self, tripulante):
        posicao = self.hash(tripulante.nome)
        tripulante.codigo = posicao + 1

        if self.tamanho < self.tamanho_max:
            self.tabela[posicao].append(tripulante)
            self.tamanho = self.tamanho + 1
        else:
            print("Navio-cruzeiro Cheio!")

    def deletar(self, nome):
        posicao = self.hash(nome)

        for tripulante in self.tabela[posicao]:
            if tripulante.nome == nome:
                self.tabela[posicao].remove(tripulante)
                self.tamanho = self.tamanho - 1
                return

        print("Tripulante não encontrado!")

    def buscar(self, nome):
        posicao = self.hash(nome)

        for tripulante in self.tabela[posicao]:
            if tripulante.nome == nome:
                return tripulante

    def imprimir_tripulantes(self):
        for lista in self.tabela:
            for tripulante in lista:
                print(
                    f"Código: {tripulante.codigo}, Nome: {tripulante.nome}, Idade: {tripulante.idade}")
