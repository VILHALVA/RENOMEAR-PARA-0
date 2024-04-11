import os
import tkinter as tk
from tkinter import filedialog

def rename_files(directory):
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename[0].isdigit():
                new_filename = '0' + filename
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
        info_label.config(text="Arquivos renomeados com sucesso!")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        rename_files(directory)

window = tk.Tk()
window.title("RENOMEAR +0")

footer_label = tk.Label(window, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
footer_label.pack(side=tk.BOTTOM, fill=tk.X)        
window.state('zoomed')

browse_button = tk.Button(window, text="ESCOLHER", command=browse_directory)
browse_button.pack(pady=20)

info_label = tk.Label(window, text="")
info_label.pack()

window.mainloop()
