import tkinter as tk
from tkinter import ttk


def set_values(device, param, value):
    print(f"{device}: {param} set to {value}")


def connect_device(device):
    print(f"{device}: Connected")


def disconnect_device(device):
    print(f"{device}: Disconnected")


# Create the main window
root = tk.Tk()
root.title("Device Control Panel")
root.geometry("1200x800")

# Device Frame Template
def create_device_frame(root, device_name):
    frame = ttk.LabelFrame(root, text=device_name, padding=5)
    frame.grid(sticky="ew", padx=5, pady=5)

    # Labels and sliders
    ttk.Label(frame, text="Voltage [V]").grid(row=0, column=0, sticky="w", padx=2, pady=2)
    voltage_slider = ttk.Scale(frame, from_=0, to=500, orient="horizontal")
    voltage_slider.grid(row=0, column=1, sticky="ew", padx=2)
    voltage_value_label = ttk.Label(frame, text=f"{voltage_slider.get():.2f} V")
    voltage_value_label.grid(row=0, column=2, padx=2)
    voltage_slider.bind("<Motion>", lambda e: voltage_value_label.config(text=f"{voltage_slider.get():.2f} V"))
    ttk.Button(frame, text="Set Volt", command=lambda: set_values(device_name, "Voltage", voltage_slider.get())).grid(row=0, column=3, padx=2)

    ttk.Label(frame, text="Source Current [A]").grid(row=1, column=0, sticky="w", padx=2, pady=2)
    current_slider = ttk.Scale(frame, from_=0, to=50, orient="horizontal")
    current_slider.grid(row=1, column=1, sticky="ew", padx=2)
    current_value_label = ttk.Label(frame, text=f"{current_slider.get():.2f} A")
    current_value_label.grid(row=1, column=2, padx=2)
    current_slider.bind("<Motion>", lambda e: current_value_label.config(text=f"{current_slider.get():.2f} A"))
    ttk.Button(frame, text="Set Current", command=lambda: set_values(device_name, "Current", current_slider.get())).grid(row=1, column=3, padx=2)

    ttk.Label(frame, text="Load Current [A]").grid(row=2, column=0, sticky="w", padx=2, pady=2)
    load_current_slider = ttk.Scale(frame, from_=-50, to=50, orient="horizontal")
    load_current_slider.grid(row=2, column=1, sticky="ew", padx=2)
    load_current_value_label = ttk.Label(frame, text=f"{load_current_slider.get():.2f} A")
    load_current_value_label.grid(row=2, column=2, padx=2)
    load_current_slider.bind("<Motion>", lambda e: load_current_value_label.config(text=f"{load_current_slider.get():.2f} A"))
    ttk.Button(frame, text="Set Load Current", command=lambda: set_values(device_name, "Load Current", load_current_slider.get())).grid(row=2, column=3, padx=2)

    ttk.Label(frame, text="Max Permitted Power [W]").grid(row=3, column=0, sticky="w", padx=2, pady=2)
    max_power_entry = ttk.Entry(frame)
    max_power_entry.grid(row=3, column=1, sticky="ew", padx=2)
    ttk.Button(frame, text="Set Power", command=lambda: set_values(device_name, "Max Power", max_power_entry.get())).grid(row=3, column=3, padx=2)

    # Status and buttons
    status_label = ttk.Label(frame, text="Status: Disconnected", foreground="red")
    status_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=2)

    ttk.Button(frame, text="Connect", command=lambda: [connect_device(device_name), status_label.config(text="Status: Connected", foreground="green")]).grid(row=5, column=0, pady=2)
    ttk.Button(frame, text="Disconnect", command=lambda: [disconnect_device(device_name), status_label.config(text="Status: Disconnected", foreground="red")]).grid(row=5, column=1, pady=2)

    return frame


# Power Supply Device
def create_power_supply_frame(root, device_name):
    frame = ttk.LabelFrame(root, text=device_name, padding=5)
    frame.grid(sticky="ew", padx=5, pady=5)

    for i in range(2):  # 2 channels
        channel_frame = ttk.LabelFrame(frame, text=f"Channel {i + 1}", padding=5)
        channel_frame.grid(row=i, column=0, sticky="ew", padx=2, pady=2)

        ttk.Label(channel_frame, text="Voltage [V]").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        voltage_slider = ttk.Scale(channel_frame, from_=0, to=300, orient="horizontal")
        voltage_slider.grid(row=0, column=1, sticky="ew", padx=2)
        voltage_value_label = ttk.Label(channel_frame, text=f"{voltage_slider.get():.2f} V")
        voltage_value_label.grid(row=0, column=2, padx=2)
        voltage_slider.bind("<Motion>", lambda e, label=voltage_value_label: label.config(text=f"{voltage_slider.get():.2f} V"))
        ttk.Button(channel_frame, text="Set Voltage", command=lambda ch=i: set_values(f"{device_name} Ch {ch + 1}", "Voltage", voltage_slider.get())).grid(row=0, column=3, padx=2)

        ttk.Label(channel_frame, text="Current [A]").grid(row=1, column=0, sticky="w", padx=2, pady=2)
        current_slider = ttk.Scale(channel_frame, from_=0, to=10, orient="horizontal")
        current_slider.grid(row=1, column=1, sticky="ew", padx=2)
        current_value_label = ttk.Label(channel_frame, text=f"{current_slider.get():.2f} A")
        current_value_label.grid(row=1, column=2, padx=2)
        current_slider.bind("<Motion>", lambda e, label=current_value_label: label.config(text=f"{current_slider.get():.2f} A"))
        ttk.Button(channel_frame, text="Set Current", command=lambda ch=i: set_values(f"{device_name} Ch {ch + 1}", "Current", current_slider.get())).grid(row=1, column=3, padx=2)

    # Status and buttons
    status_label = ttk.Label(frame, text="Status: Disconnected", foreground="red")
    status_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=2)

    ttk.Button(frame, text="Connect", command=lambda: [connect_device(device_name), status_label.config(text="Status: Connected", foreground="green")]).grid(row=3, column=0, pady=2)
    ttk.Button(frame, text="Disconnect", command=lambda: [disconnect_device(device_name), status_label.config(text="Status: Disconnected", foreground="red")]).grid(row=3, column=1, pady=2)

    return frame


# Temperature Chamber Device
def create_temperature_chamber_frame(root, device_name):
    frame = ttk.LabelFrame(root, text=device_name, padding=5)
    frame.grid(sticky="ne", padx=5, pady=5)

    ttk.Label(frame, text="Set Temperature [°C]").grid(row=0, column=0, sticky="w", padx=2, pady=2)
    temperature_slider = ttk.Scale(frame, from_=-40, to=150, orient="horizontal")
    temperature_slider.grid(row=0, column=1, sticky="ew", padx=2)
    temperature_value_label = ttk.Label(frame, text=f"{temperature_slider.get():.2f} °C")
    temperature_value_label.grid(row=0, column=2, padx=2)
    temperature_slider.bind("<Motion>", lambda e: temperature_value_label.config(text=f"{temperature_slider.get():.2f} °C"))
    ttk.Button(frame, text="Set Temperature", command=lambda: set_values(device_name, "Set Temperature", temperature_slider.get())).grid(row=0, column=3, padx=2)

    ttk.Label(frame, text="Read Temperature [°C]").grid(row=1, column=0, sticky="w", padx=2, pady=2)
    temperature_entry = ttk.Entry(frame)
    temperature_entry.grid(row=1, column=1, sticky="ew", padx=2)

    # Status and buttons
    status_label = ttk.Label(frame, text="Status: Disconnected", foreground="red")
    status_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=2)

    ttk.Button(frame, text="Connect", command=lambda: [connect_device(device_name), status_label.config(text="Status: Connected", foreground="green")]).grid(row=3, column=0, pady=2)
    ttk.Button(frame, text="Disconnect", command=lambda: [disconnect_device(device_name), status_label.config(text="Status: Disconnected", foreground="red")]).grid(row=3, column=1, pady=2)

    return frame


# Regenerative Grid Simulator Frame
def create_regenerative_grid_simulator_frame(root, device_name):
    frame = ttk.LabelFrame(root, text=device_name, padding=5)
    frame.grid(sticky="se", padx=5, pady=5)

    ttk.Label(frame, text="Phase Mode").grid(row=0, column=0, sticky="w", padx=2, pady=2)
    phase_mode_dropdown = ttk.Combobox(frame, values=["Single Phase", "Three Phase"], state="readonly")
    phase_mode_dropdown.set("Three Phase")
    phase_mode_dropdown.grid(row=0, column=1, sticky="ew", padx=2)

    ttk.Label(frame, text="Operation Mode").grid(row=1, column=0, sticky="w", padx=2, pady=2)
    operation_mode_dropdown = ttk.Combobox(frame, values=["Source", "Load"], state="readonly")
    operation_mode_dropdown.set("Source")
    operation_mode_dropdown.grid(row=1, column=1, sticky="ew", padx=2)

    for i, phase in enumerate(["Phase A", "Phase B", "Phase C"]):
        phase_frame = ttk.LabelFrame(frame, text=phase, padding=5)
        phase_frame.grid(row=2, column=i, sticky="nw", padx=2, pady=2)

        ttk.Label(phase_frame, text="Voltage [V]").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        voltage_slider = ttk.Scale(phase_frame, from_=0, to=500, orient="horizontal")
        voltage_slider.grid(row=0, column=1, sticky="ew", padx=2)
        voltage_value_label = ttk.Label(phase_frame, text=f"{voltage_slider.get():.2f} V")
        voltage_value_label.grid(row=0, column=2, padx=2)
        voltage_slider.bind("<Motion>", lambda e, label=voltage_value_label: label.config(text=f"{voltage_slider.get():.2f} V"))

        ttk.Label(phase_frame, text="Frequency [Hz]").grid(row=1, column=0, sticky="w", padx=2, pady=2)
        frequency_slider = ttk.Scale(phase_frame, from_=0, to=100, orient="horizontal")
        frequency_slider.grid(row=1, column=1, sticky="ew", padx=2)
        frequency_value_label = ttk.Label(phase_frame, text=f"{frequency_slider.get():.2f} Hz")
        frequency_value_label.grid(row=1, column=2, padx=2)
        frequency_slider.bind("<Motion>", lambda e, label=frequency_value_label: label.config(text=f"{frequency_slider.get():.2f} Hz"))

    # Status and buttons for Grid Simulator
    status_label = ttk.Label(frame, text="Status: Disconnected", foreground="red")
    status_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=2)

    ttk.Button(frame, text="Connect", command=lambda: [connect_device(device_name), status_label.config(text="Status: Connected", foreground="green")]).grid(row=4, column=0, pady=2)
    ttk.Button(frame, text="Disconnect", command=lambda: [disconnect_device(device_name), status_label.config(text="Status: Disconnected", foreground="red")]).grid(row=4, column=1, pady=2)

    return frame


# Add devices to the panel
lv_source_frame = create_device_frame(root, "LV SOURCE ")
lv_source_frame.grid(row=0, column=0, padx=5, pady=5)

# Add TEST BENCH AUTOMATION label next to LV Source


hv_source_frame = create_device_frame(root, "HV SOURCE ")
hv_source_frame.grid(row=1, column=0, padx=5, pady=5)

power_supply_frame = create_power_supply_frame(root, "Power Supply ")
power_supply_frame.grid(row=0, column=1, padx=5, pady=5)

temperature_chamber_frame = create_temperature_chamber_frame(root, "Temperature Chamber s")
temperature_chamber_frame.grid(row=1, column=1, padx=5, pady=5)

regenerative_grid_simulator_frame = create_regenerative_grid_simulator_frame(root, "Regenerative Grid Simulator (Chroma 61800)")
regenerative_grid_simulator_frame.grid(row=2, column=0, padx=5, pady=5)

# Start the main event loop
root.mainloop()
