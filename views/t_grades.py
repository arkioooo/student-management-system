from customtkinter import CTkLabel

def stu_view(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    label = CTkLabel(content_frame, text="Student Grades Page", font=("Arial", 18), text_color="white")
    label.pack(pady=20)
    