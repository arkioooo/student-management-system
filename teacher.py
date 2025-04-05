import customtkinter as ctk
from tkinter import messagebox
from views.t_home import home_view
from views.t_grades import stu_view
from views.t_courses import course_view

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TeacherDashboard(ctk.CTk):
    def __init__(self, teacher_id):
        super().__init__()
        self.teacher_id = teacher_id  # Store teacher_id for all views
        self.title("Teacher Dashboard")
        self.geometry("800x500")
        self.configure(fg_color="black")

        self.main_frame = ctk.CTkFrame(self, fg_color="black")
        self.main_frame.pack(fill="both", expand=True)

        self.nav_frame = ctk.CTkFrame(self.main_frame, fg_color="black", height=50)
        self.nav_frame.pack(fill="x", side="top")

        ctk.CTkButton(self.nav_frame, text="Home", command=self.home_view, width=220, height=35).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="View Student Grades", command=self.stu_view, width=220, height=35).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="View Courses", command=self.course_view, width=220, height=35).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="Logout", command=self.logout, fg_color="red", width=100, height=35).pack(side="right", padx=10, pady=5)

        self.header = ctk.CTkLabel(self.main_frame, text="Teacher Dashboard", font=("Arial", 28, "bold"), text_color="white")
        self.header.pack(pady=30)

        self.welcome_label = ctk.CTkLabel(self.main_frame, text=f"Welcome, {teacher_id}!", font=("Arial", 20), text_color="white")
        self.welcome_label.pack(pady=10)

        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="black")
        self.content_frame.pack(fill="both", expand=True, pady=20)

        self.home_view()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def home_view(self):
        self.clear_content()
        home_view(self.content_frame, self.teacher_id)

    def stu_view(self):
        self.clear_content()
        stu_view(self.content_frame, self.teacher_id)

    def course_view(self):
        self.clear_content()
        course_view(self.content_frame, self.teacher_id)

    def logout(self):
        messagebox.showinfo("Logout", "You have been logged out.")
        self.destroy()
        import landing
        landing.main()

def main(teacher_id):
    print("📌 Teacher ID passed to dashboard:", teacher_id)
    app = TeacherDashboard(teacher_id)
    app.mainloop()

if __name__ == "__main__":
    main("T201")  # For testing
