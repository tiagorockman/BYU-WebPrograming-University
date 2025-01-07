-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`department` ;

CREATE TABLE IF NOT EXISTS `mydb`.`department` (
  `department` VARCHAR(45) NULL,
  `department_code` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`department_code`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`college`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`college` ;

CREATE TABLE IF NOT EXISTS `mydb`.`college` (
  `college_id` INT NOT NULL AUTO_INCREMENT,
  `college` VARCHAR(150) NULL,
  `department_code` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`college_id`),
  INDEX `fk_college_department1_idx` (`department_code` ASC) VISIBLE,
  CONSTRAINT `fk_college_department1`
    FOREIGN KEY (`department_code`)
    REFERENCES `mydb`.`department` (`department_code`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`student`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`student` ;

CREATE TABLE IF NOT EXISTS `mydb`.`student` (
  `student_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `gender` VARCHAR(1) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(2) NULL,
  `birthdate` DATE NULL,
  PRIMARY KEY (`student_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`term`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`term` ;

CREATE TABLE IF NOT EXISTS `mydb`.`term` (
  `term_id` INT NOT NULL AUTO_INCREMENT,
  `term_year` CHAR(4) NULL,
  `term` VARCHAR(10) NULL,
  PRIMARY KEY (`term_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`course` ;

CREATE TABLE IF NOT EXISTS `mydb`.`course` (
  `course_num` INT NOT NULL,
  `course_title` VARCHAR(45) NULL,
  `credits` INT NOT NULL,
  `college_id` INT NOT NULL,
  PRIMARY KEY (`course_num`),
  INDEX `fk_course_college1_idx` (`college_id` ASC) VISIBLE,
  CONSTRAINT `fk_course_college1`
    FOREIGN KEY (`college_id`)
    REFERENCES `mydb`.`college` (`college_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`faculty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`faculty` ;

CREATE TABLE IF NOT EXISTS `mydb`.`faculty` (
  `faculty_id` INT NOT NULL AUTO_INCREMENT,
  `faculty_fname` VARCHAR(25) NULL,
  `faculty_lname` VARCHAR(25) NULL,
  PRIMARY KEY (`faculty_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`section`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`section` ;

CREATE TABLE IF NOT EXISTS `mydb`.`section` (
  `section_id` INT NOT NULL,
  `capacity` INT NULL,
  `term_id` INT NOT NULL,
  `course_num` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  PRIMARY KEY (`section_id`, `term_id`, `course_num`, `faculty_id`),
  INDEX `fk_section_term1_idx` (`term_id` ASC) VISIBLE,
  INDEX `fk_section_course1_idx` (`course_num` ASC) VISIBLE,
  INDEX `fk_section_faculty1_idx` (`faculty_id` ASC) VISIBLE,
  CONSTRAINT `fk_section_term1`
    FOREIGN KEY (`term_id`)
    REFERENCES `mydb`.`term` (`term_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_course1`
    FOREIGN KEY (`course_num`)
    REFERENCES `mydb`.`course` (`course_num`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_section_faculty1`
    FOREIGN KEY (`faculty_id`)
    REFERENCES `mydb`.`faculty` (`faculty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`enrollment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`enrollment` ;

CREATE TABLE IF NOT EXISTS `mydb`.`enrollment` (
  `enrollment_id` INT NOT NULL,
  `student_id` INT NOT NULL,
  `section_id` INT NOT NULL,
  `term_id` INT NOT NULL,
  `course_num` INT NOT NULL,
  `faculty_id` INT NOT NULL,
  PRIMARY KEY (`enrollment_id`),
  INDEX `fk_enrollment_student1_idx` (`student_id` ASC) VISIBLE,
  INDEX `fk_enrollment_section1_idx` (`section_id` ASC, `term_id` ASC, `course_num` ASC, `faculty_id` ASC) VISIBLE,
  CONSTRAINT `fk_enrollment_student1`
    FOREIGN KEY (`student_id`)
    REFERENCES `mydb`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_enrollment_section1`
    FOREIGN KEY (`section_id` , `term_id` , `course_num` , `faculty_id`)
    REFERENCES `mydb`.`section` (`section_id` , `term_id` , `course_num` , `faculty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

/*********************************************************************************************************/
/************************************INSERT***************************************************************/
/*********************************************************************************************************/

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




/*********************************************************************************************************/
/************************************QUERY***************************************************************/
/*********************************************************************************************************/
-- 1
SELECT first_name AS fname, last_name AS lname, DATE_FORMAT(birthdate, '%e %M, %Y') AS 'Sept Birthdays' FROM student WHERE MONTH(birthdate)   = 9;


-- 2
SELECT *, concat(a.Years , ' - Yrs, ' , a.Days ,' - Days') AS 'Years and Days'  FROM (
SELECT  last_name AS lname, first_name AS fname, floor(datediff(current_date(), birthdate)/365) AS Years, datediff(current_date(), birthdate) % 365 AS Days
  FROM student ORDER BY birthdate ASC) AS A;
  
-- 3
select s.first_name, s.last_name from enrollment as e 
inner join faculty as f on f.faculty_id = e.faculty_id and f.faculty_fname = 'John' and f.faculty_lname = 'Jensen'
inner join student as s on s.student_id = e.student_id
order by s.last_name;

-- 4
select f.faculty_fname, f.faculty_lname  from enrollment as e 
inner join student as s on s.student_id = e.student_id and s.first_name = 'Bryce'
inner join term as t on t.term_id = e.term_id and t.term_year = 2018
inner join faculty as f on f.faculty_id = e.faculty_id
order by f.faculty_lname;

-- 5
select  s.first_name as fname, s.last_name as lname from enrollment as e 
inner join student as s on s.student_id = e.student_id
inner join term as t on t.term_id = e.term_id and t.term_year = 2019 and t.term = 'Fall'
inner join faculty as f on f.faculty_id = e.faculty_id
inner join course as c on c.course_num = e.course_num and c.course_title = 'Econometrics'
order by s.last_name;

-- 6
select d.department_code, c.course_num, c.course_title from enrollment as e 
inner join student as s on s.student_id = e.student_id and s.first_name = 'Bryce' and s.last_name = 'Carlson'
inner join term as t on t.term_id = e.term_id and t.term_year = 2018 and t.term = 'Winter'
inner join course as c on c.course_num = e.course_num
inner join college as co on co.college_id = c.college_id
inner join department d on d.department_code = co.department_code
order by c.course_title;

-- 7
select t.term, t.term_year, count(*) as Enrollment from enrollment as e 
inner join term as t on t.term_id = e.term_id and t.term_year = 2019 and t.term = 'Fall'
group by t.term, t.term_year;

-- 8 
select c.college, count(*) from college c
inner join course co on c.college_id = co.college_id
group by c.college
order by c.college;

-- 9 
select * FROM (
select f.faculty_fname as fname, f.faculty_lname as lname, SUM(sec.capacity) as TeachingCapacity from enrollment as e 
inner join section as sec on sec.section_id = e.section_id and e.term_id = sec.term_id and e.course_num = sec.course_num and e.faculty_id = sec.faculty_id 
inner join student as s on s.student_id = e.student_id
inner join term as t on t.term_id = e.term_id and t.term_year = 2018 and t.term = 'Winter'
inner join faculty as f on f.faculty_id = e.faculty_id
group by f.faculty_fname, f.faculty_lname
) AS A order by TeachingCapacity;

-- 10 
SELECT * FROM (
select s.last_name as lname, s.first_name as fname, SUM(c.credits) Credits from enrollment as e 
inner join section as sec on sec.section_id = e.section_id and e.term_id = sec.term_id and e.course_num = sec.course_num and e.faculty_id = sec.faculty_id 
inner join student as s on s.student_id = e.student_id
inner join term as t on t.term_id = e.term_id and t.term_year = 2019 and t.term = 'Fall'
inner join faculty as f on f.faculty_id = e.faculty_id
inner join course as c on c.course_num = e.course_num
group by s.last_name , s.first_name 
) AS A 
order by Credits DESC;
