from libpythonpro.span.modelos import Usuario


def teste_salvar_usuario(sessao):
    usuario = Usuario(nome="Henrique", email="hgf777@gmail.com")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def teste_listar_usuario(sessao):
    usuarios = [Usuario("Henique", email="hgf777@gmail.com"),
                Usuario("Katia", email="katia@gmail.com"),
                Usuario("Bruna", email="bruna@gmail.com"),
                Usuario("Luísa", email="luisa@gmail.com")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
