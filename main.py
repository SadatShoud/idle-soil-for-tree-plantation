import serial
import tkinter as tk

# Arduino serial communication setup
arduino_port = 'COM3'  # Change this to your Arduino port
baud_rate = 9600
arduino = serial.Serial(arduino_port, baud_rate)

# Function to read pH level from Arduino
def read_pH_level():
    try:
        pH_data = arduino.readline().decode('utf-8').strip()
        return float(pH_data)
    except Exception as e:
        print("Error reading pH level:", e)
        return None

# Function to check if water and fertilizer levels are ideal
def check_levels():
    pH_level = read_pH_level()
    if pH_level is not None:
        if pH_level < 6.5 or pH_level > 7.5:  # Adjust ideal pH range as needed
            alert_label.config(text="Alert: pH level is not ideal!", fg="red")
        else:
            alert_label.config(text="pH level is ideal", fg="green")
    else:
        alert_label.config(text="Error reading pH level", fg="red")

# Create main window
root = tk.Tk()
root.title("Tree Monitoring System")

# Display pH level
pH_label = tk.Label(root, text="pH Level:", font=("Arial", 12))
pH_label.grid(row=0, column=0)

pH_value_label = tk.Label(root, text="", font=("Arial", 12))
pH_value_label.grid(row=0, column=1)

# Alert label
alert_label = tk.Label(root, text="", font=("Arial", 12))
alert_label.grid(row=1, columnspan=2)

# Function to update pH level and check levels periodically
def update_values():
    pH_level = read_pH_level()
    if pH_level is not None:
        pH_value_label.config(text=str(pH_level))
    check_levels()
    root.after(5000, update_values)  # Update values every 5 seconds

# Start updating values
update_values()

# Run the application
root.mainloop()
