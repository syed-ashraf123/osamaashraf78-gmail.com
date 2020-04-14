alter table customers
add unique key(email_address) ;
alter table customers
change column number_of_complaints number_of_complaints int default 0;
insert into customers(customer_id,first_name,last_name)
values(1,'John','Micheal');

alter table customers//used for modification
modify customer_id int(55) auto_increment;

select * from customers;