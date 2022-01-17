START TRANSACTION;

-- Use (swtich to) webapp_db 
USE webapp_db;

-- Drop the Persons table if it exists
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Persons;
DROP TABLE IF EXISTS Credentials;

-- Create the Credentias table and set the uniqe auto_incrementing ID
CREATE TABLE Credentials (
    credId int NOT NULL AUTO_INCREMENT,
    uname varchar(255) NOT NULL,
    pwd varchar(255) NOT NULL,

   
);

-- Create the Persons table and set the uniqe auto_incrementing ID
CREATE TABLE Persons (
    PersonID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255),
    FirstName varchar(255),
    email varchar(255),
    addr varchar(1024),
    credId int NOT NULL,

    PRIMARY KEY (PersonID),
    FOREIGN KEY (credId) REFERENCES Credentials(credId)
);



-- Create the Books table
CREATE TABLE Books (
    BookID int NOT NULL AUTO_INCREMENT,
    Title varchar(255),
    Author varchar(255),
    

    PRIMARY KEY (BookID),
    
);

