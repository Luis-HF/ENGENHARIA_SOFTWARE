# Padrão de Projeto: Adapter (Estrutural)

## O que é o Adapter?

O **Adapter** é um padrão de projeto estrutural que permite que duas interfaces incompatíveis trabalhem juntas.  
Ele atua como um *adaptador* criando uma camada intermediária que converte uma interface existente para o formato esperado por outro componente.

A principal vantagem é que **nenhuma das classes originais precisa ser alterada**.

---

## Qual problema o Adapter resolve?

Esse padrão é usado quando:

- Você possui um código legado que funciona bem;
- Deseja integrar um novo módulo, biblioteca ou serviço;
- **Mas as interfaces são incompatíveis**;
- E você não pode modificar o código antigo (para não quebrar o sistema);
- Nem modificar o novo módulo (porque você não tem controle sobre ele).

O Adapter permite que os dois lados conversem corretamente, convertendo dados e chamadas de um formato para outro.
