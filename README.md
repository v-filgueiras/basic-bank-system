# 🏦 Sistema Bancário CLI com Python

Este é um projeto simples de um **sistema bancário de terminal** utilizando **orientação a objetos em Python**, com suporte a cadastro de clientes, criação de contas, movimentações financeiras e extrato de operações.

---

## ✅ Funcionalidades

- Cadastro de clientes
- Criação de conta bancária (corrente ou poupança)
- Depósito de valores
- Saque com verificação de saldo
- Consulta de extrato com histórico de transações
- Validações básicas de entrada

---

## 🧱 Estrutura das Classes

### `Cliente`
- Armazena dados como nome, sobrenome, idade, sexo, raça e ID.
- Exibe as informações do cliente.

### `Conta`
- Ligada a um cliente.
- Possui número da conta, tipo (corrente/poupança), saldo e histórico.
- Métodos para sacar, depositar e exibir extrato.

---

## 💡 Exemplo de Uso

=== Menu Principal ===
1 - Cadastrar Cliente
2 - Criar Conta
3 - Mostrar Informações do Cliente
4 - Depositar
5 - Sacar
6 - Ver Extrato
7 - Sair

## 🏗️ Tabelas para Banco de Dados

```sql
CREATE TABLE clientes (
    id INT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    sexo CHAR(1) NOT NULL,
    raca VARCHAR(10) NOT NULL,
    saldo FLOAT NOT NULL
);

CREATE TABLE depositos (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    valor_deposito FLOAT NOT NULL,
    data_deposito TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE saques (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    valor_saque FLOAT NOT NULL,
    data_saque TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE transferencias (
    id SERIAL PRIMARY KEY,
    remetente_id INT NOT NULL,
    destinatario_id INT NOT NULL,
    valor FLOAT NOT NULL,
    data_transferencia TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (remetente_id) REFERENCES clientes(id),
    FOREIGN KEY (destinatario_id) REFERENCES clientes(id)
);
