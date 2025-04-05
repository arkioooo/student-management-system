from customtkinter import CTkLabel
from db import DatabaseManager

def stu_view(content_frame, teacher_id):
    for widget in content_frame.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        query = """
            SELECT g.reg_no, s.name, c.course_name, g.grade
            FROM grades g
            JOIN students s ON g.reg_no = s.reg_no
            JOIN courses c ON g.course_id = c.course_id
            WHERE c.teacher_id = %s
            ORDER BY g.reg_no, c.course_name
        """
        results = db.execute_query(query, (teacher_id,), fetch=True)

        CTkLabel(content_frame, text="Student Grades", font=("Arial", 20), text_color="white").pack(pady=10)
        for reg, sname, course, grade in results:
            CTkLabel(content_frame, text=f"{reg} - {sname} | {course} - Grade: {grade}", font=("Arial", 14), text_color="white").pack()

    except Exception as e:
        CTkLabel(content_frame, text=f"Error: {e}", text_color="red").pack()
    finally:
        db.close()
