import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import nbformat
from nbconvert import PDFExporter, HTMLExporter
import os
import sys
import subprocess


ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')

# Load an image
icon_path = os.path.join(ASSETS_DIR, 'icon.ico')

#########
# Theme #
#########
theme_path = os.path.join(ASSETS_DIR, 'Anthracite.json')
ctk.set_appearance_mode(theme_path)  # default
ctk.set_default_color_theme(theme_path)  # default

#######
# GUI #
#######


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('JupyterExport')
        self.resizable('False', 'False')
        self.minsize(270, 250)
        self.iconbitmap(default=icon_path)
        self.configure(fg_color='#35374B')

        ###########
        # Widgets #
        ###########
        frame_main = ctk.CTkFrame(self, fg_color='transparent', border_width=0)
        frame_main.pack(fill=tk.BOTH, expand=True, pady=20)

        # Create a StringVar variable
        self.text_variable = ctk.StringVar()
        self.text_variable.set("No file selected")  # Set initial value

        open_button = ctk.CTkButton(frame_main, text="Choose File", command=self.open_file_dialog)
        open_button.pack()

        # Create a Label widget and connect it to the StringVar variable
        label = ctk.CTkLabel(frame_main, textvariable=self.text_variable, text_color='white')
        label.pack()

        self.convert_to = ctk.StringVar(value="PDF")
        option_menu = ctk.CTkOptionMenu(frame_main, values=["PDF", "HTML"],
                                        variable=self.convert_to)
        option_menu.pack()

        self.output_file_var = ctk.StringVar()
        self.output_file_var.set("output")
        output_file_ent = ctk.CTkEntry(frame_main, textvariable=self.output_file_var)
        output_file_ent.pack(pady=20)

        self.convert_btn = ctk.CTkButton(frame_main, text="Convert", command=self.check_fun)
        self.convert_btn.pack(pady=20)

    def open_file_dialog(self):
        global file
        file = filedialog.askopenfilename(
            title="Select IPython Notebook File",
            filetypes=[("IPython Notebook Files", "*.ipynb")]
        )

        if file:
            # Extract the filename from the path
            file_name = os.path.basename(file)
            self.text_variable.set(file_name)
        else:
            self.text_variable.set("No file selected")

    def check_fun(self):
        # Create a new thread for the long-running function
        if self.text_variable.get() != "No file selected":
            self.convert_ipynb(file, self.output_file_var.get())
        else:
            messagebox.showerror("Error", "Please choose a file to convert!")

    def open_file_in_browser(self, file_path):
        """
        Open the file in the default file browser.
        """
        if os.name == 'nt':  # Windows
            os.startfile(file_path)
        elif os.name == 'posix':  # macOS or Linux
            subprocess.Popen(['xdg-open', file_path])
        else:
            raise NotImplementedError("Unsupported operating system")

    def convert_ipynb(self, ipynb_file, output):
        app.configure(cursor='wait')
        self.convert_btn.configure(state='disabled')

        if self.convert_to.get() == 'PDF':
            # Read the IPython Notebook
            with open(ipynb_file, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)

            # Initialize the PDF exporter
            pdf_exporter = PDFExporter()

            # Convert the notebook to PDF
            body, resources = pdf_exporter.from_notebook_node(nb)

            # Write the PDF
            with open(f'{output}.pdf', 'wb') as f:
                f.write(body)
        else:
            # Read the IPython Notebook
            with open(ipynb_file, 'r', encoding='utf-8') as f:
                nb = nbformat.read(f, as_version=4)

            # Initialize the HTML exporter
            html_exporter = HTMLExporter()

            # Convert the notebook to HTML
            body, resources = html_exporter.from_notebook_node(nb)

            # Write the HTML
            with open(f'{output}.html', 'w', encoding='utf-8') as f:
                f.write(body)

        self.convert_btn.configure(state='normal')
        app.configure(cursor="")
        messagebox.showinfo("Success", "Operation completed successfully!")

        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Open file dialog with initial directory set to script directory
        file_path = filedialog.askopenfilename(initialdir=script_dir)
        self.open_file_in_browser(file_path)

app = App()
app.mainloop()
