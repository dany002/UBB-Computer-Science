create database usersfilesphpdb;

create table Users( id int auto_increment primary key, username varchar(200), password varchar(200));

create table Files(id int auto_increment primary key, userid int, filename varchar(200), filepath varchar(200), size int, foreign key(userid) references Users(id));

insert into Files(userid,filename,filepath,size) Values(1,"filename 1","filepath 1",1);

insert into Files(userid,filename,filepath,size) Values(1,"filename 2","filepath 2",2);

insert into Files(userid,filename,filepath,size) Values(1,"filename 3","filepath 3",3);

insert into Files(userid,filename,filepath,size) Values(1,"filename 4","filepath 4",4);

insert into Files(userid,filename,filepath,size) Values(1,"filename 5","filepath 5",5);

insert into Files(userid,filename,filepath,size) Values(1,"filename 6","filepath 6",6);

insert into Files(userid,filename,filepath,size) Values(1,"filename 7","filepath 7",7);

insert into Files(userid,filename,filepath,size) Values(1,"filename 1","filepath 8",8);
