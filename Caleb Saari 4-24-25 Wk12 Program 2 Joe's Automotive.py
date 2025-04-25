# The services include an oil change, lube job, radiator flush, transmission fluid,
# inspection, muffler replacement, and tire rotation, each with a specified cost.
# Upon selection of the services, the user can click a button to calculate and display the
# total charges.

import tkinter as tk
from tkinter import messagebox

# Service costs
service_costs = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Fluid": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00
}


def calculate_total():
    total = 0
    selected_services = []

    for service, var in service_vars.items():
        if var.get():
            selected_services.append(service)
            total += service_costs[service]

    if selected_services:
        messagebox.showinfo("Total Charges",
                            f"Selected Services: {', '.join(selected_services)}\nTotal Charges: ${total:.2f}")
    else:
        messagebox.showwarning("No Selection", "Please select at least one service.")


# Create the main window
root = tk.Tk()
root.title("Joe's Automotive Service Cost Calculator")

# Create a dictionary to hold the variable references for each service
service_vars = {}

# Create check buttons for each service
for service in service_costs.keys():
    var = tk.BooleanVar()
    service_vars[service] = var
    cb = tk.Checkbutton(root, text=service, variable=var)
    cb.pack(anchor='w')

# Create a button to calculate total charges
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack()

# Run the application
root.mainloop()

# Caleb Saari 4/24/25 Wk12 Program 2: Joe's Automotive