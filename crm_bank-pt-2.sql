CREATE DATABASE crm_bank;
USE crm_bank;
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contacts (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE opportunities (
    opportunity_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    value DECIMAL(10, 2),
    stage VARCHAR(50),
    close_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    contact_id INT,
    activity_type VARCHAR(50),
    subject VARCHAR(100),
    description TEXT,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE SET NULL
);

INSERT INTO customers (name, address, city, state, postal_code, country, phone, email)
VALUES ('Empresa Exemplo', 'Rua Exemplo, 123', 'Lisboa', 'Lisboa', '1000-000', 'Portugal', '211234567', 'contato@exemplo.com');

INSERT INTO contacts (customer_id, first_name, last_name, phone, email)
VALUES (1, 'João', 'Silva', '211234568', 'joao.silva@exemplo.com');

INSERT INTO opportunities (customer_id, name, description, value, stage, close_date)
VALUES (1, 'Projeto Exemplo', 'Descrição do projeto', 10000.00, 'Negociação', '2024-12-31');

INSERT INTO activities (customer_id, contact_id, activity_type, subject, description, due_date)
VALUES (1, 1, 'Reunião', 'Reunião inicial', 'Discutir detalhes do projeto', '2024-06-30');

SELECT * FROM customers;
SELECT * FROM contacts;
SELECT * FROM opportunities;
SELECT * FROM activities;