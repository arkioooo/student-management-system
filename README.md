# Student Management System

The Student Management System is a Python-based application designed to manage student and teacher information within an educational institution. It provides functionalities for user authentication, viewing student grades, and managing course information.

## Features

- **User Authentication**: Secure login system for students and teachers.
- **Student Dashboard**: View personal information and enrolled courses.
- **Teacher Dashboard**: Access to courses taught and student grades.
- **Database Integration**: Utilizes PostgreSQL for data storage and retrieval.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- PostgreSQL database
- Required Python packages listed in `requirements.txt`

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/arkioooo/student-management-system.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd student-management-system
   ```

3. **Set Up a Virtual Environment** (Optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the Database**:

   - Create a PostgreSQL database named `university`.
   - Update the `.env` file with your database credentials.

6. **Seed the Database**:

   Run the `seed_runner.py` script to populate the database with initial data:

   ```bash
   python seed_runner.py
   ```

## Usage

To start the application, run the `landing.py` script:

```bash
python landing.py
```

## Project Structure

- `landing.py`: The main entry point of the application.
- `db.py`: Handles database connections and queries.
- `student.py`: Contains the student dashboard and related functionalities.
- `teacher.py`: Contains the teacher dashboard and related functionalities.
- `views/`: Directory containing GUI components.
- `seed_data.sql`: SQL script with initial data for seeding the database.
- `seed_runner.py`: Script to execute the `seed_data.sql` file.

