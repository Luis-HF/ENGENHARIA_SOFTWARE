#Nesse padrão eu optei por utilizar apenas um exemplo, já que é um padrão um pouco mais complexo de implementar e é mais simples explicar direto na aplicação.

#O exemplo consiste em utilizar Observer para mostrar notícias da barbearia, tais como descontos, cupons, cortes e serviços novos.

class NewsPublisher:
    def __init__(self):
        self.observers = []
        self.latest_news = None

    def add_observer(self, observer):
        self.observers.append(observer)
        print(f"Observer {observer.__class__.__name__} registrado.")

    def remove_observer(self, observer):
        self.observers.remove(observer)
        print(f"Observer {observer.__class__.__name__} removido.")

    def notify_observers(self):
        print("\nNotificando observers...")
        for observer in self.observers:
            observer.update(self.latest_news)

    def publish_news(self, news):
        print(f"\nPublicando notícia: {news}")
        self.latest_news = news
        self.notify_observers()


class EmailSubscriber:
    def update(self, news):
        print(f"[Email] Nova notícia recebida: {news}")

class SMSSubscriber:
    def update(self, news):
        print(f"[SMS] Notificação: {news}")

class AppSubscriber:
    def update(self, news):
        print(f"[App] Push recebido: {news}")


if __name__ == "__main__":
    publisher = NewsPublisher()

    email = EmailSubscriber()
    sms = SMSSubscriber()
    app = AppSubscriber()

    publisher.add_observer(email)
    publisher.add_observer(sms)
    publisher.add_observer(app)

    publisher.publish_news("Novo jogo lançado hoje!")
    publisher.publish_news("Promoção imperdível por 24 horas!")

    publisher.remove_observer(sms)

    publisher.publish_news("Atualização importante do sistema.")