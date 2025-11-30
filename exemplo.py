#Como primeiro exemplo, irei mostrar um uso simples no qual fazemos a conexão entre um sistema antigo e um sistema novo. Adapter será utilizado para fazer a comunicação entre os dois.

# Classe antiga (o código legado)
class SistemaAntigo:
    def enviar_mensagem(self, texto):
        print(f"[Antigo] Mensagem enviada: {texto}")


# Nova classe que queremos usar, mas com interface diferente
class NovaAPI:
    def send(self, msg):
        print(f"[NovaAPI] Enviando: {msg}")


# Adapter: faz NovaAPI parecer com o SistemaAntigo
class Adapter:
    def __init__(self, nova_api):
        self.nova_api = nova_api

    def enviar_mensagem(self, texto):
        # converte a chamada esperada pelo sistema antigo
        self.nova_api.send(texto)

# sistema antigo funciona normalmente
antigo = SistemaAntigo()
antigo.enviar_mensagem("Olá mundo!")

# integração de API nova usando o Adapter
nova_api = NovaAPI()
adaptado = Adapter(nova_api)

# agora a nova API funciona como se fosse o sistema antigo
adaptado.enviar_mensagem("Mensagem através do Adapter!")


#Para o exemplo prático, vamos supor que queremos que o login na barbearia como cliente possa ser realizado por meio do google também. Para isso podemos utilizar o adapter:

class BarbeariaLoginSystem:
    def login_usuario(self, nome, email):
        print(f"[Barbearia] Login realizado: {nome} ({email})")


# API do Google (interface incompatível)
class GoogleLoginAPI:
    def login_google(self):
        # normalmente isso viria da Google OAuth
        return {
            "fullName": "Luis Henrique",
            "mail": "luis@example.com",
            "token": "XYZ123456"
        }


# Adapter: converte dados da Google para o formato da barbearia
class GoogleToBarbeariaAdapter:
    def __init__(self, google_api, barbearia_sistema):
        self.google_api = google_api
        self.barbearia_sistema = barbearia_sistema

    def login_usuario(self):
        dados_google = self.google_api.login_google()

        # Converte para o formato que a barbearia espera
        nome = dados_google["fullName"]
        email = dados_google["mail"]

        # Faz o login no sistema da barbearia
        self.barbearia_sistema.login_usuario(nome, email)

google_api = GoogleLoginAPI()
barbearia = BarbeariaLoginSystem()

adaptador = GoogleToBarbeariaAdapter(google_api, barbearia)
adaptador.login_usuario()