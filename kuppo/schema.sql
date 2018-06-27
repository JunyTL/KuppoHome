DROP TABLE IF EXISTS user;		
DROP TABLE IF EXISTS calander;	
DROP TABLE IF EXISTS notice;		
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS photo;

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,		
	username TEXT UNIQUE NOT NULL,
	password TEXT NOT NULL,
	email TEXT NOT NULL
);

CREATE TABLE calander (
	id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE notice (
	id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE post (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	author_id INTEGER NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	title TEXT NOT NULL,
	body TEXT NOT NULL,
	FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE photo (
	id INTEGER PRIMARY KEY AUTOINCREMENT
);