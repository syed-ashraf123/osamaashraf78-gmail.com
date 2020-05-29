create table car(
SNo int not null primary key auto_increment,
dt datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
years int,
km int,
ml int,
en int,
pwr int,
st varchar(10) not null,
cm varchar(10) not null,
ct varchar(10) not null,
ty varchar(10) not null,
tran varchar(10) not null,
own varchar(10) not null
);