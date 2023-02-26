import tkinter as tk, os, sys

import tkinter.messagebox
import password

try:
    import pyperclip
    import customtkinter as ctk
except ModuleNotFoundError:
    if tkinter.messagebox.askyesnocancel("Missing dependencies", 
                                             "The application has detected missing dependencies. Do you want to install them?"):
        os.system("pip install -r requirements.txt")
        try:
            import pyperclip
            import customtkinter as ctk
            tkinter.messagebox.showinfo("Success!", "The dependencies have been installed successfully.")
        except ModuleNotFoundError:
            tkinter.messagebox.showwarning("Network Error", "You will need a strong internet connection for this. Please connect and try again.")
            sys.exit()
    else:
        tkinter.messagebox.showwarning("Process Failed", "Cannot run this application without the required dependencies.")
        sys.exit()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App:
    def __init__(self) -> None:
        
        self.screen = tk.Tk()
        self.screen.configure(bg="black")
        self.screen.title("Password Generator")

        self.screen_width, self.screen_height = int(.40*self.screen.winfo_screenwidth()), int(.60*self.screen.winfo_screenheight())
        self.screen.geometry("%sx%s" % (self.screen_width, self.screen_height))

        self.password_stringvar = tk.StringVar()
        
        tk.Label(self.screen,
                  text="Password generator", 
                  font=("Berlin Sans FB Demi", 40, "bold"), 
                  background="black", 
                  foreground="#20BEBE").pack(pady=(25, 0))

        self.password_length_entry = ctk.CTkEntry(self.screen, placeholder_text="Enter password length...", width=300, justify="center")
        self.button = tk.Button(self.screen, borderwidth=0, text="Generate password", font=(None, 18, "bold"), fg="black", command=lambda: self.generate_password(self.password_length_entry.get()))

        self.output_label = ctk.CTkLabel(self.screen, textvariable=self.password_stringvar)

        self.password_length_entry.pack(pady=(50, 0))        
        self.button.pack(pady=(60, 10))

        self.output_label.pack()
        
        self.copy_button = ctk.CTkButton(self.screen, text="COPY", command=self.copy_password_to_clipboard)
    
    def generate_password(self, length: str) -> str:
        self.copy_button.configure(text="COPY")
        try:
            self.password_length = int(length)
            self.password = password.generate_password(self.password_length)
            self.password_stringvar.set(self.password)
            self.copy_button.pack()
            print(self.password)
        except ValueError:
            tkinter.messagebox.showerror("Password generator Error", "Please enter a number for password length!")
    
    def copy_password_to_clipboard(self):
        pyperclip.copy(self.password_stringvar.get())
        self.copy_button.configure(text="TEXT COPIED")

if __name__ == "__main__":
    try:
        password_generator = App()
        password_generator.screen.mainloop()
    except ModuleNotFoundError:
        if tkinter.messagebox.askyesnocancel("Missing dependencies", 
                                             "The application has detected missing dependencies. Do you want to install them?"):
            os.system("pip install -r requirements.txt")
