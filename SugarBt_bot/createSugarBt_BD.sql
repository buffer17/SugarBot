use SugarBt;

drop table bakery;
drop table iceCream;
drop table chocolate;
drop table milk;
drop table fruits;

create table bakery (
	bakery_id INT AUTO_INCREMENT PRIMARY KEY,
	name varchar(50),
	gram float
);

create table iceCream (
	iceCream_id INT AUTO_INCREMENT PRIMARY KEY,
	name varchar(50),
	gram float
);

create table chocolate (
	chocolate_id INT AUTO_INCREMENT PRIMARY KEY,
	name varchar(50),
	gram float
);

create table milk (
	milk_id INT AUTO_INCREMENT PRIMARY KEY,
	name varchar(50),
	gram float
);

create table fruits (
	fruits_id INT AUTO_INCREMENT PRIMARY KEY,
	name varchar(50),
	gram float
);

insert into bakery value (null, 'Булочки из сладкого дрожжевого теста', 12.50);
insert into bakery value (null, 'Хлеб белый пшеничный', 5.73);
insert into bakery value (null, 'Хлеб пшеничный цельнозерновой', 4.34);

insert into iceCream value (null, 'Мороженое', 21.22);

insert into chocolate value (null, 'Шоколад белый', 57.5);
insert into chocolate value (null, 'Шоколадный батончик', 52.10);
insert into chocolate value (null, 'Шоколад молочный', 51.50);
insert into chocolate value (null, 'Шоколад тёмный', 23.99);

insert into milk value (null, 'Кефир', 4.61);
insert into milk value null, 'Сыр сливочный', 3.76);
insert into milk value (null, 'Сметана', 0.22);
insert into milk value (null, 'Масло сливочное', 0.1);
insert into milk value (null, 'Молоко цельное', 4.7);
insert into milk value (null, 'Молоко сгущённое', 54.40);

insert into fruits value (null, 'Яблоки', 12.3);
insert into fruits value (null, 'Черешня', 13.2);
insert into fruits value (null, 'Слива', 10.9);
insert into fruits value (null, 'Персики садовые', 4.5);
insert into fruits value (null, 'Малина садовая', 7.3);
insert into fruits value (null, 'Земляника садовая', 7.8);
insert into fruits value (null, 'Дыня', 16);
insert into fruits value (null, 'Груша', 10.5);
insert into fruits value (null, 'Апельсин', 7.1);
insert into fruits value (null, 'Арбуз', 0.8);


