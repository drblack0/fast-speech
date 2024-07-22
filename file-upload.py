import tkinter as tk
from tkinter import filedialog

def upload_file():
  file_path = filedialog.askopenfilename()
  if file_path:
    file_label.config(text=file_path)
    # Do something with the uploaded file
    

root = tk.Tk()
root.title("File Uploader")

upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack()

file_label = tk.Label(root, text="")
file_label.pack()

root.mainloop()