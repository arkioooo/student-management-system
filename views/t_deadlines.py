import customtkinter as ctk

def show_deadlines(parent):
    # Ensure parent has a transparent background
    parent.configure(fg_color="transparent")

    label = ctk.CTkLabel(
        parent,
        text="• Project reviews due next week\n• Final exam submissions by April 20",
        justify="left",
        font=ctk.CTkFont(size=14),
        fg_color="transparent"  # Transparent label background
    )
    label.pack(padx=10, pady=10)
