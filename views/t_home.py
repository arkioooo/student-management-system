from customtkinter import CTkLabel, CTkFrame
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

            # Transparent card-style container
            card = CTkFrame(content_frame, fg_color="transparent", corner_radius=10)
            card.pack(pady=40, padx=40, fill="both", expand=True)

            CTkLabel(card, text="Teacher Profile", font=("Arial", 24, "bold")).pack(pady=(20, 10))

            CTkLabel(card, text=f"Name: {name}", font=("Arial", 18), anchor="w", justify="left").pack(pady=5, anchor="w", padx=20)
            CTkLabel(card, text=f"Teacher ID: {teacher_id}", font=("Arial", 18), anchor="w", justify="left").pack(pady=5, anchor="w", padx=20)

        else:
            CTkLabel(content_frame, text=f"Teacher ID {teacher_id} not found.", font=("Arial", 18), text_color="red").pack(pady=30)

    except Exception as e:
        CTkLabel(content_frame, text=f"Error: {e}", font=("Arial", 16), text_color="red").pack(pady=30)

    finally:
        db.close()
