class Consulta():
    def __init__(self, id,nome, email, telefone, data, estado, descricao):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data = data
        self.estado = estado
        self.descricao = descricao


class Editar():
    def __init__(self, nome, id, email, telefone, data, estado, descricao):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data = data
        self.estado = estado
        self.descricao = descricao
        self.id = id

