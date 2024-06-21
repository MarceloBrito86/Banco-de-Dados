CREATE DATABASE SistemaEscolar_DB;
USE SistemaEscolar_DB;

CREATE TABLE Estudantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Professores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Disciplinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

CREATE TABLE Turmas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    disciplina_id INT,
    professor_id INT,
    semestre VARCHAR(10),
    horario VARCHAR(50),
    FOREIGN KEY (disciplina_id) REFERENCES Disciplinas(id),
    FOREIGN KEY (professor_id) REFERENCES Professores(id)
);

CREATE TABLE Matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudante_id INT,
    turma_id INT,
    data_matricula DATE,
    FOREIGN KEY (estudante_id) REFERENCES Estudantes(id),
    FOREIGN KEY (turma_id) REFERENCES Turmas(id)
);

CREATE TABLE Notas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula_id INT,
    nota DECIMAL(5, 2),
    data_avaliacao DATE,
    FOREIGN KEY (matricula_id) REFERENCES Matriculas(id)
);

INSERT INTO Estudantes (nome, data_nascimento, endereco, telefone, email)
VALUES ('João Silva', '2005-03-15', 'Rua A, 123', '99999-9999', 'joao@example.com'),
       ('Maria Souza', '2006-07-22', 'Rua B, 456', '98888-8888', 'maria@example.com');

INSERT INTO Professores (nome, data_nascimento, endereco, telefone, email)
VALUES ('Carlos Pereira', '1980-01-30', 'Rua C, 789', '97777-7777', 'carlos@example.com'),
       ('Ana Lima', '1985-05-10', 'Rua D, 101', '96666-6666', 'ana@example.com');

INSERT INTO Disciplinas (nome, descricao)
VALUES ('Matemática', 'Estudo dos números e suas operações.'),
       ('Português', 'Estudo da língua portuguesa.');

INSERT INTO Turmas (disciplina_id, professor_id, semestre, horario)
VALUES (1, 1, '2024-1', 'Segunda e Quarta, 10:00-12:00'),
       (2, 2, '2024-1', 'Terça e Quinta, 14:00-16:00');

INSERT INTO Matriculas (estudante_id, turma_id, data_matricula)
VALUES (1, 1, '2024-01-15'),
       (2, 2, '2024-01-15');

INSERT INTO Notas (matricula_id, nota, data_avaliacao)
VALUES (1, 8.5, '2024-05-20'),
       (2, 7.0, '2024-05-20');
       
SELECT E.nome, T.semestre, D.nome AS disciplina, P.nome AS professor
FROM Matriculas M
JOIN Estudantes E ON M.estudante_id = E.id
JOIN Turmas T ON M.turma_id = T.id
JOIN Disciplinas D ON T.disciplina_id = D.id
JOIN Professores P ON T.professor_id = P.id
WHERE T.id = 1;

SELECT E.nome AS estudante, D.nome AS disciplina, N.nota, N.data_avaliacao
FROM Notas N
JOIN Matriculas M ON N.matricula_id = M.id
JOIN Estudantes E ON M.estudante_id = E.id
JOIN Turmas T ON M.turma_id = T.id
JOIN Disciplinas D ON T.disciplina_id = D.id
WHERE E.id = 1;

SELECT T.semestre, D.nome AS disciplina, P.nome AS professor, T.horario
FROM Turmas T
JOIN Disciplinas D ON T.disciplina_id = D.id
JOIN Professores P ON T.professor_id = P.id;       