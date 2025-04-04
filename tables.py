from db import DatabaseManager

def create_tables():
    db = DatabaseManager()

    try:
        # Table creation queries
        create_tables_query = '''
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            phone VARCHAR(15) UNIQUE,
            department VARCHAR(50),
            address TEXT,
            hire_date DATE
        );
  
        CREATE TABLE IF NOT EXISTS courses (
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            code VARCHAR(10) NOT NULL UNIQUE,
            credits INTEGER CHECK (credits > 0),
            teacher_id INTEGER REFERENCES teachers(teacher_id)
        );

        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            phone VARCHAR(15) UNIQUE,
            reg_number VARCHAR(50) NOT NULL UNIQUE,
            year INTEGER CHECK (year > 0),
            course_id INTEGER REFERENCES courses(course_id)
        );

        CREATE TABLE IF NOT EXISTS grades (
            grade_id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES students(student_id),
            course_id INTEGER REFERENCES courses(course_id),
            grade VARCHAR(2) CHECK (grade IN ('A', 'B', 'C', 'D', 'E', 'F')),
            semester INTEGER CHECK (semester > 0),
            year INTEGER CHECK (year > 0)
        );

        CREATE TABLE IF NOT EXISTS enrollment (
            enroll_id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES students(student_id),
            course_id INTEGER REFERENCES courses(course_id),
            enroll_date DATE DEFAULT CURRENT_DATE
        );
        '''
        # Execute the combined query
        db.execute_query(create_tables_query)
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")
    finally:
        db.close()

# Call the function to create tables
create_tables()
