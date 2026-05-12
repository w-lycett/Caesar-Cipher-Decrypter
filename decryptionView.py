# Import tkinter for GUI elements
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class CaesarView:
    # Constructor method
    def __init__(self, root):
        # Main window
        self.root = root
        self.root.title("Caesar Cipher Decrypter")
        self.root.geometry("700x450")
        self.root.minsize(500, 350)

        # Icon photo
        icon = tk.PhotoImage(file = "img/icon.png")
        self.root.iconphoto(False, icon)

        # Menu bar container
        self.menu_bar = tk.Menu(self.root)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label = "Clear", command = self.clear_fields)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.root.quit)
        self.menu_bar.add_cascade(label = "File", menu = self.file_menu)

        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff = 0)
        self.help_menu.add_command(label = "About", command = self.show_about)
        self.menu_bar.add_cascade(label = "Help", menu = self.help_menu)

        # Attach menu bar to window
        self.root.config(menu = self.menu_bar)

        # Main container frame
        self.main_frame = ttk.Frame(self.root, padding = 20)
        self.main_frame.pack(fill = "both", expand = True)

        # Title label
        self.title_label = ttk.Label(self.main_frame, text = "Caesar Cipher Decrypter", font = ("Segoe UI", 20, "bold"))
        self.title_label.grid(row = 0, column = 0, columnspan = 2, pady = (0, 20))

        # Input label
        self.input_label = ttk.Label(self.main_frame, text = "Enter encrypted text: ", font = ("Segoe UI", 11))
        self.input_label.grid(row = 1, column = 0, sticky = "w", pady = (0, 5))

        # Text entry
        self.text_entry = ScrolledText(self.main_frame, height = 6, wrap = "word", font = ("Consolas", 11))
        self.text_entry.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew", pady = (0, 15))

        # Crack button
        self.button = ttk.Button(self.main_frame, text = "Crack Cipher")
        self.button.grid(row = 3, column = 0, columnspan = 2, pady = (0, 20))

        # Result labels
        self.shift_label = ttk.Label(self.main_frame, text = "Detected shift: ", font = ("Segoe UI", 11))
        self.shift_label.grid(row = 4, column = 0, sticky = "w", pady = (0, 10))

        self.plaintext_label = ttk.Label(self.main_frame, text = "Decrypted text: ", font = ("Segoe UI", 11))
        self.plaintext_label.grid(row = 5, column = 0, sticky = "w", pady = (0, 5))

        # Output text area
        self.output_text = ScrolledText(self.main_frame, height = 8, wrap = "word", font = ("Consolas", 11), state = "disabled")
        self.output_text.grid(row = 6, column = 0, columnspan = 2, sticky = "nsew")

        # Responsive resizing
        self.main_frame.columnconfigure(0, weight = 1)
        self.main_frame.rowconfigure(2, weight = 1)
        self.main_frame.rowconfigure(6, weight = 1)

    # Gets ciphertext from text entry field
    def get_ciphertext(self):
        return self.text_entry.get("1.0", tk.END).strip()

    # Displays the shift and plaintext
    def display_result(self, shift, plaintext):
        self.shift_label.config(text = f"Detected shift: {shift}")
        self.output_text.config(state = "normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, plaintext)
        self.output_text.config(state = "disabled")
    
    # Clears input & output fields
    def clear_fields(self):
        self.text_entry.delete("1.0", tk.END)
        self.shift_label.config(text = "Detected shift: ")
        self.output_text.config(state = "normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state = "disabled")
    
    # Shows about message box
    def show_about(self):
        messagebox.showinfo("About", "Welcom to my Caesar Cipher Decrypter!\n\nBuilt using Python and Tkinter, it uses frequency analysis to decode Caesar ciphers.\nSimply enter your ciphertext in the upper box and click 'Crack Cipher'. The program will find the plaintext and display it in the lower box, as well as the shift used.")
