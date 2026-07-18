use mini_erp;

create table if not exists usuario
(
	id integer not null auto_increment,
	nome varchar(50) not null,
	email varchar(50) not null,
	data_nascimento date not null,
	primary key(id)
);