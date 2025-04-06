from customtkinter import CTkLabel, CTkFrame
from db import DatabaseManager

def show_courses(parent, regno):
    # Clear previous content
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
            # Title above the card
            CTkLabel(parent, text="Enrolled Courses", font=("Arial", 22, "bold")).pack(pady=(30, 10))

            # Card-style frame with transparent background
            card = CTkFrame(parent, corner_radius=15, border_width=2, fg_color="transparent")
            card.pack(pady=10, padx=40, fill="both", expand=False)

            # Column headers
            CTkLabel(card, text="Course Name", font=("Arial", 14, "bold")).grid(row=0, column=0, sticky="w", padx=20, pady=(10, 5))
            CTkLabel(card, text="Instructor", font=("Arial", 14, "bold")).grid(row=0, column=1, sticky="w", padx=20, pady=(10, 5))

            # Course entries
            for i, (course, teacher) in enumerate(results, start=1):
                CTkLabel(card, text=course, font=("Arial", 14)).grid(row=i, column=0, sticky="w", padx=20, pady=5)
                CTkLabel(card, text=teacher, font=("Arial", 14)).grid(row=i, column=1, sticky="w", padx=20, pady=5)

        else:
            CTkLabel(parent, text="No enrolled courses found.", font=("Arial", 16)).pack(pady=20)

    except Exception as e:
        CTkLabel(parent, text=f"Error: {e}", font=("Arial", 16)).pack(pady=20)
    finally:
        db.close()
