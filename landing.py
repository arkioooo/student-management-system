import psycopg2
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Student Management System")
        self.geometry("1000x600")
        self.configure(fg_color="black")

        self.main_frame = ctk.CTkFrame(self, fg_color="black")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.logo_image = ctk.CTkImage(
            light_image=Image.open("logo.png"),
            size=(350, 130)
        )

        self.image_label = ctk.CTkLabel(self.main_frame, image=self.logo_image, text="")
        self.image_label.pack(pady=10)

        self.header = ctk.CTkLabel(self.main_frame, text="Login", font=("Arial", 28, "bold"))
        self.header.pack(pady=20)

        self.role_var = ctk.StringVar(value="Student")
        self.role_label = ctk.CTkLabel(self.main_frame, text="Select Role:", font=("Arial", 14))
        self.role_label.pack(pady=5)
        self.role_combo = ctk.CTkComboBox(
            self.main_frame, values=["Student", "Teacher"], variable=self.role_var, width=250
        )
        self.role_combo.pack(pady=5)

        self.username_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Username", width=250)
        self.username_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Password", show="*", width=250)
        self.password_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self.main_frame, text="Login", command=self.login, width=200)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        role = self.role_var.get().lower()

        if not username or not password:
            messagebox.showerror("Input Error", "Please enter both username and password.")
            return

        try:
            conn = psycopg2.connect(
                dbname="university",
                user="postgres",
                password="db_pass", # Replace with your DB password
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()

            query = "SELECT * FROM users WHERE username = %s AND password = %s AND role = %s"
            cursor.execute(query, (username, password, role))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success", f"Welcome, {role.capitalize()}!")
                self.destroy()

                if role == "student":
                    import student
                    student.main(username)  # Pass student reg_no
                else:
                    import teacher
                    teacher.main(username)  # Pass teacher_id
            else:
                messagebox.showerror("Login Failed", "Invalid username, password, or role.")

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

def main():
    app = LoginPage()
    app.mainloop()

if __name__ == "__main__":
    main()
