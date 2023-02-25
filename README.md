# Bus_Booking_management_system
DOCUMENT FOR BUS BOOKING SYSTEM
I have created this project with the help of mysql.connector instead of mysqlite3.

To : lucknow 
from : guna 
date:2022-11-30
                                            Steps for SQL:
Install MySQL command line client
Set password Piyush@123 at the time of installation
OR you can change project file by your own SQL password
Line number 3 in every sql.connect
mydb=sql.connect(
    host='localhost',
    user='root',
    passwd='Piyush@123',
    database='busbooking'
)
mycursor=mydb.cursor()
MySQL Installation
Watch YouTube video to download correct version of MySQL (GPL) and Installation steps. https://www.youtube.com/watch?v=mezkwKb_kkc
Or directly go to link
https://dev.mysql.com/downloads/
After installation execute following queries:
Create database busbooking;
Use busbooking;
Create table operator(OP_ID int, Name   varchar(20), Address  varchar(30) ,Phone_no  int, Email varchar (30));
Create table route(RT_ID int, St_Name  varchar(20), St_ID int);
Create table bus(Bus_ID int, Bus_type varchar(20), capacity int, Fare int, Opr_ID int, Route_ID int);
Create table running(Bs_ID int, Rn_dt  date , seat_avl int);
Create table passenger(name  varchar(20), no_seat int, age  int, booking_ref int Auto_increment, travel_on  date, desti   varchar(20), gender varchar(15), ph_no  int ,fare int, bus_dt varchar(20), booked_on date, bording_pt varchar(20),primary key(booking_ref ));
alter table bus add constraint bus_pk primary key(Bus_ID);
alter table operator add constraint op_pk primary key(OP_ID);
alter table bus add constraint bus_fk foreign key(Opr_ID) references operator(OP_ID);
alter table running add constraint run_fk foreign key(Bs_ID) references bus(Bus_ID);
insert into operator values(1,”kamla”,”ruthiyai”,123456,”kamla@g.com”);
insert into operator values(2,”shatabdi”,”raghogarh”,123456789,”shatabdi@g.com”);
insert into bus values(100,”2x2”,20,1000,1,10);
insert into bus values(200,”AC 2x2”,20,2000,2,20);
insert into running values(100,”2022-11-30”,15);
insert into running values(200,”2022-11-30”,10);
insert into route values(10,”lucknow”,32);
insert into route values(10,”guna”,50);
insert into route values(20,”lucknow”,32);
insert into route values(20,”guna”,50);
