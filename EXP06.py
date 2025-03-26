import tkinter as tk
from tkinter import messagebox

def submit():
    """Collects user input and displays it in a messagebox."""
    name = name_entry.get()
    gender = gender_var.get()
    skills = []
    
    if skill1_var.get():
        skills.append("Python")
    if skill2_var.get():
        skills.append("Java")
    if skill3_var.get():
        skills.append("C++")
    
    skill_text = ", ".join(skills) if skills else "None"
    
    info = f"Name: {name}\nGender: {gender}\nSkills: {skill_text}"
    messagebox.showinfo("Information Submitted", info)

def custom_dialog():
    """Displays a custom warning dialog."""
    messagebox.showwarning("Custom Dialog", "This is a custom warning dialog!")

# Main window setup
root = tk.Tk()
root.title("User Information Form")
root.geometry("400x400")

# Title Label
tk.Label(root, text="User Information Form", font=("Arial", 18)).pack(pady=10)

# Name Entry
tk.Label(root, text="Enter your name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Gender Selection (Radio Buttons)
tk.Label(root, text="Select Gender:").pack(pady=5)
gender_var = tk.StringVar(value="None")  # Default value
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Skills Selection (Checkboxes)
tk.Label(root, text="Select Skills:").pack(pady=5)
skill1_var = tk.BooleanVar()
skill2_var = tk.BooleanVar()
skill3_var = tk.BooleanVar()

tk.Checkbutton(root, text="Python", variable=skill1_var).pack()
tk.Checkbutton(root, text="Java", variable=skill2_var).pack()
tk.Checkbutton(root, text="C++", variable=skill3_var).pack()

# Submit Button
tk.Button(root, text="Submit", command=submit).pack(pady=10)

# Custom Dialog Button
tk.Button(root, text="Show Custom Dialog", command=custom_dialog).pack(pady=10)

# Run the application
root.mainloop()