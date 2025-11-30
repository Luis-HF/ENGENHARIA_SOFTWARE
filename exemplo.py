class Singleton: #define a classe
    _instance = None  #a única instância
    _initialized = False   # evita reinicialização em __init__

    def __new__(cls, *args, **kwargs): #construtor da classe. Recebe o primeiro argumento, que vai dizer se já foi criado ou não e define os outros argumentos como genéricos, para aumentar a flexibilidade da classe e possibilitar seu uso com diferentes APIs, por exemplo.
        if cls._instance is None: #verifica se cls (classe) é nulo, ou seja, se a instância única já foi criada. Se sim, ele retorna a instância para a chamada. Se não, ele cria a instância.
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, valor): #inicialização dos atributos. Se a instância já foi criada, não faz nada. Mas se ainda não foi criada, ele inicializa seus atributos.
        if not self._initialized:
            self.valor = valor      # inicializa apenas uma vez
            Singleton._initialized = True


a = Singleton(10) #tenta criar duas instâncias da classe Singleton.
b = Singleton(999)

print(a.valor) #o valor da primeia instância é exibido
print(b.valor) #a segunda instância é, na verdade, a primeira. Como os atributos já foram inicializados, b é apenas uma cópia de a.
print(a is b)


#Agora que um código simples usando esse padrão foi mostrado, vamos para uma aplicação real:
#O código abaixo simula um ambiente de controle de acesso ao banco de dados, no qual apenas uma instância pode estar acessando o banco por vez.

class DatabaseConnection:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Criando conexão com o banco pela primeira vez...")
            cls._instance = super().__new__(cls)
        return cls._instance
    
#até aqui o código é extremamente parecido

    def __init__(self, host, user, password):
        if not self._initialized:
            self.host = host #alguns atributos a mais são colocados para simular a conexão com o db.
            self.user = user
            self.password = password
            self.connected = True
            print("Conexão estabelecida com sucesso!")
            DatabaseConnection._initialized = True
        else:
            print("Conexão já existente reaproveitada.")


db1 = DatabaseConnection("localhost", "admin", "123") #gerenciador de conexão à um banco de dados.
db2 = DatabaseConnection("servidor_remoto", "root", "senha_errada")

print("\nMesma instância?", db1 is db2)
print("Host utilizado:", db1.host)
