create database UniversityDB;

use [UniversityDB]
GO

--Create table Departments
drop table if exists Departments;
Create table Departments
(
DepartmentID int identity(1,1) PRIMARY KEY,
DepartmentName varchar(100)
);

--Create table Students
drop table if exists Students;
create table Students
(
StudentID int identity(1,1) PRIMARY KEY,
Name varchar(100),
Age int,
DepartmentID int FOREIGN KEY REFERENCES Departments(DepartmentID)
);

--Create table Courses
drop table if exists Courses;
create table Courses
(
CourseID int identity(1,1),
CourseName varchar(100),
StudentID int FOREIGN KEY REFERENCES Students(StudentID)
);

--Insert query
insert into Departments values('Computer Science');
insert into Departments values('Commerce');
insert into Departments values('Bio Chemistry');
insert into Departments values('Artificial Intelligence');
insert into Departments values('Mechanical Engineering');


--Insert query
insert into Students values('Sankara',17,1);
insert into Students values('Raja',19,1);
insert into Students values('Repesh',18,2);
insert into Students values('Kamal',20,2);
insert into Students values('Swadesh',17,3);
insert into Students values('Ram Kumar',18,4);
insert into Students values('Sharmanil',28,2);
insert into Students values('Rajali',22,4);
insert into Students values('Neeraj',26,4);
insert into Students values('Vishal',17,3);
insert into Students values('Alice Johnson',25,5);


--Insert query
insert into Courses values('DBMS',1);
insert into Courses values('Operating Systems',1);
insert into Courses values('Commerce',2);
insert into Courses values('Advanced Commerce',2);
insert into Courses values('Industry Commerce',2);
insert into Courses values('Artificial Intelligence',3);
insert into Courses values('Artificial Intelligence',7);
insert into Courses values('Machine Learning',7);
insert into Courses values('Lab Engineering',5);
insert into Courses values('Thermo Chemistry',10);
insert into Courses values('Statistics',11);
insert into Courses values('Data Analysis',3);
insert into Courses values('History',null);
insert into Courses values('Literature',null);

--select individual table query
select * from Departments(nolock);
select * from Students(nolock);
Select * from Courses(nolock);

--Query-Based Questions
--Retrieve all student details along with their department names.
select s.StudentID,s.Name,D.DepartmentName
from 
Students s join Departments d on s.DepartmentID = d.DepartmentID;

--Find the names of all students who are enrolled in 'Artificial Intelligence'
select s.StudentID,s.Name,C.CourseName
from 
Students s join Courses c on s.StudentID = c.StudentID
where C.CourseName = 'Artificial Intelligence';

--Count how many students are in each department
select d.DepartmentID,d.DepartmentName,count(*) as [No of Student]
from 
Students s join Departments d on s.DepartmentID = d.DepartmentID
group by d.DepartmentID,d.DepartmentName

--List the courses taken by 'Alice Johnson'.
select s.StudentID,s.Name,C.CourseName
from 
Students s join Courses c on s.StudentID = c.StudentID
where s.Name = 'Alice Johnson';

--Find students who are enrolled in more than one course
;With CTE as
(select s.StudentID,count(*) as [Enrolled Course(s)]
from 
Students s join Courses c on s.StudentID = c.StudentID
group by s.StudentID)
select c.StudentID,s.Name,c.[Enrolled Course(s)] 
from CTE c join Students s on c.StudentID = s.StudentID 
where c.[Enrolled Course(s)] > 1

--Get the average age of students in each department.
;With CTE as
(select s.StudentID,s.Age,d.DepartmentID
from 
Students s join Departments d on s.DepartmentID = d.DepartmentID)
select c.DepartmentID, d.DepartmentName,avg(c.Age) 
from CTE c join Departments d  on c.DepartmentID = d.DepartmentID
group by c.DepartmentID,d.DepartmentName

--Find the department with the most students
;With CTE as
(select d.DepartmentID,count(*) cnt
from 
Students s join Departments d on s.DepartmentID = d.DepartmentID group by d.DepartmentID)
select top 1 * from CTE order by cnt desc

--List all students who are NOT enrolled in any course.
SELECT Students.Name 
FROM Students 
LEFT JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Courses.StudentID IS NULL;

--Retrieve students along with the total number of courses they are enrolled in.
select s.Name,t.cnt as Enrolled_Course from
(SELECT s.StudentID,count(*) cnt
FROM Students s JOIN Courses c ON s.StudentID = c.StudentID
group by s.StudentID)t join Students s on t.StudentID = s.StudentID

--Find students who belong to 'Computer Science' and are taking a course with 'Data' in its name.
SELECT Students.Name 
FROM Students 
JOIN Departments ON Students.DepartmentID = Departments.DepartmentID 
JOIN Courses ON Students.StudentID = Courses.StudentID 
WHERE Departments.DepartmentName = 'Computer Science' 
AND Courses.CourseName LIKE '%Data%';






