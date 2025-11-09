from flask_login import current_user
from config.database import db
from models.refeicao import Refeicao


class RefeicaoService:


    def create(self, dados_refeicao):
        nome = dados_refeicao.get('nome')
        descricao = dados_refeicao.get('descricao')
        dt_criacao = dados_refeicao.get('data_hora')
        tipo = dados_refeicao.get('tipo')
        usuario_id = current_user.id

        if nome and descricao and dt_criacao and tipo:
            try:
                nova_refeicao = Refeicao(
                    nome=nome,
                    descricao=descricao,
                    dt_criacao=dt_criacao,
                    tipo=tipo,
                    usuario_id=usuario_id
                )
                db.session.add(nova_refeicao)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return {'message': 'Erro ao criar a refeição: ' + str(e)}, 500

            return {'message': 'Refeição criada com sucesso!'}, 201
        return {'message': 'Nome, descrição, data_hora, tipo são obrigatórios!'}, 400


    def findAll(self):
        usuario_id = current_user.id
        refeicoes = Refeicao.query.filter_by(usuario_id=usuario_id).all()
        if refeicoes:
            refeicao_list = [{
                'id': refeicao.id,
                'nome': refeicao.nome,
                'descricao': refeicao.descricao,
                'data_hora': refeicao.dt_criacao,
                'tipo': refeicao.tipo
            } for refeicao in refeicoes]
            return {'refeicoes': refeicao_list}, 200

        return {'message': 'Usuário não encontrado!'}, 404

    def update(self, id_refeicao, dados_atualizados):
        nome = dados_atualizados.get('nome')
        descricao = dados_atualizados.get('descricao')
        dt_criacao = dados_atualizados.get('data_hora')
        tipo = dados_atualizados.get('tipo')
        usuario_id = current_user.id

        refeicao = Refeicao.query.filter_by(id=id_refeicao).all()

        if refeicao and refeicao.usuario_id == usuario_id:
            if nome:
                refeicao.nome = nome
            if descricao:
                refeicao.descricao = descricao
            if dt_criacao:
                refeicao.dt_criacao = dt_criacao
            if tipo:
                refeicao.tipo = tipo

            db.session.commit()
            return {'message': 'Refeição atualizada com sucesso!'}, 200
        return {'message': 'Refeição não encontrada!'}, 404

    def delete(self, id_refeicao):
        usuario_id = current_user.id
        refeicao = Refeicao.query.filter_by(id=id_refeicao).all()

        if refeicao and refeicao.usuario_id == usuario_id:
            db.session.delete(refeicao)
            db.session.commit()
            return {'message': 'Refeição deletada com sucesso!'}, 200
        return {'message': 'Refeição não encontrada!'}, 404