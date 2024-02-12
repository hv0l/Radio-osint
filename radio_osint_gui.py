import tkinter as tk
from tkinter import ttk

def dummy_operation():
    pass

def start_recording():
    frequency = frequency_entry.get()
    duration = duration_entry.get()
    dummy_operation()
    transcription_text.set("Trascrizione in corso...")

root = tk.Tk()
root.title("Advanced Radio Listener GUI")
root.geometry("400x300")  # Dimensione della finestra

style = ttk.Style()
style.theme_use('clam')

style.configure('TFrame', background='white')
style.configure('TLabel', background='white', font=('Arial', 10))
style.configure('TEntry', foreground='blue', font=('Arial', 10))
style.configure('TButton', foreground='blue', background='white', font=('Arial', 10))
style.map('TButton', background=[('active', 'light blue')])

mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mainframe['borderwidth'] = 2
mainframe['relief'] = 'groove'

frequency_text = tk.StringVar()
duration_text = tk.StringVar()
transcription_text = tk.StringVar()

frequency_label = ttk.Label(mainframe, text="Frequenza (Hz):")
frequency_label.grid(column=1, row=1, sticky=tk.W)
frequency_entry = ttk.Entry(mainframe, textvariable=frequency_text, justify=tk.CENTER)
frequency_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

duration_label = ttk.Label(mainframe, text="Durata (secondi):")
duration_label.grid(column=1, row=2, sticky=tk.W)
duration_entry = ttk.Entry(mainframe, textvariable=duration_text, justify=tk.CENTER)
duration_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))

start_button = ttk.Button(mainframe, text="Avvia Registrazione", command=start_recording)
start_button.grid(column=2, row=3, sticky=tk.W)

transcription_label = ttk.Label(mainframe, textvariable=transcription_text, wraplength=300)
transcription_label.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

frequency_entry.focus()

root.mainloop()
