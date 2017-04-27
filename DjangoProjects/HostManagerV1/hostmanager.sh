#!/bin/bash
#Created on 2016-12-1 @Author:Guolikai
#Description:HostManager System
USER='root'
PWD='123456'
HOST='localhost'
mysqlconn="mysql -h${HOST} -u${USER} -p${PWD}"
createdatabase='create database if not exists hostmanager character set utf8;;'
$mysqlconn -e "$createdatabase"
createuserinfo='create table hostmanager.userinfo(id int(2) auto_increment,username varchar(100) NOT NULL,password varchar(100) NOT NULL,primary key(id,username));'
$mysqlconn -e "$createuserinfo"
descuserinfo=' desc hostmanager.hostmanager.userinfo'
$mysqlconn -e "$descuserinfo"
insertuserinfo1="insert into hostmanager.userinfo (username,password) values('root',md5('123456','admin'));"
$mysqlconn -e "$insertuserinfo1"
insertuserinfo2="insert into hostmanager.userinfo (username,password,remarks) values('glk',md5('123456'),'user');"
$mysqlconn -e "$insertuserinfo2"
selectuserinfo='select * from hostmanager.hostmanager.userinfo;'
$mysqlconn -e "$selectuserinfo"

createhostgroups='create table hostmanager.hostgroups(id int(2) auto_increment ,ip varchar(100) NOT NULL,hostname varchar(100) NOT NULL,port int(2),hostgroup varchar(100) NOT NULL,username varchar(100) NOT NULL,remarks varchar(100),primary key(id,username));'
$mysqlconn -e "$createuserloced"
inserthostgroups1="insert into hostmanager.hostgroups (ip,hostname,port,hostgroup,username,remarks) values('172.16.1.100','zabbix_server.1.100',22,'zabbix_server','root','centos7');"
inserthostgroups2="insert into hostmanager.hostgroups (ip,hostname,port,hostgroup,username,remarks) values('172.16.1.101','kvm01.1.101',22,'kvm01','root','centos7');"
inserthostgroups3="insert into hostmanager.hostgroups (ip,hostname,port,hostgroup,username,remarks) values('172.16.1.110','muban_node1.1.110',22,'muban','root','centos7');"
inserthostgroups4="insert into hostmanager.hostgroups (ip,hostname,port,hostgroup,username,remarks) values('172.16.1.120','muban_node2.1.120',22,'muban','root','centos7');"
$mysqlconn -e "$inserthostgroups1"
$mysqlconn -e "$inserthostgroups2"
$mysqlconn -e "$inserthostgroups3"
$mysqlconn -e "$inserthostgroups4"
selecthostgroups='select * from hostmanager.hostmanager.hostgroups;'
$mysqlconn -e "$selecthostgroups"



createhostuserpassword='create table hostmanager.hostuserpassword (id int(2) auto_increment ,ip varchar(100) NOT NULL,username varchar(100) NOT NULL,password varchar(100) NOT NULL,remarks varchar(100),primary key(id,username));'
$mysqlconn -e "$createhostuserpassword"
descaccountdetails=' desc hostmanager.hostuserpassword'
$mysqlconn -e "$deschostuserpassword"
inserthostuserpassword1='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.100','root','123456','admin');'
inserthostuserpassword2='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.101','root','123456','admin');'
inserthostuserpassword3='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.110','root','123456','admin');'
inserthostuserpassword4='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.120','root','123456','admin');'
inserthostuserpassword5='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.130','root','123456','admin');'
inserthostuserpassword6='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.140','root','123456','admin');'
$mysqlconn -e "$inserthostuserpassword1"
$mysqlconn -e "$inserthostuserpassword2"
$mysqlconn -e "$inserthostuserpassword3"
$mysqlconn -e "$inserthostuserpassword4"
$mysqlconn -e "$inserthostuserpassword5"
$mysqlconn -e "$inserthostuserpassword6"

inserthostuserpassword7='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.100','glk','123456','user');'
inserthostuserpassword8='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.110','glk','123456','user');'
inserthostuserpassword9='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.120','glk','123456','user');'
inserthostuserpassword10='insert into hostmanager.hostuserpassword (ip,username,password,remarks) values('172.16.1.101','glk','123456','user');'
$mysqlconn -e "$inserthostuserpassword7"
$mysqlconn -e "$inserthostuserpassword8"
$mysqlconn -e "$inserthostuserpassword9"
$mysqlconn -e "$inserthostuserpassword10"


createuserlogs='create table hostmanager.userlogs(id int(2) auto_increment primary key,user varchar(100) NOT NULL,time varchar(100) NOT NULL,username varchar(100) NOT NULL,ip varchar(100) NOT NULL,cmd varchar(100) NOT NULL);'
$mysqlconn -e "$createuserlogs"

#mysqldump -uroot -p123456 hostmanager > /root/hostmanager.sql

#172.16.1.112: zabbix_server.1.100
#172.16.1.100: zabbix_server.1.100
#172.16.1.140: moban_node04.1.140
#172.16.1.130: muban_node3
#172.16.1.101: kvm01.1.101
#172.16.1.110: muban_node1.1.110
#172.16.1.120: muban_node2.1.120
#172.16.1.115: tomcat1.1.115
