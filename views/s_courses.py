from customtkinter import CTkLabel
from db import DatabaseManager

def show_courses(parent, regno):
    for widget in parent.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        query = """
        SELECT c.course_name, t.name AS teacher
        FROM enrollments e
        JOIN courses c ON e.course_id = c.course_id
        JOIN teachers t ON c.teacher_id = t.teacher_id
        WHERE e.reg_no = %s
        """
        results = db.execute_query(query, (regno,), fetch=True)

        if results:
            for course, teacher in results:
                CTkLabel(parent, text=f"{course} - {teacher}", font=("Arial", 16)).pack(anchor="w", padx=20, pady=5)
        else:
            CTkLabel(parent, text="No enrolled courses found.", font=("Arial", 16)).pack(pady=20)

    except Exception as e:
        CTkLabel(parent, text=f"Error: {e}", font=("Arial", 16)).pack(pady=20)
    finally:
        db.close()
