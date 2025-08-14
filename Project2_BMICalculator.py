import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def calculate_bmi_value(mass_kg: float, stature_m: float) -> float:
    return round(mass_kg / (stature_m ** 2), 2)

def interpret_bmi(value: float) -> str:
    if value < 18.5:
        return "Underweight"
    if value < 25:
        return "Healthy"
    if value < 30:
        return "Overweight"
    return "Obese"

def ideal_weight_limits(height_m: float) -> tuple:
    min_wt = 18.5 * (height_m ** 2)
    max_wt = 24.9 * (height_m ** 2)
    return round(min_wt, 2), round(max_wt, 2)

def ideal_height_limits(weight_kg: float) -> tuple:
    min_ht = (weight_kg / 24.9) ** 0.5
    max_ht = (weight_kg / 18.5) ** 0.5
    return round(min_ht, 2), round(max_ht, 2)

def store_history(value: float, label: str):
    record = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | BMI: {value} | Category: {label}\n"
    with open("bmi_log.txt", "a") as f:
        f.write(record)

# -------------------- UI Helper --------------------
def flash_label(widget: tk.Label, colors: list, repeat: int = 4):
 
    def change_color(count=0):
        widget.config(bg=colors[count % 2])
        if count < repeat:
            window.after(140, change_color, count + 1)
        else:
            widget.config(bg="SystemButtonFace")
    change_color()


def on_bmi_click():
    try:
        weight_val = float(entry_weight.get())
        height_val = float(entry_height.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter numeric values only.")
        return

    if weight_val <= 0 or height_val <= 0:
        messagebox.showerror("Invalid Data", "Weight/Height must be positive.")
        return

    # Unit conversion
    unit_w = weight_unit.get()
    unit_h = height_unit.get()
    if unit_w == "Pounds":
        weight_val *= 0.453592
    if unit_h == "Feet":
        height_val *= 0.3048

    # Compute
    bmi = calculate_bmi_value(weight_val, height_val)
    category = interpret_bmi(bmi)
    min_w, max_w = ideal_weight_limits(height_val)
    min_h, max_h = ideal_height_limits(weight_val)

    # Display
    lbl_bmi.config(text=f"Your BMI: {bmi}")
    lbl_category.config(text=f"Category: {category}")
    lbl_weight_range.config(text=f"Healthy Weight: {min_w} - {max_w} kg")
    lbl_height_range.config(text=f"Healthy Height: {min_h} - {max_h} m")

    # Effects
    flash_label(lbl_bmi, ["#D0F0C0", "SystemButtonFace"])
    flash_label(lbl_category, ["#FFD580", "SystemButtonFace"])

    # Save
    store_history(bmi, category)


window = tk.Tk()
window.title("BMI Health Tracker")
window.geometry("520x390")
window.resizable(False, False)

frame_main = ttk.Frame(window, padding=12)
frame_main.pack(fill="both", expand=True)

# Inputs
ttk.Label(frame_main, text="Enter Weight:").grid(row=0, column=0, sticky="w", pady=5)
entry_weight = ttk.Entry(frame_main)
entry_weight.grid(row=0, column=1, pady=5)
weight_unit = tk.StringVar(value="Kilograms")
ttk.Combobox(frame_main, textvariable=weight_unit,
             values=["Kilograms", "Pounds"], state="readonly", width=12).grid(row=0, column=2, padx=5)

ttk.Label(frame_main, text="Enter Height:").grid(row=1, column=0, sticky="w", pady=5)
entry_height = ttk.Entry(frame_main)
entry_height.grid(row=1, column=1, pady=5)
height_unit = tk.StringVar(value="Meters")
ttk.Combobox(frame_main, textvariable=height_unit,
             values=["Meters", "Feet"], state="readonly", width=12).grid(row=1, column=2, padx=5)

# Button
ttk.Button(frame_main, text="Check BMI", command=on_bmi_click).grid(row=2, column=0, columnspan=3, pady=12)

# Outputs
lbl_bmi = tk.Label(frame_main, text="Your BMI: --", font=("Arial", 11), anchor="w")
lbl_bmi.grid(row=3, column=0, columnspan=3, sticky="w", pady=3)

lbl_category = tk.Label(frame_main, text="Category: --", font=("Arial", 11), anchor="w")
lbl_category.grid(row=4, column=0, columnspan=3, sticky="w", pady=3)

lbl_weight_range = tk.Label(frame_main, text="Healthy Weight: --", font=("Arial", 11), anchor="w")
lbl_weight_range.grid(row=5, column=0, columnspan=3, sticky="w", pady=3)

lbl_height_range = tk.Label(frame_main, text="Healthy Height: --", font=("Arial", 11), anchor="w")
lbl_height_range.grid(row=6, column=0, columnspan=3, sticky="w", pady=3)

window.mainloop()
