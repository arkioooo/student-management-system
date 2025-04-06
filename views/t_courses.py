from customtkinter import CTkLabel, CTkFrame, CTkScrollableFrame
from db import DatabaseManager
import random

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

        CTkLabel(content_frame, text="Your Courses", font=("Arial", 24, "bold")).pack(pady=(10, 20))

        if courses:
            scroll_frame = CTkScrollableFrame(content_frame, fg_color="transparent")
            scroll_frame.pack(fill="both", expand=True, padx=40, pady=10)

            for cid, cname in courses:
                # Dummy data for classes completed
                completed_classes = random.randint(30, 46)
                total_classes = 46

                course_card = CTkFrame(scroll_frame, fg_color="#1a1a1a", corner_radius=10)
                course_card.pack(fill="x", padx=10, pady=10)

                CTkLabel(course_card, text=f"{cname}", font=("Arial", 18, "bold"),
                         text_color="white", anchor="w").pack(anchor="w", padx=15, pady=(10, 2))

                CTkLabel(course_card, text=f"Course ID: {cid}", font=("Arial", 15),
                         text_color="white", anchor="w").pack(anchor="w", padx=15, pady=2)

                CTkLabel(course_card, text=f"Classes Completed: {completed_classes}/{total_classes}",
                         font=("Arial", 15), text_color="#00ffcc", anchor="w").pack(anchor="w", padx=15, pady=(2, 10))

        else:
            CTkLabel(content_frame, text="You have not been assigned any courses.",
                     font=("Arial", 16), text_color="gray").pack(pady=20)

    except Exception as e:
        CTkLabel(content_frame, text=f"Error: {e}", font=("Arial", 16), text_color="red").pack(pady=30)

    finally:
        db.close()
