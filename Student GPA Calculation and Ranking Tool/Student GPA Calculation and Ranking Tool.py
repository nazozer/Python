import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

# Global variable
df = None

# Load the Excel file
def load_excel():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            df['GPA'] = df.apply(calculate_gpa, axis=1)
            df.sort_values(by='GPA', ascending=False, inplace=True)
            df['Rank'] = range(1, len(df) + 1)
            messagebox.showinfo("Success", "Excel file loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {str(e)}")

# Function to calculate GPA
def calculate_gpa(row):
    physics = row['Physics'] * 0.25
    calculus = row['Calculus'] * 0.25
    advanced_programming = row['Advanced Programming'] * 0.30
    chemistry = row['Chemistry'] * 0.20
    gpa = physics + calculus + advanced_programming + chemistry
    return round(gpa, 2)

# Display student information
def display_student_info():
    global df
    if df is None:
        messagebox.showerror("Error", "Please load an Excel file first.")
        return

    student_id = entry_id.get()
    if not student_id.isdigit():
        messagebox.showerror("Error", "Please enter a valid student ID.")
        return

    student = df[df['ID'] == int(student_id)]
    if not student.empty:
        name = student.iloc[0]['Name']
        surname = student.iloc[0]['Surname']
        gpa = student.iloc[0]['GPA']
        rank = student.iloc[0]['Rank']
        label_name.config(text=f"{name} {surname}")
        label_gpa.config(text=f"{gpa}")
        label_rank.config(text=f"{rank}")
    else:
        messagebox.showerror("Error", "Student not found.")

# Clear input fields
def clear_info():
    entry_id.delete(0, tk.END)
    label_name.config(text="")
    label_gpa.config(text="")
    label_rank.config(text="")

# Export student data to file
def export_to_file():
    global df
    if df is None:
        messagebox.showerror("Error", "Please load an Excel file first.")
        return

    student_id = entry_id.get()
    file_type = combobox_filetype.get()

    student = df[df['ID'] == int(student_id)]
    if not student.empty:
        name = student.iloc[0]['Name']
        surname = student.iloc[0]['Surname']
        gpa = student.iloc[0]['GPA']
        rank = student.iloc[0]['Rank']
        file_name = f"{student_id}_{name}_{surname}.{file_type}"

        try:
            if file_type == 'txt':
                with open(file_name, 'w') as file:
                    file.write(f"Name: {name}\nSurname: {surname}\nGPA: {gpa}\nRank: {rank}")
            elif file_type == 'xls':
                student[['Name', 'Surname', 'ID', 'GPA', 'Rank']].to_excel(file_name, index=False)

            messagebox.showinfo("Success", f"File saved: {file_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    else:
        messagebox.showerror("Error", "Student not found.")

# GUI design
root = tk.Tk()
root.title("Haliç University")
root.geometry("380x270")

# Top Label: Student GPA and Ranking
top_label = tk.Label(root, text="Student GPA and Ranking")
top_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


# "Browse" button and file selection
label_browse = tk.Label(root, text="Open file")
label_browse.grid(row=1, column=0, padx=10, pady=5, sticky='we')

button_browse = tk.Button(root, text="Browse", command=load_excel)
button_browse.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

# ID entry field
label_id = tk.Label(root, text="ID:")
label_id.grid(row=2, column=0, padx=10, pady=5, sticky='w')

entry_id = tk.Entry(root)
entry_id.grid(row=2, column=1, padx=10, pady=5)

# Student information (Name Surname, GPA, Rank)
label_name_title = tk.Label(root, text="Name Surname:")
label_name_title.grid(row=3, column=0, padx=10, pady=5, sticky='w')
label_name = tk.Label(root, text="")
label_name.grid(row=3, column=1, padx=10, pady=5)

label_gpa_title = tk.Label(root, text="GPA:")
label_gpa_title.grid(row=4, column=0, padx=10, pady=5, sticky='w')
label_gpa = tk.Label(root, text="")
label_gpa.grid(row=4, column=1, padx=10, pady=5)

label_rank_title = tk.Label(root, text="Rank:")
label_rank_title.grid(row=5, column=0, padx=10, pady=5,sticky='w')
label_rank = tk.Label(root, text="")
label_rank.grid(row=5, column=1, padx=10, pady=5)


# File type selection
label_filetype = tk.Label(root, text="Please select file type:")
label_filetype.grid(row=6, column=0, padx=10, pady=5, sticky='w')

combobox_filetype = ttk.Combobox(root, values=["txt", "xlsx"], state="readonly")
combobox_filetype.set("txt")
combobox_filetype.grid(row=6, column=1, padx=10, pady=5, sticky='ew')


# "Display", "Export", and "Clear" buttons
button_display = tk.Button(root, text="Display", command=display_student_info, width=10)
button_display.grid(row=7, column=0, padx=0, pady=0, sticky="nsew")

button_export = tk.Button(root, text="Export", command=export_to_file, width=10)
button_export.grid(row=7, column=1, padx=0, pady=0, sticky="nsew")

button_clear = tk.Button(root, text="Clear", command=clear_info, width=10)
button_clear.grid(row=7, column=2, padx=0, pady=0, sticky="nsew")

root.mainloop()
