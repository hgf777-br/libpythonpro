from libpythonpro.span.enviador_de_email import Enviador
from libpythonpro.span.enviador_de_email import EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize("destinatario", ["hgf777@gmail.com", "katia@inovegrafica.com.br"])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'hgf@inovegrafica.com.br',
        'Curso de Python',
        'teste de texto do documento'
    )
    assert destinatario in resultado


@pytest.mark.parametrize("destinatario", ["hgf777Agmail.com", "katia"])
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    resultado = None
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            destinatario,
            'hgf@inovegrafica.com.br',
            'Curso de Python',
            'teste de texto do documento'
        )

    return resultado
