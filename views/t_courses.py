from customtkinter import CTkLabel

def course_view(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    label = CTkLabel(content_frame, text="Courses Page", font=("Arial", 18), text_color="white")
    label.pack(pady=20)
