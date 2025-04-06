from customtkinter import CTkLabel, CTkFrame, CTkScrollableFrame, CTkOptionMenu, StringVar
from db import DatabaseManager

def stu_view(content_frame, teacher_id):
    for widget in content_frame.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        # Fetch distinct courses taught by the teacher
        course_query = """
            SELECT DISTINCT course_name
            FROM courses
            WHERE teacher_id = %s
            ORDER BY course_name
        """
        courses = db.execute_query(course_query, (teacher_id,), fetch=True)
        course_names = [row[0] for row in courses]

        if not course_names:
            CTkLabel(content_frame, text="No courses assigned to you.", font=("Arial", 16), text_color="gray").pack(pady=20)
            return

        # Title
        CTkLabel(content_frame, text="Student Grades", font=("Arial", 24, "bold")).pack(pady=(10, 5))

        # Filter label and dropdown
        filter_frame = CTkFrame(content_frame, fg_color="transparent")
        filter_frame.pack(pady=5)

        CTkLabel(filter_frame, text="Filter by Course:", font=("Arial", 16)).pack(side="left", padx=(10, 5))

        selected_course = StringVar(value=course_names[0])
        dropdown = CTkOptionMenu(filter_frame, variable=selected_course, values=course_names,
                                 command=lambda value: load_grades(value))
        dropdown.pack(side="left", padx=5)

        # Scrollable container for results
        scroll_frame = CTkScrollableFrame(content_frame, fg_color="transparent")
        scroll_frame.pack(fill="both", expand=True, padx=40, pady=10)

        # Function to load grades based on selected course
        def load_grades(course_name):
            for widget in scroll_frame.winfo_children():
                widget.destroy()

            grade_query = """
                SELECT g.reg_no, s.name, c.course_name, g.grade
                FROM grades g
                JOIN students s ON g.reg_no = s.reg_no
                JOIN courses c ON g.course_id = c.course_id
                WHERE c.teacher_id = %s AND c.course_name = %s
                ORDER BY g.reg_no
            """
            results = db.execute_query(grade_query, (teacher_id, course_name), fetch=True)

            if results:
                for reg, sname, course, grade in results:
                    row_frame = CTkFrame(scroll_frame, fg_color="#1a1a1a", corner_radius=10)
                    row_frame.pack(fill="x", padx=10, pady=10)

                    CTkLabel(row_frame, text=f"{sname} ({reg})", font=("Arial", 16, "bold"), text_color="white",
                             anchor="w", justify="left").pack(anchor="w", padx=15, pady=(10, 2))
                    CTkLabel(row_frame, text=f"{course}", font=("Arial", 15), text_color="white",
                             anchor="w", justify="left").pack(anchor="w", padx=15, pady=2)
                    CTkLabel(row_frame, text=f"Grade: {grade}", font=("Arial", 15), text_color="white",
                             anchor="w", justify="left").pack(anchor="w", padx=15, pady=(2, 10))
            else:
                CTkLabel(scroll_frame, text="No grades found for this course.",
                         font=("Arial", 16), text_color="gray").pack(pady=20)

        # Load grades for default selected course
        load_grades(selected_course.get())

    except Exception as e:
        CTkLabel(content_frame, text=f"Error: {e}", font=("Arial", 16), text_color="red").pack(pady=30)

    finally:
        db.close()
