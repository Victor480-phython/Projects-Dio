USE schema_bd_dio;

-- Criação das respectivas tabelas

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);
CREATE TABLE employee (
	id_employee INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departament VARCHAR (100),
    email VARCHAR(100),
    funcao VARCHAR(100),
    salario DECIMAL(10,2)
);
CREATE TABLE ordens_servico (
    id_os INT AUTO_INCREMENT PRIMARY KEY,
    data_abertura DATE,
    id_cliente INT,
    id_employee INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_employee) REFERENCES employee(id_employee)
);

-- Inserção dos dados nas tabelas
-- Inserindo clientes

INSERT INTO clientes (nome, telefone, email) VALUES
('Joao silva', '42998447732', 'joaozinho@gmail.com'),
('Maria Coralina', '4382938292', 'Mariazinha@gmail.com');
	
    SELECT * FROM clientes;

-- Inserindo employee

INSERT INTO employee (nome, departament, email, funcao, salario) VALUES
('Carlos Andrade', 'Mecânica', 'carlos@oficina.com', 'Mecânico', 3500.00),
('Fernanda Lopes', 'Elétrica', 'fernanda@oficina.com', 'Eletricista', 3800.00),
('Roberto Costa', 'Pintura', 'roberto@oficina.com', 'Pintor', 3200.00),
('Juliana Silva', 'Atendimento', 'juliana@oficina.com', 'Atendente', 2900.00);

	SELECT * FROM employee;

INSERT INTO clientes (nome, telefone, email) VALUES
('João Silva', '11999999999', 'joao@email.com'),
('Maria Souza', '11888888888', 'maria@email.com'),
('Pedro Santos', '11777777777', 'pedro@email.com'),
('Ana Oliveira', '11666666666', 'ana@email.com');

	SELECT * FROM clientes;
    
INSERT INTO ordens_servico (data_abertura, id_cliente, id_employee) VALUES
('2025-01-10', 1, 1),
('2025-01-12', 2, 2),
('2025-01-15', 3, 3),
('2025-01-18', 1, 1),
('2025-01-20', 4, 2);
SELECT * FROM ordens_servico;
-- Criando uma coluna e definindo alias com desconto de 10%
SELECT
	id_employee,
    nome,
    salario,
    -- atributo derivado
    salario *0.90 AS salario_com_desconto
FROM employee;

-- Ordenando por nome em ordem alfabética crescente
SELECT 
	id_cliente,
	nome,
	telefone, email
FROM clientes
ORDER BY nome ASC;

-- Ordem de serviço mais recentes
SELECT id_os, data_abertura, id_cliente, id_employee
FROM ordens_servico
ORDER BY data_abertura DESC;

-- Condições de filtro em grupos usando HAVING
SELECT id_employee, COUNT(*) AS total_ordens
FROM ordens_servico
GROUP BY id_employee
HAVING COUNT(*) >1;

-- Usando os famosos PROCV do SQL os JOIN's
SELECT
	os.id_os,
    os.data_abertura,
    c.nome AS nome_cliente,
    e.nome AS nome_funcionario
FROM ordens_servico os
JOIN clientes c ON os.id_cliente = c.id_cliente
JOIN employee e ON os.id_employee = e.id_employee;

-- Combinando tudo

SELECT
    e.nome,
    e.salario,
    COUNT(os.id_os) AS total_ordens
FROM employee e
LEFT JOIN ordens_servico os ON e.id_employee = os.id_employee
GROUP BY e.id_employee
HAVING COUNT(os.id_os) > 1
ORDER BY total_ordens DESC;
