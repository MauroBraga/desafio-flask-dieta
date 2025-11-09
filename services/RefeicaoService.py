

class RefeicaoService:
    def __init__(self, refeicao_repository):
        self.refeicao_repository = refeicao_repository

    def create(self, dados_refeicao):
        # Lógica para criar uma nova refeição
        return self.refeicao_repository.adicionar(dados_refeicao)

    def findAll(self):
        # Lógica para obter todas as refeições
        return self.refeicao_repository.listar_todas()

    def update(self, id_refeicao, dados_atualizados):
        # Lógica para atualizar uma refeição existente
        return self.refeicao_repository.atualizar(id_refeicao, dados_atualizados)

    def delete(self, id_refeicao):
        # Lógica para deletar uma refeição
        return self.refeicao_repository.remover(id_refeicao)