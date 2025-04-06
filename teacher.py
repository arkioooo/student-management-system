import customtkinter as ctk
from tkinter import messagebox

from views.t_home import home_view
from views.t_grades import stu_view
from views.t_courses import course_view
from views.t_announcements import show_announcements
from views.t_deadlines import show_deadlines

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TeacherDashboard(ctk.CTk):
    def __init__(self, teacher_id):
        super().__init__()
        self.teacher_id = teacher_id
        self.title("Teacher Dashboard")
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
        ctk.CTkButton(self.nav_frame, text="Home", command=self.home_view, width=220, height=35).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="View Student Grades", command=self.stu_view, width=220, height=35).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(self.nav_frame, text="View Courses", command=self.course_view, width=220, height=35).pack(side="left", padx=10, pady=10)

        # Right-side theme selector and logout
        self.theme_option_menu = ctk.CTkOptionMenu(self.nav_frame, values=["Dark", "Light", "System"], command=self.change_theme)
        self.theme_option_menu.pack(side="right", padx=10, pady=10)

        ctk.CTkButton(self.nav_frame, text="Logout", command=self.logout, fg_color="red", width=100, height=35).pack(side="right", padx=10, pady=5)

        # HEADER
        self.header = ctk.CTkLabel(self.main_frame, text="Teacher Dashboard", font=("Arial", 28, "bold"), text_color="white")
        self.header.pack(pady=(20, 5))

        self.welcome_label = ctk.CTkLabel(self.main_frame, text=f"Welcome, {teacher_id}!", font=("Arial", 20), text_color="white")
        self.welcome_label.pack(pady=(0, 15))

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

        self.announcements_tab = self.right_tabview.add("Announcements")
        self.deadlines_tab = self.right_tabview.add("Deadlines")

        show_announcements(self.announcements_tab)
        show_deadlines(self.deadlines_tab)

        self.home_view()  # Default view

    def change_theme(self, mode):
        ctk.set_appearance_mode(mode)
        new_bg = "black" if mode == "Dark" else "white"
        self.update_bg_colors(new_bg)

    def update_bg_colors(self, color):
        self.main_frame.configure(fg_color=color)
        self.nav_frame.configure(fg_color=color)
        self.content_frame.configure(fg_color=color)
        self.left_content.configure(fg_color=color)
        self.right_side_frame.configure(fg_color=color)
        self.right_tabview.configure(fg_color=color)

        is_dark = (color == "black")
        text_color = "white" if is_dark else "black"
        self.header.configure(text_color=text_color)
        self.welcome_label.configure(text_color=text_color)

    def clear_content(self):
        for widget in self.left_content.winfo_children():
            widget.destroy()

    def home_view(self):
        self.clear_content()
        home_view(self.left_content, self.teacher_id)

    def stu_view(self):
        self.clear_content()
        stu_view(self.left_content, self.teacher_id)

    def course_view(self):
        self.clear_content()
        course_view(self.left_content, self.teacher_id)

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
    main("T201")
