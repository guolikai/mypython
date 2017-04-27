#!/bin/bash
#Created on 2016-11-17 @Author:Guolikai
#Description:¿¿¿¿bankdata¿mysql¿¿
mysqlconn="mysql -uroot -p123456"

createdatabase='create database if not exists bankdata character set utf8;;'
$mysqlconn -e "$createdatabase"

createuserinfo='create table bankdata.userinfo(id int(2) auto_increment,username varchar(100) NOT NULL,password varchar(100) NOT NULL,current_money int(2) NOT NULL,credit_money int(2) NOT NULL,primary key(id,username));'
$mysqlconn -e "$createuserinfo"
descuserinfo=' desc bankdata.userinfo'
$mysqlconn -e "$descuserinfo"
insertuserinfo1="insert into bankdata.userinfo (username,password,current_money,credit_money) values('user01',md5('123456'),20000,0);"
$mysqlconn -e "$insertuserinfo1"
insertuserinfo2="insert into bankdata.userinfo (username,password,current_money,credit_money) values('user02',md5('654321'),20000,0);"
#insertuserinfo2="insert into bankdata.userinfo (username,password,current_money,credit_money) values('user02',123456,20000,0);"
$mysqlconn -e "$insertuserinfo2"
selectuserinfo='select * from bankdata.userinfo;'
$mysqlconn -e "$selectuserinfo"

createuserloced='create table bankdata.userlocked(id int(2) primary key auto_increment,username varchar(100) NOT NULL);'
$mysqlconn -e "$createuserloced"
insertuserlocked="insert into bankdata.userlocked(username) values('glk');"
$mysqlconn -e "$insertuserlocked"
selectuserlocked='select * from bankdata.userlocked;'
$mysqlconn -e "$selectuserlocked"

createaccountdetails='create table bankdata.accountdetails(id int(2) primary key auto_increment,trans_date varchar(100) NOT NULL,trans_account varchar(100) NOT NULL,trans_amount int(2) NOT NULL,other_account  varchar(100) NOT NULL,description varchar(100) NOT NULL);'
$mysqlconn -e "$createaccountdetails"
descaccountdetails=' desc bankdata.accountdetails'
$mysqlconn -e "$descaccountdetails"
#mysqldump -uroot -p123456 bankdata > /root/bankdata.sql
