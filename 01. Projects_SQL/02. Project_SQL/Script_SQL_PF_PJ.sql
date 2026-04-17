CREATE DATABASE clientes_pj_pf;
USE clientes_pj_pf;

-- Tabela clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo_cliente ENUM('PF','PJ') NOT NULL,
    cpf_cnpj VARCHAR(20) UNIQUE,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela fornecedores
CREATE TABLE fornecedores (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- Tabela produtos
CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    id_fornecedor INT,
    estoque INT DEFAULT 0,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedores(id_fornecedor)
);

-- Tabela formas de pagamento
CREATE TABLE formas_pagamento (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    tipo_pagamento VARCHAR(50),  -- Ex: Cartão, Boleto, Pix
    dados_pagamento VARCHAR(100),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabela pedidos
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    data_pedido DATE NOT NULL,
    status_pedido VARCHAR(50), -- Ex: Em andamento, Entregue
    codigo_rastreio VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabela Itens pedidos
CREATE TABLE itens_pedido (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT,
    id_produto INT,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

-- Realização dos INSERT's

-- Clientes
INSERT INTO clientes (nome, tipo_cliente, cpf_cnpj, telefone, email) VALUES
('João Silva', 'PF', '123.456.789-00', '11999999999', 'joao@email.com'),
('Empresa XYZ', 'PJ', '12.345.678/0001-00', '11888888888', 'contato@xyz.com');

-- Fornecedores
INSERT INTO fornecedores (nome, telefone, email) VALUES
('Fornecedor A', '1112345678', 'fornecedorA@email.com'),
('Fornecedor B', '1123456789', 'fornecedorB@email.com');

-- Produtos
INSERT INTO produtos (nome, preco, id_fornecedor, estoque) VALUES
('Teclado Mecânico', 250.00, 1, 50),
('Mouse Gamer', 150.00, 2, 100);

-- Formas de pagamento
INSERT INTO formas_pagamento (id_cliente, tipo_pagamento, dados_pagamento) VALUES
(1, 'Cartão', 'Visa 1234'),
(1, 'Pix', 'joao@email.com');

-- Pedidos
INSERT INTO pedidos (id_cliente, data_pedido, status_pedido, codigo_rastreio) VALUES
(1, '2025-12-01', 'Em andamento', 'ABC123'),
(2, '2025-12-02', 'Entregue', 'XYZ987');

-- Itens do pedido
INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 2, 250.00),
(1, 2, 1, 150.00),
(2, 1, 5, 250.00);

SELECT * FROM clientes;
-- Puxar a informação aonde o status do pedido está em andamento
SELECT * FROM pedidos
WHERE status_pedido = 'Em andamento';

-- Atributo derivado para criação somando o produto da quantidade
-- pelo preço unitario fazendo um ALIAS de valor total e
-- agrupando por id_pedido
SELECT 
    id_pedido,
    SUM(quantidade * preco_unitario) AS valor_total
FROM itens_pedido
GROUP BY id_pedido;

-- Ordenação
SELECT 
    id_pedido,
    SUM(quantidade * preco_unitario) AS valor_total
FROM itens_pedido
GROUP BY id_pedido;

-- Usando o HAVING para responder os clientes que compraram mais de um item
SELECT id_cliente, COUNT(*) AS total_itens
FROM pedidos p
JOIN itens_pedido i ON p.id_pedido = i.id_pedido
GROUP BY id_cliente
HAVING COUNT(*) > 1;

-- Relacionando pedidos com cliente e produto com uso de JOINs
SELECT 
    p.id_pedido,
    c.nome AS cliente,
    pr.nome AS produto,
    i.quantidade,
    i.preco_unitario
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id_cliente
JOIN itens_pedido i ON p.id_pedido = i.id_pedido
JOIN produtos pr ON i.id_produto = pr.id_produto;

-- com fornecedor
SELECT pr.nome AS produto, f.nome AS fornecedor
FROM produtos pr
JOIN fornecedores f ON pr.id_fornecedor = f.id_fornecedor;

-- pedidos feitos por cliente
SELECT c.nome AS cliente, COUNT(p.id_pedido) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente;

-- tem algum vendedor que seja fornecedor também?
	SELECT c.nome AS cliente_e_vendedor
FROM clientes c
JOIN fornecedores f ON c.nome = f.nome;
-- Não tem kkkkkk

-- relação de produtos, fornecedores e estoque
SELECT pr.nome AS produto, f.nome AS fornecedor, pr.estoque
FROM produtos pr
JOIN fornecedores f ON pr.id_fornecedor = f.id_fornecedor;

-- Nome de fornecedor x nomes de produto
SELECT f.nome AS fornecedor, pr.nome AS produto
FROM fornecedores f
JOIN produtos pr ON f.id_fornecedor = pr.id_fornecedor
ORDER BY f.nome, pr.nome;




