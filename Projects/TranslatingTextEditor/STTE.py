import tkinter as tk
from tkinter import scrolledtext, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from googletrans import Translator


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
    window.title(f"STTE - {filepath}")


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
    window.title(f"STTE - {new_filepath}")


def save_file():
    """Save the contents in a OPENED file"""
    if filepath:
        with open(filepath, "w") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"STTE - {filepath}")


def clean():
    txt_edit.delete("1.0", tk.END)
    return


def trans():
    """Translates the contents of text box after choosing proper setting and pressing "translate button" """
    f = str(from_lang.get())
    t = str(to_lang.get())

    # checking if user has chosen proper translation settings
    values = ['en', 'pl', 'no']
    if f not in values or t not in values:
        return

    # translating and inserting translated words into the text box
    translator = Translator(service_urls=['translate.google.com'])
    origins = []
    for word in txt_edit.get("1.0", tk.END).splitlines():
        origins.append(word)
    translations = translator.translate(origins, src=f'{f}', dest=f'{t}')
    txt_edit.delete("1.0", tk.END)
    for translation in translations:
        txt_edit.insert(tk.END, f"{str(translation.origin)} - {str(translation.text)}\n")

"""
        result = translator.translate(word, dest=f, src=t)
        txt_edit.insert(f"{i}.{str(len(word))}", f" - {result}")
                if len(word) > 0:
            
        i += 1
"""
# CREATING GUI


window = tk.Tk()
# setting window parameters
window.title("STTE")
window.event_add('<<Paste>>', '<Control-v>')
window.event_add('<<Cut>>', '<Control-x>')
window.event_add('<<Copy>>', '<Control-v>')

# configuring the layout of the window
window.rowconfigure(0, minsize=780, weight=1)
window.rowconfigure(1, minsize=20, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


txt_edit = scrolledtext.ScrolledText(master=window, font=("Helvetica", 14))

# creating buttons
fr_buttons = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)
btn_open = tk.Button(master=fr_buttons, text="Open", command=open_file)
btn_save_as = tk.Button(master=fr_buttons, text="Save As...", command=save_file_as)
btn_save = tk.Button(master=fr_buttons, text="Save", command=save_file)
btn_clean = tk.Button(master=fr_buttons, text="Clean", command=clean)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_save_as.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_clean.grid(row=3, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")

# translation segment
translation_mode = tk.Frame(master=window)

lbl_description = tk.Label(master=translation_mode, text="Chose translation:", font=("Helvetica", 13))
btn_trans = tk.Button(master=translation_mode, text="Translate", command=trans)

from_lang = ttk.Combobox(master=translation_mode, state="readonly", width=13)
from_lang['values'] = ['en', 'pl', 'no']
from_lang.current(0)

to_lang = ttk.Combobox(master=translation_mode, state="readonly", width=13)
to_lang['values'] = ['en', 'pl', 'no']
to_lang.current()

lbl_description.grid(column=10, row=5, padx=10, pady=10)
from_lang.grid(column=11, row=5)
to_lang.grid(column=12, row=5, padx=5)
btn_trans.grid(column=13, row=5, sticky="ew", padx=20)

translation_mode.grid(row=1, column=1, sticky="e")

window.mainloop()
