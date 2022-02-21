import pytest
from libpythonpro.span.enviador_de_email import Enviador
from libpythonpro.span.main import EnviadorDeSpam
from libpythonpro.span.modelos import Usuario

class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qtd_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario("Henrique", email="hgf777@gmail.com"),
            Usuario("Katia", email="katia@gmail.com"),
            Usuario("Bruna", email="bruna@gmail.com")
        ],
        [
            Usuario("Luísa", email="luisa@gmail.com")
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "hgf777@gmail.com",
        "Curso de Python",
        "Confira todo o conteudo"
    )

    assert len(usuarios) == enviador.qtd_emails_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Henrique", email="hgf777@gmail.com")
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "katia@gmail.com",
        "Curso de Python",
        "Confira todo o conteúdo"
    )

    assert enviador.parametros_de_envio == (
        "katia@gmail.com",
        "hgf777@gmail.com",
        "Curso de Python",
        "Confira todo o conteúdo"
    )