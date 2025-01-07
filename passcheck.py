import customtkinter as ctk
import tkinter as tk
import tkinter.messagebox as tkmb
import re


# Function to check password strength
def check_password_strength(event=None):  # Allows binding to the Enter key
    password = password_entry.get()
    strength_label.configure(text="")

    if len(password) < 6:
        strength_label.configure(text="Weak: Password is too short", text_color="red")
    else:
        score = 0
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[0-9]', password):
            score += 1
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1

        # Determine strength
        if score == 1:
            strength_label.configure(text="Weak: Add more variety", text_color="red")
        elif score == 2:
            strength_label.configure(text="Moderate: Add complexity", text_color="orange")
        elif score == 3:
            strength_label.configure(text="Strong: Almost there", text_color="green")
        else:
            strength_label.configure(text="Very Strong: Great password!", text_color="blue")


# Function to toggle password visibility
def toggle_password_visibility():
    if show_password_switch.get():
        password_entry.configure(show="")  # Show the password
    else:
        password_entry.configure(show="*")  # Hide the password


# Function to display the About message
def show_about():
    tkmb.showinfo("About", "Password Strength Checker\nVersion 1.0\nDeveloped by Tansique Dasari.")


# Function to exit the app
def exit_app():
    app.destroy()


# Initialize the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Password Strength Checker")
app.geometry("400x350")

# Menu Bar
menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

menu_bar.add_command(label="About", command=show_about)
menu_bar.add_command(label="Exit", command=exit_app)

# UI Components
title_label = ctk.CTkLabel(app, text="Password Strength Checker", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

password_label = ctk.CTkLabel(app, text="Enter Password:")
password_label.pack()

password_entry = ctk.CTkEntry(app, width=250, show="*")
password_entry.pack(pady=5)

# Bind Enter key to the password strength check
password_entry.bind("<Return>", check_password_strength)

show_password_switch = ctk.CTkSwitch(app, text="Show Password", command=toggle_password_visibility)
show_password_switch.pack(pady=5)

check_button = ctk.CTkButton(app, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

strength_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
strength_label.pack(pady=5)

# Run the app
app.mainloop()
