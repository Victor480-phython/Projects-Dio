

# Desafio DIO: Gerenciamento de Clientes, Funcionários e Ordens de Serviço

## 1. Introdução

Este projeto consiste em um **banco de dados relacional** para gerenciar clientes, funcionários e ordens de serviço de uma oficina. A solução envolve a criação de tabelas, inserção de dados, consultas básicas, consultas avançadas com `JOIN`, cálculos e filtros.

O objetivo é demonstrar **habilidades em SQL**, como:

* Criação de tabelas;
* Inserção de dados;
* Consultas simples e complexas;
* Uso de funções agregadas (`COUNT`);
* Filtragem com `WHERE` e `HAVING`;
* Ordenação de dados com `ORDER BY`;
* Criação de colunas derivadas.

---

## 2. Criação das Tabelas

### 2.1 Tabela `clientes`

```sql
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100)
);
```

* Armazena informações dos clientes.
* `id_cliente` é chave primária, garantindo unicidade.
* Campos `nome`, `telefone` e `email` armazenam dados pessoais.

### 2.2 Tabela `employee`

```sql
CREATE TABLE employee (
    id_employee INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departament VARCHAR(100),
    email VARCHAR(100),
    funcao VARCHAR(100),
    salario DECIMAL(10,2)
);
```

* Armazena dados dos funcionários.
* `salario` utiliza tipo `DECIMAL` para valores monetários.
* `departament` e `funcao` ajudam a organizar funções internas.

### 2.3 Tabela `ordens_servico`

```sql
CREATE TABLE ordens_servico (
    id_os INT AUTO_INCREMENT PRIMARY KEY,
    data_abertura DATE,
    id_cliente INT,
    id_employee INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_employee) REFERENCES employee(id_employee)
);
```

* Registra ordens de serviço realizadas.
* Contém chaves estrangeiras (`id_cliente` e `id_employee`) para relacionar clientes e funcionários.

---

## 3. Inserção de Dados

### 3.1 Inserindo clientes

```sql
INSERT INTO clientes (nome, telefone, email) VALUES
('Joao silva', '42998447732', 'joaozinho@gmail.com'),
('Maria Coralina', '4382938292', 'Mariazinha@gmail.com');
```

* Adiciona clientes iniciais na tabela `clientes`.

### 3.2 Inserindo funcionários

```sql
INSERT INTO employee (nome, departament, email, funcao, salario) VALUES
('Carlos Andrade', 'Mecânica', 'carlos@oficina.com', 'Mecânico', 3500.00),
('Fernanda Lopes', 'Elétrica', 'fernanda@oficina.com', 'Eletricista', 3800.00),
('Roberto Costa', 'Pintura', 'roberto@oficina.com', 'Pintor', 3200.00),
('Juliana Silva', 'Atendimento', 'juliana@oficina.com', 'Atendente', 2900.00);
```

* Adiciona funcionários com diferentes funções e salários.

### 3.3 Inserindo ordens de serviço

```sql
INSERT INTO ordens_servico (data_abertura, id_cliente, id_employee) VALUES
('2025-01-10', 1, 1),
('2025-01-12', 2, 2),
('2025-01-15', 3, 3),
('2025-01-18', 1, 1),
('2025-01-20', 4, 2);
```

* Registra ordens vinculadas a clientes e funcionários.

---

## 4. Consultas SQL

### 4.1 Seleção básica

```sql
SELECT * FROM clientes;
SELECT * FROM employee;
SELECT * FROM ordens_servico;
```

* Exibe todos os registros das tabelas.

### 4.2 Criação de coluna derivada

```sql
SELECT
    id_employee,
    nome,
    salario,
    salario * 0.90 AS salario_com_desconto
FROM employee;
```

* Calcula o salário com desconto de 10% sem alterar os dados originais.

### 4.3 Ordenação de dados

```sql
SELECT 
    id_cliente,
    nome,
    telefone, 
    email
FROM clientes
ORDER BY nome ASC;
```

* Organiza os clientes em ordem alfabética.

```sql
SELECT id_os, data_abertura, id_cliente, id_employee
FROM ordens_servico
ORDER BY data_abertura DESC;
```

* Lista as ordens mais recentes primeiro.

### 4.4 Funções agregadas e filtros com `HAVING`

```sql
SELECT id_employee, COUNT(*) AS total_ordens
FROM ordens_servico
GROUP BY id_employee
HAVING COUNT(*) > 1;
```

* Conta quantas ordens cada funcionário atendeu.
* Exibe apenas aqueles com mais de 1 ordem.

### 4.5 Relacionamento entre tabelas (JOIN)

```sql
SELECT
    os.id_os,
    os.data_abertura,
    c.nome AS nome_cliente,
    e.nome AS nome_funcionario
FROM ordens_servico os
JOIN clientes c ON os.id_cliente = c.id_cliente
JOIN employee e ON os.id_employee = e.id_employee;
```

* Combina informações de ordens, clientes e funcionários.
* Semelhante ao `PROCV` do Excel, mas mais poderoso.

### 4.6 Combinação de agregação e JOIN

```sql
SELECT
    e.nome,
    e.salario,
    COUNT(os.id_os) AS total_ordens
FROM employee e
LEFT JOIN ordens_servico os ON e.id_employee = os.id_employee
GROUP BY e.id_employee
HAVING COUNT(os.id_os) > 1
ORDER BY total_ordens DESC;
```

* Conta as ordens de cada funcionário.
* Ordena pelo total de ordens e mostra apenas os funcionários com mais de 1 ordem.
* Uso de `LEFT JOIN` garante que mesmo funcionários sem ordens apareçam se desejado (no caso, filtrados pelo `HAVING`).

---
