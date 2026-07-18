use mini_erp;

create table if not exists fornecedor
(
	id integer not null auto_increment,
	razao_social varchar(50) not null,
	nome_fantasia varchar(50) not null,
	cnpj varchar(14) not null,
	sla_atendimento int not null,
	primary key(id)
);