from unittest.mock import Mock
import pytest
from libpythonpro.span.main import EnviadorDeSpam
from libpythonpro.span.modelos import Usuario


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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "hgf777@gmail.com",
        "Curso de Python",
        "Confira todo o conteudo"
    )

    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Henrique", email="hgf777@gmail.com")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "katia@gmail.com",
        "Curso de Python",
        "Confira todo o conteúdo"
    )

    enviador.enviar.assert_called_once_with(
        "katia@gmail.com",
        "hgf777@gmail.com",
        "Curso de Python",
        "Confira todo o conteúdo"
    )
