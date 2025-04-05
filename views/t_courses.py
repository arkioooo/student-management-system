from customtkinter import CTkLabel
from db import DatabaseManager

def course_view(content_frame, teacher_id):
    for widget in content_frame.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        query = """
            SELECT course_id, course_name FROM courses
            WHERE teacher_id = %s
        """
        courses = db.execute_query(query, (teacher_id,), fetch=True)

        CTkLabel(content_frame, text="Your Courses", font=("Arial", 20), text_color="white").pack(pady=10)
        for cid, cname in courses:
            CTkLabel(content_frame, text=f"{cid} - {cname}", font=("Arial", 16), text_color="white").pack()

    except Exception as e:
        CTkLabel(content_frame, text=f"Error: {e}", text_color="red").pack()
    finally:
        db.close()
