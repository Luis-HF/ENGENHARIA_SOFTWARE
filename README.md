# 👁️ Padrão de Projeto: Observer (Comportamental)

## O que é o Observer?

O **Observer** é um padrão de projeto comportamental que estabelece uma relação **1 → N** entre objetos.  
Ou seja, quando **um objeto muda**, todos os seus observadores são **notificados automaticamente**.

Ele é muito usado quando partes diferentes do sistema precisam reagir a um mesmo evento, sem criar alto acoplamento entre elas.

---

## Qual problema o Observer resolve?

Imagine um sistema em que:

- vários módulos precisam ser avisados quando algum evento acontece;
- você não quer criar dependências diretas entre esses módulos;
- você precisa adicionar ou remover “interessados” no evento sem alterar o código principal.

O Observer resolve isso ao permitir que:

- o **Sujeito (Subject)** emita atualizações,
- diversos **Observadores** fiquem “inscritos”,
- e todos sejam avisados automaticamente quando algo mudar.

Não é necessário que os objetos se conheçam diretamente — apenas seguem o protocolo de notificação.

---

##  Estrutura clássica do Observer

- **Subject (Observado)**  
  - Mantém uma lista de observadores  
  - Tem métodos `subscribe()`, `unsubscribe()` e `notify()`

- **Observer (Observador)**  
  - Possui o método `update()`  
  - Reage quando o Subject envia uma notificação

---
