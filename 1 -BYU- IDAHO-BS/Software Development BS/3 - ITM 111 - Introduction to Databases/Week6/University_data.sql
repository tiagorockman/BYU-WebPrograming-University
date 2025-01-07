Select * from department;

INSERT INTO department (department, department_code)
VALUES
('Computer Information Technology', 'ITM'),
('Economics', 'ECON'),
('Humanities and Philosophy', 'HUM');

SELECT * FROM college;

INSERT INTO college (college, department_code)
VALUES
('College of Physical Science and Engineering', 'ITM'),
('College of Business and Communication', 'ECON'),
('College of Language and Letters', 'HUM');

SELECT * FROM course;

INSERT INTO course (course_num, course_title, credits, college_id)
VALUES
(111, 'Intro to Databases', 3, (SELECT college_id FROM college WHERE college = 'College of Physical Science and Engineering')),
(388, 'Econometrics', 4, (SELECT college_id FROM college WHERE college = 'College of Business and Communication')),
(150, 'Micro Economics', 3, (SELECT college_id FROM college WHERE college = 'College of Business and Communication')),
(376, 'Classical Heritage', 2, (SELECT college_id FROM college WHERE college = 'College of Language and Letters'));

SELECT * FROM faculty;

INSERT INTO faculty (faculty_fname, faculty_lname)
VALUES
('Marty', 'Morring'),
('Nate', 'Norris'),
('Ben', 'Barrus'),
('John', 'Jensen'),
('Bill', 'Barney');

SELECT * FROM term;

INSERT INTO term (term_year, term)
VALUES
(2019, 'Fall'),
(2018, 'Winter');


SELECT * FROM section;

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Marty' AND faculty_lname = 'Morring'), 
  (SELECT course_num FROM Course WHERE course_num = '111'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  30);
  
/*  
INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Marty' AND faculty_lname = 'Morring'), 
  (SELECT course_num FROM Course WHERE course_num = '111'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  30);*/

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Nate' AND faculty_lname = 'Norris'), 
  (SELECT course_num FROM Course WHERE course_num = '150'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  50);
  
 /* INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Nate' AND faculty_lname = 'Norris'), 
  (SELECT course_num FROM Course WHERE course_num = '150'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  50);*/

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(2, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Nate' AND faculty_lname = 'Norris'), 
  (SELECT course_num FROM Course WHERE course_num = '150'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  50);
  
INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Ben' AND faculty_lname = 'Barrus'), 
  (SELECT course_num FROM Course WHERE course_num = '388'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  35);
  
  /*
  INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Ben' AND faculty_lname = 'Barrus'), 
  (SELECT course_num FROM Course WHERE course_num = '388'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  35);  
  */

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'John' AND faculty_lname = 'Jensen'), 
  (SELECT course_num FROM Course WHERE course_num = '376'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
  30);

/*INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'John' AND faculty_lname = 'Jensen'), 
  (SELECT course_num FROM Course WHERE course_num = '376'), 
  (SELECT term_id FROM Term WHERE term_year = 2019 AND term = 'Fall'),
30);*/

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(2, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Marty' AND faculty_lname = 'Morring'), 
  (SELECT course_num FROM Course WHERE course_num = '111'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  30);
  
/*  INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(2, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Marty' AND faculty_lname = 'Morring'), 
  (SELECT course_num FROM Course WHERE course_num = '111'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  30),*/

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(3, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Bill' AND faculty_lname = 'Barney'), 
  (SELECT course_num FROM Course WHERE course_num = '111'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  35);
  
/*INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(3, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Bill' AND faculty_lname = 'Barney'), 
  (SELECT course_num FROM Course WHERE course_num = '111'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  35);*/

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Nate' AND faculty_lname = 'Norris'), 
  (SELECT course_num FROM Course WHERE course_num = '150'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  50);
  
/*INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Nate' AND faculty_lname = 'Norris'), 
  (SELECT course_num FROM Course WHERE course_num = '150'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  50);
  */


INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(2, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'Nate' AND faculty_lname = 'Norris'), 
  (SELECT course_num FROM Course WHERE course_num = '150'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  50);

INSERT INTO Section (section_id, faculty_id, course_num, term_id, capacity)
VALUES
(1, 
  (SELECT faculty_id FROM Faculty WHERE faculty_fname = 'John' AND faculty_lname = 'Jensen'), 
  (SELECT course_num FROM Course WHERE course_num = '376'), 
  (SELECT term_id FROM Term WHERE term_year = 2018 AND term = 'Winter'),
  30);
  
  select * from section;
  
INSERT INTO Student (first_name, last_name, gender, city, state, birthdate) VALUES
('Paul', 'Miller', 'M', 'Dallas', 'TX', '1996-02-22'),
('Katie', 'Smith', 'F', 'Provo', 'UT', '1995-07-22'),
('Kelly', 'Jones', 'F', 'Provo', 'UT', '1998-06-22'),
('Devon', 'Merrill', 'M', 'Mesa', 'AZ', '2000-07-22'),
('Mandy', 'Murdock', 'F', 'Topeka', 'KS', '1996-11-22'),
('Alece', 'Adams', 'F', 'Rigby', 'ID', '1997-05-22'),
('Bryce', 'Carlson', 'M', 'Bozeman', 'MT', '1997-11-22'),
('Preston', 'Larsen', 'M', 'Decatur', 'TN', '1996-09-22'),
('Julia', 'Madsen', 'F', 'Rexburg', 'ID', '1998-09-22'),
('Susan', 'Sorensen', 'F', 'Mesa', 'AZ', '1998-08-09');

select * from enrollment;

INSERT INTO enrollment (enrollment_id, student_id, section_id, term_id, course_num, faculty_id)
VALUES
(1, (SELECT student_id FROM student WHERE first_name = 'Alece' AND last_name = 'Adams'),
    (SELECT section_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 3),
    (SELECT term_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 3),
    (SELECT course_num FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 3),
    (SELECT faculty_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 3)),

(2, (SELECT student_id FROM student WHERE first_name = 'Bryce' AND last_name = 'Carlson'),
    (SELECT section_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2),
    (SELECT term_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2),
    (SELECT course_num FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2),
    (SELECT faculty_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2)),

(3, (SELECT student_id FROM student WHERE first_name = 'Bryce' AND last_name = 'Carlson'),
    (SELECT section_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 1)),

(4, (SELECT student_id FROM student WHERE first_name = 'Bryce' AND last_name = 'Carlson'),
    (SELECT section_id FROM section WHERE course_num = '376' AND term_id = '2' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '376' AND term_id = '2' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '376' AND term_id = '2' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '376' AND term_id = '2' AND section_id = 1)),

(5, (SELECT student_id FROM student WHERE first_name = 'Devon' AND last_name = 'Merrill'),
    (SELECT section_id FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1)),

(6, (SELECT student_id FROM student WHERE first_name = 'Julia' AND last_name = 'Madsen'),
    (SELECT section_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT term_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT course_num FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT faculty_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2)),

(7, (SELECT student_id FROM student WHERE first_name = 'Katie' AND last_name = 'Smith'),
    (SELECT section_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1)),

(8, (SELECT student_id FROM student WHERE first_name = 'Kelly' AND last_name = 'Jones'),
    (SELECT section_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1)),

(9, (SELECT student_id FROM student WHERE first_name = 'Mandy' AND last_name = 'Murdock'),
    (SELECT section_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '388' AND term_id = '1' AND section_id = 1)),

(10, (SELECT student_id FROM student WHERE first_name = 'Mandy' AND last_name = 'Murdock'),
    (SELECT section_id FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '376' AND term_id = '1' AND section_id = 1)),

(11, (SELECT student_id FROM student WHERE first_name = 'Paul' AND last_name = 'Miller'),
    (SELECT section_id FROM section WHERE course_num = '111' AND term_id = '1' AND section_id = 1),
    (SELECT term_id FROM section WHERE course_num = '111' AND term_id = '1' AND section_id = 1),
    (SELECT course_num FROM section WHERE course_num = '111' AND term_id = '1' AND section_id = 1),
    (SELECT faculty_id FROM section WHERE course_num = '111' AND term_id = '1' AND section_id = 1)),

(12, (SELECT student_id FROM student WHERE first_name = 'Paul' AND last_name = 'Miller'),
    (SELECT section_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT term_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT course_num FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT faculty_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2)),

(13, (SELECT student_id FROM student WHERE first_name = 'Preston' AND last_name = 'Larsen'),
    (SELECT section_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT term_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT course_num FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2),
    (SELECT faculty_id FROM section WHERE course_num = '150' AND term_id = '2' AND section_id = 2)),

(14, (SELECT student_id FROM student WHERE first_name = 'Susan' AND last_name = 'Sorensen'),
    (SELECT section_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2),
    (SELECT term_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2),
    (SELECT course_num FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2),
    (SELECT faculty_id FROM section WHERE course_num = '111' AND term_id = '2' AND section_id = 2));





