CREATE TABLE IF NOT EXISTS utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);
INSERT INTO utilisateurs (nom) VALUES ('Admin'), ('User1'), ('User2');