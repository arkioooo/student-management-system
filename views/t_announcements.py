import customtkinter as ctk

def show_announcements(parent):
    # Set parent frame background to transparent
    parent.configure(fg_color="transparent")

    label = ctk.CTkLabel(
        parent,
        text="• Staff meeting on Monday\n• Assignment deadline on Friday",
        justify="left",
        font=ctk.CTkFont(size=14),
        fg_color="transparent"  # Transparent label background
    )
    label.pack(padx=10, pady=10)
