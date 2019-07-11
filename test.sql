-- Create a new database called 'Student'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'Student'
)
CREATE DATABASE Student
GO

-- Get a list of databases
SELECT Student FROM sys.databases
GO

USE Student
GO

CREATE TABLE student(
    id INT,
    age INT
)
INSERT INTO Student VALUES(
    0001,
    18
)
GO
SELECT * FROM Student
GO
