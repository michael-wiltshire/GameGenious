from customtkinter import *
from functions import *
import tkinter as tk
import customtkinter as ctk

#test
def show_button_below_poem():
    button.grid(row=5, column=1, columnspan=10, pady=12, sticky=S)
    error_label.grid_forget()


def start_button_pushed():
    entered_text = text_box.get()
    poem = main(entered_text)
    if poem:
        ai_output.delete("1.0", "end")  # delete all previous text
        ai_output.insert(tk.END, poem)
        ai_output.pack()
        show_button_below_poem()
    else:
        error_label.grid(row=6, column=1, columnspan=10, pady=12, sticky=S)
        ai_output.delete("1.0", "end")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("GameGenius")
root.geometry("500x800")

frame1 = ctk.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both")

label = ctk.CTkLabel(master=frame1, text="Game Genius", font=('Roboto', 24))
label.grid(row=0, column=0, columnspan=2, pady=12, padx=10, sticky=E)

summoner_label = ctk.CTkLabel(master=frame1, text="Summoner Name:")
summoner_label.grid(row=1, column=0, pady=12, padx=10, sticky=W)

text_box = ctk.CTkEntry(master=frame1)
text_box.grid(row=1, column=1, pady=12, padx=10, sticky=W)
text_box.bind('<Return>', lambda event: start_button_pushed())

# Create the error label (initially hidden)
error_label = ctk.CTkLabel(master=frame1, text="No live game")

loading_label = ctk.CTkLabel(master=frame1, text="")
loading_label.grid(row=1, column=2)

# tips_label = ctk.CTkLabel(master=frame1, text="Tips:")
# tips_label.grid(row=2, column=0, pady=12, padx=10, sticky=NW)

button = ctk.CTkButton(master=frame1, text="Start")

frame2 = ctk.CTkFrame(master=root)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

ai_output = tk.Text(master=frame2, bg='black', fg='white', borderwidth=0, height=30, width=40, wrap='word') # traditional tkinter Text widget

button.configure(command=start_button_pushed)
button.grid(row=4, column=1, columnspan=10, pady=12, sticky=S)

root.mainloop()