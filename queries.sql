--1. Print the names of professors who work in departments that have fewer than 50 PhD students.

SELECT p.pname, d.dname,d.numphds FROM prof p
INNER JOIN dept d ON p.dname = d.dname WHERE d.numphds < 50;

--2. Print the names of the students with the lowest GPA.
SELECT name FROM student
WHERE gpa IN (
SELECT min(gpa) FROM student
);

-- 3. For each Computer Sciences class, print the class number, section number, and the average gpa of the students enrolled in the class section.

SELECT  e.cno,c.cname, e.sectno, AVG(s.gpa) AS Avg_GPA, COUNT(e.sid) FROM enroll e
JOIN student s ON e.sid = s.sid 
JOIN course c ON e.cno = c.cno WHERE c.dname = 'Computer Sciences'
GROUP BY e.cno, c.cname, e.sectno ORDER BY e.cno, e.sectno;


-- 4. Print the names and section numbers of all sections with more than six students enrolled in them.

SELECT e.sectno, e.dname,c.cname, COUNT(e.sid) FROM enroll e 
JOIN section s ON e.sectno = s.sectno AND e.cno = s.cno AND e.dname = s.dname
JOIN course c ON e.cno = c.cno AND e.dname = c.dname
GROUP BY e.sectno, e.dname, c.cname HAVING count(e.sid) > 6
ORDER BY e.dname, e.sectno, COUNT(e.sid);

-- 5. Print the name(s) and sid(s) of the student(s) enrolled in the most sections.

WITH record AS (
SELECT s.sid, s.name, COUNT(s.sid) FROM student s INNER JOIN
enroll e ON s.sid = e.sid GROUP BY s.sid, s.name
)
SELECT sid, name, COUNT FROM record WHERE COUNT IN (
SELECT MAX(count) FROM record
);

-- 6. Print names of departments with one or more majors under 18.

SELECT m.dname, COUNT(m.sid) FROM major m
JOIN student s on m.sid = s.sid GROUP BY m.dname, s.age HAVING s.age < 18;

-- 7. Print names and majors of students taking a "College Geometry" course.

WITH record AS(
SELECT e.sid, s.name, e.dname, c.cname FROM enroll e
JOIN course c ON e.cno = c.cno 
JOIN student s ON e.sid = s.sid GROUP BY e.sid, s.name, e.dname, c.cname
HAVING c.cname = 'College Geometry 1' OR c.cname = 'College Geometry 2'
) 
SELECT r.name, m.dname FROM record r
JOIN major m ON r.sid = m.sid;

-- 8. For those departments that have no major taking a College Geometry course print the department name and the number of PhD students in the department

WITH records AS(
WITH record AS(
SELECT e.sid, s.name, e.dname, c.cname FROM enroll e
JOIN course c ON e.cno = c.cno 
JOIN student s ON e.sid = s.sid GROUP BY e.sid, s.name, e.dname, c.cname
HAVING c.cname = 'College Geometry 1' OR c.cname = 'College Geometry 2'
) 
SELECT m.dname AS College_dept FROM record r
JOIN major m ON r.sid = m.sid GROUP BY m.dname
) SELECT dname, numphds FROM dept WHERE dname NOT IN(
SELECT College_dept FROM records );

-- 9. Print the names of students who are taking both a Computer Sciences course and a Mathematics course.

with record as (
select e1.sid as rec_id from enroll e1
join enroll e2 on e1.sid = e2.sid where
e1.dname in ('Mathematics', 'Computer Sciences') and 
e2.dname in  ('Mathematics', 'Computer Sciences') and e1.dname != e2.dname
)
select name from student
where sid in (select rec_id from record);

-- 10. Print the age difference between the oldest and the youngest Computer Sciences major.

SELECT MAX(s.age)-MIN(s.age) AS Diff_Between_Oldest_Youngest FROM student s 
JOIN major m ON s.sid = m.sid WHERE m.dname = 'Computer Sciences';

-- 11. For each department that has one or more majors with a GPA under 1.0, print the name of the department and the average GPA of its majors.

WITH record AS (
SELECT dname, COUNT(s.gpa), s.gpa FROM major m
JOIN student s ON m.sid = s.sid 
GROUP BY m.dname, s.gpa HAVING s.gpa < 1
)
SELECT dname, AVG(gpa) FROM record GROUP BY dname;

-- 12. Print the ids, names and GPAs of the students who are currently taking all the Civil Engineering courses.

SELECT sid, name, gpa FROM student WHERE sid = (
WITH records AS (
		SELECT e1.sid AS st_id, e1.cno AS one, e2.cno AS two FROM enroll e1 
		JOIN enroll e2 ON e1.sid = e2.sid WHERE e1.dname = 'Civil Engineering' 
		AND e2.dname = 'Civil Engineering'
		AND e1.cno != e2.cno)
	SELECT DISTINCT r.st_id FROM records r
	JOIN enroll e3 ON e3.sid = r.st_id WHERE e3.cno != r.one 
	AND e3.cno != r.two
	AND e3.dname = 'Civil Engineering'
)
