import customtkinter as ctk

def show_events(parent):
    label = ctk.CTkLabel(parent, text="Upcoming Events:\n- Tech Solstice - 6/4\n- IBM Tech Talk - 7/4\n- Sports Meet - 13/4", justify="left", font=ctk.CTkFont(size=14))
    label.pack(padx=20, pady=20)
