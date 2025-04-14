'''# main.py
import tkinter as tk
from tkinter import messagebox
from license_system import License, sign_license, save_license_file, load_and_verify_license

PRIVATE_KEY_PATH = "certificate/LicenseSign.pem"
PUBLIC_KEY_PATH = "certificate/LicenseVerify.pem"
PRIVATE_KEY_PASSWORD = "demo"

class ActivationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Activate License")
        self.geometry("300x250")

        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()

        tk.Label(self, text="Select Features to Enable:").pack(pady=10)
        tk.Checkbutton(self, text="Enable Feature 1", variable=self.var1).pack(anchor="w", padx=20)
        tk.Checkbutton(self, text="Enable Feature 2", variable=self.var2).pack(anchor="w", padx=20)
        tk.Checkbutton(self, text="Enable Feature 3", variable=self.var3).pack(anchor="w", padx=20)

        tk.Button(self, text="Activate", command=self.activate).pack(pady=20)
        tk.Button(self, text="Cancel", command=self.destroy).pack()

    def activate(self):
        license_obj = License(
            feature1=self.var1.get(),
            feature2=self.var2.get(),
            feature3=self.var3.get()
        )
        license_json = license_obj.to_json()
        signature = sign_license(license_json, PRIVATE_KEY_PATH, PRIVATE_KEY_PASSWORD)
        save_license_file(license_obj, signature)
        messagebox.showinfo("Activation", "License activated successfully!")
        self.destroy()
        self.master.reload_license()


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Licensed Application")
        self.geometry("400x300")

        self.label_status = tk.Label(self, text="Checking license...", fg="blue", font=("Arial", 12))
        self.label_status.pack(pady=20)

        self.frame_features = tk.Frame(self)
        self.frame_features.pack(pady=10)

        self.btn_activate = tk.Button(self, text="Activate License", command=self.open_activation)
        self.btn_activate.pack(pady=10)

        self.reload_license()

    def reload_license(self):
        for widget in self.frame_features.winfo_children():
            widget.destroy()

        license_obj = load_and_verify_license(PUBLIC_KEY_PATH)
        if license_obj:
            self.label_status.config(text="License: VALID", fg="green")

            if license_obj.feature1:
                tk.Label(self.frame_features, text="Feature 1 is Enabled ✅").pack()
            if license_obj.feature2:
                tk.Label(self.frame_features, text="Feature 2 is Enabled ✅").pack()
            if license_obj.feature3:
                tk.Label(self.frame_features, text="Feature 3 is Enabled ✅").pack()
        else:
            self.label_status.config(text="License: INVALID or MISSING", fg="red")
            tk.Label(self.frame_features, text="Please activate to use features.").pack()

    def open_activation(self):
        ActivationWindow(self)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
'''
import sys
import os
import tkinter as tk
from tkinter import messagebox
from license_system import License, sign_license, save_license_file, load_and_verify_license

# For bundled or normal paths
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller .exe """
    try:
        base_path = sys._MEIPASS  # PyInstaller uses this temp folder
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Updated certificate paths using resource_path
PRIVATE_KEY_PATH = resource_path("certificate/LicenseSign.pem")
PUBLIC_KEY_PATH = resource_path("certificate/LicenseVerify.pem")
PRIVATE_KEY_PASSWORD = "demo"

class ActivationWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Activate License")
        self.geometry("300x250")

        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()

        tk.Label(self, text="Select Features to Enable:").pack(pady=10)
        tk.Checkbutton(self, text="Enable Feature 1", variable=self.var1).pack(anchor="w", padx=20)
        tk.Checkbutton(self, text="Enable Feature 2", variable=self.var2).pack(anchor="w", padx=20)
        tk.Checkbutton(self, text="Enable Feature 3", variable=self.var3).pack(anchor="w", padx=20)

        tk.Button(self, text="Activate", command=self.activate).pack(pady=20)
        tk.Button(self, text="Cancel", command=self.destroy).pack()

    def activate(self):
        license_obj = License(
            feature1=self.var1.get(),
            feature2=self.var2.get(),
            feature3=self.var3.get()
        )
        license_json = license_obj.to_json()
        signature = sign_license(license_json, PRIVATE_KEY_PATH, PRIVATE_KEY_PASSWORD)
        save_license_file(license_obj, signature)
        messagebox.showinfo("Activation", "License activated successfully!")
        self.destroy()
        self.master.reload_license()


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Licensed Application")
        self.geometry("400x300")

        self.label_status = tk.Label(self, text="Checking license...", fg="blue", font=("Arial", 12))
        self.label_status.pack(pady=20)

        self.frame_features = tk.Frame(self)
        self.frame_features.pack(pady=10)

        self.btn_activate = tk.Button(self, text="Activate License", command=self.open_activation)
        self.btn_activate.pack(pady=10)

        self.reload_license()

    def reload_license(self):
        for widget in self.frame_features.winfo_children():
            widget.destroy()

        license_obj = load_and_verify_license(PUBLIC_KEY_PATH)
        if license_obj:
            self.label_status.config(text="License: VALID", fg="green")

            if license_obj.feature1:
                tk.Label(self.frame_features, text="Feature 1 is Enabled ✅").pack()
            if license_obj.feature2:
                tk.Label(self.frame_features, text="Feature 2 is Enabled ✅").pack()
            if license_obj.feature3:
                tk.Label(self.frame_features, text="Feature 3 is Enabled ✅").pack()
        else:
            self.label_status.config(text="License: INVALID or MISSING", fg="red")
            tk.Label(self.frame_features, text="Please activate to use features.").pack()

    def open_activation(self):
        ActivationWindow(self)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
