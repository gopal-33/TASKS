-- create sex as an enum datatype

CREATE TYPE sex
AS
ENUM('m', 'f');



-- create table student

CREATE TABLE IF NOT EXISTS student(
    sid INTEGER NOT NULL,
    sname VARCHAR,
    gender sex,
    age INTEGER,
    year INTEGER,
    gpa FLOAT,
    PRIMARY KEY(sid)
);



-- copy student data from csv file

COPY student
FROM '/tmp/data/student.csv'
DELIMITER '	'
CSV;



-- create table dept

CREATE TABLE IF NOT EXISTS dept(
    dname VARCHAR,
    numphds INTEGER,
    PRIMARY KEY(dname)
);



-- copy dept data from csv file

COPY dept
FROM '/tmp/data/dept.csv'
DELIMITER '	'
CSV;



-- create table prof

CREATE TABLE IF NOT EXISTS prof(
    pname VARCHAR,
    dname VARCHAR,
    PRIMARY KEY(pname)
);



-- copy prof data from csv file

COPY prof
FROM '/tmp/data/prof.csv'
DELIMITER '	'
CSV;



-- create table course

CREATE TABLE IF NOT EXISTS course(
   cno  INTEGER NOT NULL,
   cname VARCHAR,
   dname VARCHAR,
   primary key(cno,dname),
   FOREIGN KEY(dname) REFERENCES dept(dname)
);



-- copy course data from csv file
COPY course
FROM '/tmp/data/course.csv'
DELIMITER '	'
CSV;



-- create table major

CREATE TABLE IF NOT EXISTS major(
   dname VARCHAR,
   sid INTEGER,
   PRIMARY KEY(dname, sid),
   FOREIGN KEY(dname) REFERENCES dept(dname),
   FOREIGN KEY(sid) REFERENCES student(sid)
);



-- copy major data from csv file

COPY major
FROM '/tmp/data/major.csv'
DELIMITER '	'
CSV;



-- create table section

CREATE TABLE IF NOT EXISTS section(
   dname VARCHAR,
   cno INTEGER,
   sectno INTEGER,
   pname VARCHAR,
   PRIMARY KEY(dname, cno, sectno),
   FOREIGN KEY(dname, cno) REFERENCES course(dname, cno),
   FOREIGN KEY(pname) REFERENCES prof(pname)
);



-- copy section data from csv file

COPY section
FROM '/tmp/data/section.csv'
DELIMITER '	'
CSV;



-- create table Enroll  

CREATE TABLE IF NOT EXISTS enroll(
   sid INTEGER,
   grade FLOAT,
   dname VARCHAR,
   cno INTEGER,
   sectno INTEGER,
   PRIMARY KEY(sid, dname, cno, sectno),
   FOREIGN KEY(dname, cno, sectno) REFERENCES section(dname, cno, sectno),
   FOREIGN KEY(sid) REFERENCES student(sid)
);



-- Copy Enroll data from csv file

COPY enroll
FROM '/tmp/data/enroll.csv'
DELIMITER '	'
CSV;
