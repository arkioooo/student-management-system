import customtkinter as ctk
from tkinter import messagebox

# Import the modular views
from views.s_profile import show_profile
from views.s_courses import show_courses
from views.s_grades import show_grades

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class StudentDashboard(ctk.CTk):
    def __init__(self, regno):
        super().__init__()
        self.title("Student Dashboard")
        self.geometry("800x500")
        self.configure(fg_color="black")
        self.regno = regno

        self.main_frame = ctk.CTkFrame(self, fg_color="black")
        self.main_frame.pack(fill="both", expand=True)

        self.nav_frame = ctk.CTkFrame(self.main_frame, fg_color="black", height=50)
        self.nav_frame.pack(fill="x", side="top")

        self.profile_button = ctk.CTkButton(self.nav_frame, text="Profile", command=self.profile_view, width=220, height=35)
        self.profile_button.pack(side="left", padx=10, pady=10)

        self.courses_button = ctk.CTkButton(self.nav_frame, text="Courses", command=self.courses_view, width=220, height=35)
        self.courses_button.pack(side="left", padx=10, pady=10)

        self.grades_button = ctk.CTkButton(self.nav_frame, text="Grades", command=self.grades_view, width=220, height=35)
        self.grades_button.pack(side="left", padx=10, pady=10)

        self.logout_button = ctk.CTkButton(self.nav_frame, text="Logout", command=self.logout, fg_color="red", width=100, height=35)
        self.logout_button.pack(side="right", padx=10, pady=5)

        self.header = ctk.CTkLabel(self.main_frame, text="Student Dashboard", font=("Arial", 28, "bold"), text_color="white")
        self.header.pack(pady=30)

        self.welcome_label = ctk.CTkLabel(self.main_frame, text=f"Welcome, {regno}!", font=("Arial", 20), text_color="white")
        self.welcome_label.pack(pady=10)

        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="black")
        self.content_frame.pack(fill="both", expand=True, pady=20)

        self.profile_view()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def profile_view(self):
        show_profile(self.content_frame, self.regno)

    def courses_view(self):
        show_courses(self.content_frame)

    def grades_view(self):
        show_grades(self.content_frame)

    def logout(self):
        messagebox.showinfo("Logout", "You have been logged out.")
        self.destroy()
        import landing
        landing.main()

def main():
    regno = "studentregno"
    app = StudentDashboard(regno)
    app.mainloop()

if __name__ == "__main__":
    main()
