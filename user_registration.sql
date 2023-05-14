create database vsc;


use vsc;

CREATE TABLE users (
  username VARCHAR(255) primary key,
  saltedHash nvarchar(255),
  email nvarchar(40)

);

select*from users;
