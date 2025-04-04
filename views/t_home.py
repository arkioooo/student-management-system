from customtkinter import CTkLabel, CTkFrame

def home_view(content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    label = CTkLabel(content_frame, text="Welcome to the Home Page!", font=("Arial", 18), text_color="white")
    label.pack(pady=20)
