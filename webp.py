import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", ".jpg;.jpeg;*.png")])
    if file_paths:
        for file_path in file_paths:
            convert_to_webp(file_path)

def convert_to_webp(file_path):
    output_file = file_path[:file_path.rfind('.')] + '.webp'
    
    try:
        image = Image.open(file_path)
        image.save(output_file, 'WEBP')
        print(f"Image converted to WebP format and saved as {output_file}")
        converted_listbox.insert(tk.END, output_file)  # Add converted file to listbox
    except Exception as e:
        print(f"Conversion failed: {e}")

root = tk.Tk()
root.title("Image Converter")

select_button = tk.Button(root, text="Select Images", command=select_images)
select_button.pack()

converted_listbox = tk.Listbox(root)
converted_listbox.pack()

root.mainloop()