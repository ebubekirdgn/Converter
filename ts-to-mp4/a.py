import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

selected_file = ""

def select_file():
    global selected_file
    file_path = filedialog.askopenfilename(filetypes=[("TS files", "*.ts")])

    if file_path:
        selected_file = file_path
        label.config(text=os.path.basename(file_path))

def convert_file():
    if not selected_file:
        messagebox.showwarning("Uyarı", "Önce .ts dosyası seç!")
        return

    try:
        output_file = selected_file.replace(".ts", ".mp4")

        clip = VideoFileClip(selected_file)
        clip.write_videofile(output_file, codec="libx264")

        messagebox.showinfo("Başarılı", f"Dönüştürüldü:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Hata", str(e))


# UI
root = tk.Tk()
root.title("TS → MP4 Converter")
root.geometry("400x200")

label = tk.Label(root, text="Dosya seçilmedi")
label.pack(pady=20)

btn1 = tk.Button(root, text="TS Dosyası Seç", command=select_file)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="MP4'e Çevir", command=convert_file)
btn2.pack(pady=10)

root.mainloop()