import pymysql
import sys




if __name__=="__main__":
	addr = sys.argv[1]
	db = pymysql.connect(addr,"root","123456",charset="utf8")
	cur = db.cursor()

	#创建数据库`game_lobby`
	#if not exists xxx 如果存在不则创建,不存在则创建
	cur.execute("create database if not exists `game_lobby` default charset=utf8;")
	cur.execute("use `game_lobby;")

	#创建用户表
	cur.execute("""
		create table if not exists user (
		id int primary key auto_increment,
		user varchar(15) not null,
		password varchar(32) not null,
		name varchar(18),
		email varchar(18) not null,
		identity_card char(18) not null)
		""")

	#创建游戏表
	cur.execute("""
		create table if not exists game (
		id int primary key auto_increment,
		name varchar(18) not null);
		""")

	#创建用户游戏记录表
	cur.execute("""
		create table if not exists `game_record` (
		id int primary key auto_increment,
		`game_id` int,
		`user_id` int,
		constraint gid foreign key(`game_id`) references game(id) on delete set null on update cascade,
		constraint uid foreign key(`user_id`) references user(id) on delete set null on update cascade);
		""")

	db.commit()
	cur.close()
	db.close()