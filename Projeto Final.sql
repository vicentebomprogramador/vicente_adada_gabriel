
DROP DATABASE IF EXISTS projeto_final;
CREATE DATABASE projeto_final;
USE projeto_final;
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS alunos;
DROP TABLE IF EXISTS notas;
DROP TABLE IF EXISTS materias;
SET FOREIGN_KEY_CHECKS = 1;
CREATE TABLE alunos (
    matricula INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100),
    turma VARCHAR(20) NOT NULL
   
);
CREATE TABLE materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) UNIQUE NOT NULL
);
CREATE TABLE notas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricula INT,
    materia_id INT, 
    nota1 FLOAT DEFAULT 0,
    nota2 FLOAT DEFAULT 0,
    FOREIGN KEY (matricula) REFERENCES alunos(matricula),
    FOREIGN KEY (materia_id) REFERENCES materias(id)
);
INSERT INTO materias (nome) VALUES
('Levantamento de requisitos'),
('Desenvolver algoritmos'),
('Banco de dados');


SELECT * FROM projeto_final.notas;
