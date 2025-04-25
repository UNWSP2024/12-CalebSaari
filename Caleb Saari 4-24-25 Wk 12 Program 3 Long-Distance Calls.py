# The application will feature radio buttons for selecting the rate
# category (Daytime, Evening, Off-Peak) and an entry widget for inputting the duration of the
# call in minutes. Upon submission, an information dialog box will display the calculated charge
# for the call.

import tkinter as tk
from tkinter import messagebox


def calculate_charge():
    try:
        minutes = float(minutes_entry.get())
        if minutes < 0:
            raise ValueError("Minutes cannot be negative.")

        if rate_var.get() == "Daytime":
            rate = 0.02
        elif rate_var.get() == "Evening":
            rate = 0.12
        elif rate_var.get() == "Off-Peak":
            rate = 0.05
        else:
            raise ValueError("Please select a rate category.")

        total_charge = minutes * rate
        messagebox.showinfo("Charge Calculation", f"The charge for your call is: ${total_charge:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Long-Distance Call Charge Calculator")

# Create a variable to hold the selected rate category
rate_var = tk.StringVar(value="Daytime")

# Create radio buttons for rate categories
tk.Radiobutton(root, text="Daytime (6:00 A.M. - 5:59 P.M.)", variable=rate_var, value="Daytime").pack(anchor=tk.W)
tk.Radiobutton(root, text="Evening (6:00 P.M. - 11:59 P.M.)", variable=rate_var, value="Evening").pack(anchor=tk.W)
tk.Radiobutton(root, text="Off-Peak (Midnight - 5:59 A.M.)", variable=rate_var, value="Off-Peak").pack(anchor=tk.W)

# Create an entry widget for minutes
tk.Label(root, text="Enter the number of minutes:").pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

# Create a button to calculate the charge
calculate_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_button.pack()

# Run the application
root.mainloop()

# Caleb Saari 4/24/25 Wk12 Program 3: Long-Distance Calls