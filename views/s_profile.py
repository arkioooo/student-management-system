from customtkinter import CTkLabel
from db import DatabaseManager

def show_profile(parent, regno):
    for widget in parent.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        query = "SELECT name, reg_no, admission_year, department FROM students WHERE reg_no = %s"
        result = db.execute_query(query, (regno,), fetch=True)

        if result:
            name, reg_no, year, dept = result[0]
            data = [
                f"Name: {name}",
                f"Registration No: {reg_no}",
                f"Admission Year: {year}",
                f"Department: {dept}"
            ]
            for line in data:
                CTkLabel(parent, text=line, font=("Arial", 16)).pack(anchor="w", padx=20, pady=5)
        else:
            CTkLabel(parent, text="Student not found.", font=("Arial", 16)).pack(pady=20)

    except Exception as e:
        CTkLabel(parent, text=f"Error: {e}", font=("Arial", 16)).pack(pady=20)
    finally:
        db.close()
