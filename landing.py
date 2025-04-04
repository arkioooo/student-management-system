import psycopg2
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Set the appearance mode to dark
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Student Management System")
        self.geometry("1000x1000")
        self.configure(fg_color="black")

        # Create a frame to hold all elements, making it easier to center
        self.main_frame = ctk.CTkFrame(self, fg_color="black")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Load the image and create a CTkImage object
        self.logo_image = ctk.CTkImage(
            light_image=Image.open(r"C:\Users\mssha\Desktop\DAA\FINAL_PROJ\student-management-system\logo.png"),  # Replace with your image file path
            size=(510, 300)  # Adjust size as needed
        )

        # Image Label
        self.image_label = ctk.CTkLabel(self.main_frame, image=self.logo_image, text="")
        self.image_label.pack(pady=10)

        # Header
        self.header = ctk.CTkLabel(self.main_frame, text="Login", font=("Arial", 28, "bold"))
        self.header.pack(pady=20)

        # Role selection (Student/Teacher)
        self.role_var = ctk.StringVar(value="Student")
        self.role_label = ctk.CTkLabel(self.main_frame, text="Select Role:", font=("Arial", 14))
        self.role_label.pack(pady=5)
        self.role_combo = ctk.CTkComboBox(
            self.main_frame, values=["Student", "Teacher"], variable=self.role_var, width=250
        )
        self.role_combo.pack(pady=5)

        # Username and Password
        self.username_entry = ctk.CTkEntry(self.main_frame, placeholder_text="College ID", width=250)
        self.username_entry.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Name", width=250)
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = ctk.CTkButton(self.main_frame, text="Login", command=self.login, width=200)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        try:
            conn = psycopg2.connect(
                dbname="student_management_system",
                user="postgres",
                password="seendo1303",
                host="localhost",
                port="5432"
            )
            cursor = conn.cursor()

            # Check login based on role
            if role == "Student":
                query = "SELECT * FROM Students WHERE student_id = %s AND name = %s"
            else:
                query = "SELECT * FROM Teachers WHERE teacher_id = %s AND name = %s"

            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Success", f"Welcome, {role}!")
                self.destroy()

                # Redirect based on role
                if role == "Student":
                    import student
                    student.main()
                else:
                    import teacher
                    teacher.main()

            else:
                messagebox.showerror("Error", "Invalid username or password")

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

def main():
    app = LoginPage()
    app.mainloop()

if __name__ == "__main__":
    main()
