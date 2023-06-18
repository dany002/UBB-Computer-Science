create database personschannelsphpdb;

create table Persons( id int auto_increment primary key, name varchar(200), age int, gender varchar(30) );

create table Channels( id int auto_increment primary key, ownerid int, name varchar(200), description varchar(200), subscribers text, foreign key(ownerid) REFERENCES Persons(id));

insert into Persons(name,age,gender) values("Dani",21,"male");

insert into Persons(name,age,gender) values("Florin",24,"male");

insert into Channels(ownerid,name,description,subscribers) values(1,'test name 1','test description 1','Dani -> 18/06/2023.');

