import tkinter as tk
from tkinter import scrolledtext, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from translate import Translator


def open_file():
    """Open a file for editing."""
    global filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert("1.0", text)
    window.title(f"SimplyEdit - {filepath}")


def save_file_as():
    """Save the current file as a new file."""
    new_filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not new_filepath:
        return
    with open(new_filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"SimplyEdit - {new_filepath}")


def save_file():
    if filepath:
        with open(filepath, "w") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"SimplyEdit - {filepath}")


def trans():
    f = from_lang.get()
    t = to_lang.get()
    translator = Translator(from_lang=f, to_lang=t)
    i = 1
    for word in txt_edit.get("1.0", tk.END).splitlines():
        result = translator.translate(word)
        if len(word) > 0:
            txt_edit.insert(f"{i}.{str(len(word))}", f" - {result}")
        i += 1
    translation_mode.destroy()


window = tk.Tk()

translated = []
tablica_Ready = []
window.title("SimplyEdit")

window.rowconfigure(0, minsize=780, weight=1)
window.rowconfigure(1, minsize=20, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = scrolledtext.ScrolledText(master=window, font=("Helvetica", 14))
fr_buttons = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)

btn_open = tk.Button(master=fr_buttons, text="Open", command=open_file)
btn_save_as = tk.Button(master=fr_buttons, text="Save As...", command=save_file_as)
btn_save = tk.Button(master=fr_buttons, text="Save", command=save_file)
btn_trans = tk.Button(master=fr_buttons, text="Translate", command=trans)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_save_as.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_trans.grid(row=3, column=0, sticky="ew", padx=5, pady=10)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

translation_mode = tk.Frame(master=window)

lbl_description = tk.Label(master=translation_mode, text="Chose translation mode: ", font=("Helvetica", 13))
lbl_select = ttk.Label(master=translation_mode, text="Select:", font=("Helvetica", 11))

from_lang = ttk.Combobox(master=translation_mode, width=13)
from_lang['values'] = ['en', 'pl', 'no']
from_lang.current(0)

to_lang = ttk.Combobox(master=translation_mode, width=13)
to_lang['values'] = ['en', 'pl', 'no']
to_lang.current()

lbl_description.grid(column=0, row=5, padx=10, pady=3)
from_lang.grid(column=1, row=5)
to_lang.grid(column=2, row=5, padx=20)

translation_mode.grid(row=1, column=1, sticky="e")

window.mainloop()
