from libpythonpro.span.modelos import Usuario
from time import sleep


class Conexao:
    def __init__(self):
        sleep(1)

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass


class Sessao:
    contador = 0
    usuarios = []

    def salvar(self, usuario: Usuario):
        Sessao.contador += 1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.usuarios

    def roll_back(self):
        self.usuarios.clear()

    def fechar(self):
        pass
