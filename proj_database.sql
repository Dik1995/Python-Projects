# Register Database
use register;
#Details Table
create table Details(Name varchar(50),last varchar(50),contact int,email varchar(50),question varchar(50),answer varchar(50),password varchar(50));
select * from details;
alter table details add column answer varchar(50)
alter table details drop column CPassword  
alter table details add constraint  primary key (Email);

# QR code Database
use qr
show databases

#Employee Table In QR Database
create table employee(
emp_id int,
emp_name varchar(50),
emp_department varchar(50),
emp_designation varchar(50)
);
select * from Employee2;

select * from employee
