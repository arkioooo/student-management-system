import customtkinter as ctk

def show_holidays(parent):
    label = ctk.CTkLabel(parent, text="Upcoming Holidays:\n- Good Friday - 18/4\n- Easter - 20/4\n- Bakrid - 7/6", justify="left", font=ctk.CTkFont(size=14))
    label.pack(padx=20, pady=20)
