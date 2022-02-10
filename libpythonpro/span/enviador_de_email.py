class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido("Invalido")
        return remetente
    
class EmailInvalido(Exception):
    pass