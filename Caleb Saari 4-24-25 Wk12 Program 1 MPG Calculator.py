# The application will feature input fields for the user to enter the total number of gallons
# the car's gas tank holds and the total number of miles that can be driven on a full tank.

import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        if gallons <= 0:
            raise ValueError("Gallons must be greater than zero.")
        mpg = miles / gallons
        result_label.config(text=f"MPG: {mpg:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Car Gas Mileage Calculator")

# Create and place the labels and entry widgets
tk.Label(root, text="Gallons of Gas:").grid(row=0, column=0, padx=10, pady=10)
gallons_entry = tk.Entry(root)
gallons_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Miles Driven:").grid(row=1, column=0, padx=10, pady=10)
miles_entry = tk.Entry(root)
miles_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calculate_button.grid(row=2, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()

# Caleb Saari 4/24/25 Wk12 Program 1: MPG Calculator