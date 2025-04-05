from customtkinter import CTkLabel
from db import DatabaseManager

def home_view(content_frame, teacher_id):
    for widget in content_frame.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        query = "SELECT name FROM teachers WHERE teacher_id = %s"
        result = db.execute_query(query, (teacher_id,), fetch=True)

        if result:
            name = result[0][0]
            info_text = f"Welcome, {name}!\nTeacher ID: {teacher_id}"
        else:
            info_text = f"Teacher ID {teacher_id} not found."

        CTkLabel(content_frame, text=info_text, font=("Arial", 20), text_color="white").pack(pady=30)

    except Exception as e:
        CTkLabel(content_frame, text=f"Error: {e}", text_color="red").pack()
    finally:
        db.close()
