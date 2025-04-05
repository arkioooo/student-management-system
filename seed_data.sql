-- Clear all existing data and reset IDs
TRUNCATE grades, enrollments, users, students, teachers, courses RESTART IDENTITY CASCADE;

-- Students
INSERT INTO students (reg_no, name, admission_year, department) VALUES
('S100', 'John Doe', 2021, 'CSE'),
('S101', 'Alice Smith', 2021, 'EE'),
('S102', 'Bob Johnson', 2022, 'CE'),
('S103', 'Clara Brown', 2023, 'CE'),
('S104', 'David Wilson', 2023, 'ECE'),
('S105', 'Ella Davis', 2021, 'ECE'),
('S106', 'Frank Miller', 2020, 'CSE'),
('S107', 'Grace Lee', 2021, 'ECE'),
('S108', 'Henry Taylor', 2023, 'ME'),
('S109', 'Isla Thomas', 2020, 'CE'),
('S110', 'Jack White', 2020, 'CSE'),
('S111', 'Katie Harris', 2022, 'ECE'),
('S112', 'Leo Martin', 2020, 'EE'),
('S113', 'Mia Clark', 2023, 'CSE'),
('S114', 'Noah Lewis', 2021, 'CE'),
('S115', 'Olivia Hall', 2020, 'CSE'),
('S116', 'Paul Allen', 2021, 'CSE'),
('S117', 'Queenie Young', 2022, 'ECE'),
('S118', 'Ryan Scott', 2020, 'CSE'),
('S119', 'Sophia Adams', 2023, 'EE');

-- Teachers
INSERT INTO teachers (teacher_id, name) VALUES
('T201', 'Dr. Alan Turing'), ('T202', 'Dr. Ada Lovelace'), ('T203', 'Dr. Grace Hopper'), 
('T204', 'Dr. Linus Torvalds'), ('T205', 'Dr. Tim Berners-Lee'),
('T206', 'Dr. Margaret Hamilton'), ('T207', 'Dr. Donald Knuth'), ('T208', 'Dr. Barbara Liskov'), 
('T209', 'Dr. John McCarthy'), ('T210', 'Dr. Dennis Ritchie');

-- CS-themed Courses
INSERT INTO courses (course_id, course_name, teacher_id) VALUES
(1, 'Introduction to Programming', 'T201'),
(2, 'Data Structures', 'T202'),
(3, 'Algorithms', 'T203'),
(4, 'Computer Networks', 'T204'),
(5, 'Operating Systems', 'T205'),
(6, 'Database Systems', 'T206'),
(7, 'Software Engineering', 'T207'),
(8, 'Web Development', 'T208'),
(9, 'Artificial Intelligence', 'T209'),
(10, 'Machine Learning', 'T210'),
(11, 'Compiler Design', 'T201'),
(12, 'Distributed Systems', 'T202'),
(13, 'Cybersecurity', 'T203'),
(14, 'Cloud Computing', 'T204'),
(15, 'Blockchain Technology', 'T205'),
(16, 'Mobile App Development', 'T206'),
(17, 'Human Computer Interaction', 'T207'),
(18, 'Natural Language Processing', 'T208'),
(19, 'Data Mining', 'T209'),
(20, 'Computer Graphics', 'T210');

-- Enrollments and Grades
DO $$
DECLARE
    student RECORD;
    start_course INTEGER := 1;
    course_count INTEGER := 20;
    courses_per_student INTEGER := 5;
    current_course INTEGER;
    i INTEGER := 0;
    grades TEXT[] := ARRAY['A', 'B', 'C', 'D'];
BEGIN
    FOR student IN SELECT reg_no FROM students ORDER BY reg_no LOOP
        FOR i IN 0..(courses_per_student - 1) LOOP
            current_course := ((start_course + i - 1) % course_count) + 1;

            -- Enroll
            INSERT INTO enrollments (reg_no, course_id)
            VALUES (student.reg_no, current_course);

            -- Grade
            INSERT INTO grades (reg_no, course_id, grade)
            VALUES (student.reg_no, current_course, grades[(random() * 4)::int + 1]);
        END LOOP;

        start_course := start_course + 1;
    END LOOP;
END $$;

-- Users for Students
INSERT INTO users (username, password, role) VALUES
('S100', 'pass123', 'student'), ('S101', 'pass123', 'student'), ('S102', 'pass123', 'student'),
('S103', 'pass123', 'student'), ('S104', 'pass123', 'student'), ('S105', 'pass123', 'student'),
('S106', 'pass123', 'student'), ('S107', 'pass123', 'student'), ('S108', 'pass123', 'student'),
('S109', 'pass123', 'student'), ('S110', 'pass123', 'student'), ('S111', 'pass123', 'student'),
('S112', 'pass123', 'student'), ('S113', 'pass123', 'student'), ('S114', 'pass123', 'student'),
('S115', 'pass123', 'student'), ('S116', 'pass123', 'student'), ('S117', 'pass123', 'student'),
('S118', 'pass123', 'student'), ('S119', 'pass123', 'student');

-- Users for Teachers
INSERT INTO users (username, password, role) VALUES
('T201', 'pass123', 'teacher'), ('T202', 'pass123', 'teacher'), ('T203', 'pass123', 'teacher'),
('T204', 'pass123', 'teacher'), ('T205', 'pass123', 'teacher'), ('T206', 'pass123', 'teacher'),
('T207', 'pass123', 'teacher'), ('T208', 'pass123', 'teacher'), ('T209', 'pass123', 'teacher'),
('T210', 'pass123', 'teacher');
