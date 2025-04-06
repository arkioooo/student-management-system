import customtkinter as ctk
from tkinter import messagebox

from views.s_profile import show_profile
from views.s_courses import show_courses
from views.s_grades import show_grades
from views.s_events import show_events
from views.s_holidays import show_holidays

ctk.set_appearance_mode("dark")  # Default mode
ctk.set_default_color_theme("blue")


class StudentDashboard(ctk.CTk):
    def __init__(self, regno):
        super().__init__()
        self.regno = regno
        self.title("Student Dashboard")
        self.geometry("1250x600")
        self.resizable(False, False)


        self.bg_color = "black" if ctk.get_appearance_mode() == "Dark" else "white"

        # MAIN FRAME
        self.main_frame = ctk.CTkFrame(self, fg_color=self.bg_color)
        self.main_frame.pack(fill="both", expand=True)

        # NAVIGATION BAR
        self.nav_frame = ctk.CTkFrame(self.main_frame, height=50, fg_color=self.bg_color)
        self.nav_frame.pack(fill="x", side="top")

        # Left-side buttons
        ctk.CTkButton(self.nav_frame, text="Profile", command=self.profile_view, width=220, height=35).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="Courses", command=self.courses_view, width=220, height=35).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="Grades", command=self.grades_view, width=220, height=35).pack(side="left", padx=10, pady=10)

        # Right-side theme selector and logout
        self.theme_option_menu = ctk.CTkOptionMenu(self.nav_frame, values=["Dark", "Light", "System"], command=self.change_theme)
        self.theme_option_menu.pack(side="right", padx=10, pady=10)

        ctk.CTkButton(self.nav_frame, text="Logout", command=self.logout, fg_color="red", width=100, height=35).pack(side="right", padx=10, pady=5)

        # HEADER
        self.header = ctk.CTkLabel(self.main_frame, text="Student Dashboard", font=("Arial", 28, "bold"), text_color="white")
        self.header.pack(pady=20)

        self.welcome_label = ctk.CTkLabel(self.main_frame, text=f"Welcome, {regno}!", font=("Arial", 20), text_color="white")
        self.welcome_label.pack(pady=5)

        # CONTENT FRAME
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color=self.bg_color)
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # LEFT CONTENT AREA
        self.left_content = ctk.CTkFrame(self.content_frame, fg_color=self.bg_color)
        self.left_content.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # RIGHT CONTENT AREA (TabView)
        self.right_side_frame = ctk.CTkFrame(self.content_frame, fg_color=self.bg_color)
        self.right_side_frame.pack(side="right", fill="y")

        self.right_tabview = ctk.CTkTabview(self.right_side_frame, width=400, fg_color=self.bg_color)
        self.right_tabview.pack(side="top", fill="y", pady=(0, 10))

        self.events_tab = self.right_tabview.add("Events")
        self.holidays_tab = self.right_tabview.add("Holidays")

        show_events(self.events_tab)
        show_holidays(self.holidays_tab)

        self.profile_view()  # Load default view

    def change_theme(self, mode):
        ctk.set_appearance_mode(mode)

        # Update background color dynamically
        new_bg = "black" if mode == "Dark" else "white"
        self.update_bg_colors(new_bg)

    def update_bg_colors(self, color):
        # Update all relevant container background colors
        self.main_frame.configure(fg_color=color)
        self.nav_frame.configure(fg_color=color)
        self.content_frame.configure(fg_color=color)
        self.left_content.configure(fg_color=color)
        self.right_side_frame.configure(fg_color=color)
        self.right_tabview.configure(fg_color=color)

        # Optionally update label colors for readability
        is_dark = (color == "black")
        text_color = "white" if is_dark else "black"
        self.header.configure(text_color=text_color)
        self.welcome_label.configure(text_color=text_color)

    def clear_content(self):
        for widget in self.left_content.winfo_children():
            widget.destroy()

    def profile_view(self):
        self.clear_content()
        show_profile(self.left_content, self.regno)

    def courses_view(self):
        self.clear_content()
        show_courses(self.left_content, self.regno)

    def grades_view(self):
        self.clear_content()
        show_grades(self.left_content, self.regno)

    def logout(self):
        messagebox.showinfo("Logout", "You have been logged out.")
        self.destroy()
        import landing
        landing.main()


def main(regno):
    print("📌 Student regno passed to dashboard:", regno)
    app = StudentDashboard(regno)
    app.mainloop()


if __name__ == "__main__":
    main("S101")  # For testing
