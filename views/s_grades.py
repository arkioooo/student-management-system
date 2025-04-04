import customtkinter as ctk

def show_grades(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()
    label = ctk.CTkLabel(content_frame, text="Grades", font=("Arial", 20), text_color="white")
    label.pack(pady=20)
