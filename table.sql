-- Tabela clientes
CREATE TABLE clientes (
    id INT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    sexo CHAR(1) NOT NULL,
    raca VARCHAR(10) NOT NULL,
    saldo FLOAT NOT NULL
);

-- Tabela depositos
CREATE TABLE depositos (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    valor_deposito FLOAT NOT NULL,
    data_deposito TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Tabela saques
CREATE TABLE saques (
    id SERIAL PRIMARY KEY,
    cliente_id INT NOT NULL,
    valor_saque FLOAT NOT NULL,
    data_saque TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Tabela transferências 
CREATE TABLE transferencias (
    id SERIAL PRIMARY KEY,
    remetente_id INT NOT NULL,
    destinatario_id INT NOT NULL,
    valor FLOAT NOT NULL,
    data_transferencia TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (remetente_id) REFERENCES clientes(id),
    FOREIGN KEY (destinatario_id) REFERENCES clientes(id)
);

