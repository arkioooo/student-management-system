import customtkinter as ctk

def show_profile(content_frame, regno):
    for widget in content_frame.winfo_children():
        widget.destroy()
    label = ctk.CTkLabel(content_frame, text=f"Profile of {regno}", font=("Arial", 20), text_color="white")
    label.pack(pady=20)
