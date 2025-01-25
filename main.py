import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pdf2image import convert_from_path


def convert_pdf_to_png():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        try:
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                image.save(f"page_{i + 1}.png", "PNG")
            messagebox.showinfo("Successo", "Conversione completata!")
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore: {e}")


root = tk.Tk()


window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)


root.title('Py - PDF to JPG Converter')
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


convert_button = tk.Button(root, text="Converti PDF in PNG", command=convert_pdf_to_png)
convert_button.pack(pady=20)


try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
