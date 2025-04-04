import customtkinter as ctk
from tkinter import messagebox
from views.t_home import home_view
from views.t_grades import stu_view
from views.t_courses import course_view

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TeacherDashboard(ctk.CTk):
    def __init__(self, email):
        super().__init__()
        self.title("Teacher Dashboard")
        self.geometry("800x500")
        self.configure(fg_color="black")
        self.email = email

        # Main Frame (Black background)
        self.main_frame = ctk.CTkFrame(self, fg_color="black")
        self.main_frame.pack(fill="both", expand=True)

        # Top Navigation Bar (Blended with Main Frame - Black)
        self.nav_frame = ctk.CTkFrame(self.main_frame, fg_color="black", height=50)
        self.nav_frame.pack(fill="x", side="top")

        # Navigation Buttons
        self.home_button = ctk.CTkButton(self.nav_frame, text="Home", command=self.home_view, width=220, height=35)
        self.home_button.pack(side="left", padx=10, pady=10)

        self.grade_button = ctk.CTkButton(self.nav_frame, text="View Student Grades", command=self.stu_view, width=220, height=35)
        self.grade_button.pack(side="left", padx=10, pady=10)

        self.courses_button = ctk.CTkButton(self.nav_frame, text="View Courses", command=self.course_view, width=220, height=35)
        self.courses_button.pack(side="left", padx=10, pady=10)

        # Logout Button on the top right
        self.logout_button = ctk.CTkButton(self.nav_frame, text="Logout", command=self.logout, fg_color="red", width=100, height=35)
        self.logout_button.pack(side="right", padx=10, pady=5)

        # Header inside the main window
        self.header = ctk.CTkLabel(self.main_frame, text="Teacher Dashboard", font=("Arial", 28, "bold"), text_color="white")
        self.header.pack(pady=30)

        # Welcome Message
        self.welcome_label = ctk.CTkLabel(self.main_frame, text=f"Welcome, {email}!", font=("Arial", 20), text_color="white")
        self.welcome_label.pack(pady=10)

        # Dynamic Content Area
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="black")
        self.content_frame.pack(fill="both", expand=True, pady=20)

        # Load the Home view by default
        self.home_view()

    def home_view(self):
        home_view(self.content_frame)

    def stu_view(self):
        stu_view(self.content_frame)

    def course_view(self):
        course_view(self.content_frame)

    def logout(self):
        messagebox.showinfo("Logout", "You have been logged out.")
        self.destroy()
        import landing
        landing.main()

def main():
    email = "teacher@example.com"  # Replace with dynamic email fetching
    app = TeacherDashboard(email)
    app.mainloop()

if __name__ == "__main__":
    main()
