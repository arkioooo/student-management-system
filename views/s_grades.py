from customtkinter import CTkLabel
from db import DatabaseManager

def show_grades(parent, regno):
    for widget in parent.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        query = """
        SELECT c.course_name, g.grade
        FROM grades g
        JOIN courses c ON g.course_id = c.course_id
        WHERE g.reg_no = %s
        """
        results = db.execute_query(query, (regno,), fetch=True)

        if results:
            for course, grade in results:
                CTkLabel(parent, text=f"{course}: {grade}", font=("Arial", 16)).pack(anchor="w", padx=20, pady=5)
        else:
            CTkLabel(parent, text="No grades available.", font=("Arial", 16)).pack(pady=20)

    except Exception as e:
        CTkLabel(parent, text=f"Error: {e}", font=("Arial", 16)).pack(pady=20)
    finally:
        db.close()
