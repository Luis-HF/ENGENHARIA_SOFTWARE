# Padrão Singleton (Criacional)

## O que é o Padrão Singleton?

O **Singleton** é um padrão de projeto do grupo **Criacional** que garante que uma classe tenha **apenas uma única instância** durante toda a execução do programa.  
Além disso, ele fornece um **ponto global de acesso** a essa instância.

Isso significa que, independentemente de quantas vezes você tente criar o objeto, o sistema sempre retornará **a mesma instância compartilhada**.

---

##  Qual problema o Singleton resolve?

Existem situações em que o sistema precisa manter **um único objeto centralizado**, seja por consistência, desempenho ou controle.  
Esse padrão é utilizado quando:

- É necessário evitar múltiplas instâncias conflitantes  
- Um recurso deve ser acessado globalmente  
- O estado compartilhado precisa ser consistente  
- Há dados sensíveis que não podem existir em cópias separadas  

---

##  Exemplo do Problema (Barbearia)

No sistema de agendamentos da barbearia, toda a aplicação precisa acessar **as mesmas configurações globais**, como:

- Porta do banco de dados  
- Chave de segurança  
- Configurações gerais do sistema  
- Variáveis essenciais para o funcionamento  

Se cada parte do código criasse sua própria instância da classe de configurações, isso poderia causar:

❌ Valores divergentes  
❌ Conflitos de portas ou chaves  
❌ Inconsistências difíceis de rastrear  
❌ Comportamentos inesperados entre módulos diferentes  

O Singleton resolve esse problema garantindo:

✔️ Apenas **uma única** instância da classe de configurações  
✔️ Todos os módulos acessam os **mesmos valores**  
✔️ Qualquer alteração se reflete automaticamente no sistema todo  

---

## 🧠 Por que usar Singleton nesse caso?

Porque as configurações do sistema são:

- Únicas  
- Compartilhadas  
- Críticas para o funcionamento  
- Sensíveis a inconsistências  

O Singleton é *exatamente* o padrão que impede a criação acidental de múltiplas instâncias e mantém tudo sincronizado.

---
