from customtkinter import CTkLabel, CTkFrame
from db import DatabaseManager

def show_profile(parent, regno):
    # Clear previous content
    for widget in parent.winfo_children():
        widget.destroy()

    db = DatabaseManager()
    try:
        query = "SELECT name, reg_no, admission_year, department FROM students WHERE reg_no = %s"
        result = db.execute_query(query, (regno,), fetch=True)

        if result:
            name, reg_no, year, dept = result[0]

            # Section title
            CTkLabel(parent, text="Student Profile", font=("Arial", 24, "bold")).pack(pady=(20, 10))

            # Card-style frame with transparent background
            card = CTkFrame(parent, corner_radius=15, border_width=1, fg_color="transparent")
            card.pack(pady=10, padx=40, fill="x", expand=False)

            profile_data = {
                "Name": name,
                "Registration No": reg_no,
                "Admission Year": year,
                "Department": dept
            }

            for i, (key, value) in enumerate(profile_data.items()):
                CTkLabel(card, text=f"{key}:", font=("Arial", 16, "bold")).grid(row=i, column=0, sticky="e", padx=(30, 10), pady=10)
                CTkLabel(card, text=str(value), font=("Arial", 16)).grid(row=i, column=1, sticky="w", padx=(10, 30), pady=10)

        else:
            CTkLabel(parent, text="Student not found.", font=("Arial", 16)).pack(pady=20)

    except Exception as e:
        CTkLabel(parent, text=f"Error: {e}", font=("Arial", 16)).pack(pady=20)

    finally:
        db.close()
