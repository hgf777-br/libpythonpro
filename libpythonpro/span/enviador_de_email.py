class Enviador:
    def __init__(self):
        self.qtd_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido("Invalido")
        self.qtd_emails_enviados += 1
        return remetente

class EmailInvalido(Exception):
    pass