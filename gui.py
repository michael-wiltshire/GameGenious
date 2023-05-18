
from customtkinter import *
#from functions import *
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("GameGenius")
root.geometry("500x900")

frame1 = ctk.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both")

label = ctk.CTkLabel(master=frame1, text="Game Genius", font=('Roboto', 24))
label.grid(row=0, column=0, columnspan=2, pady=12, padx=10, sticky=E)

summoner_label = ctk.CTkLabel(master=frame1, text="Summoner Name:")
summoner_label.grid(row=1, column=0, pady=12, padx=10, sticky=W)

text_box = ctk.CTkEntry(master=frame1)
text_box.grid(row=1, column=1, pady=12, padx=10, sticky=W)

tips_label = ctk.CTkLabel(master=frame1, text="Tips:")
tips_label.grid(row=2, column=0, pady=12, padx=10, sticky=NW)

button = ctk.CTkButton(master=frame1, text="Start")

frame2 = ctk.CTkFrame(master=root)
frame2.pack(pady=20, padx=60, fill="both", expand=True)

ai_output = tk.Text(master=frame2, bg='black', fg='white', borderwidth=0, height=10, width=40) # traditional tkinter Text widget

def show_button_below_poem():
    button.grid(row=5, column=1, columnspan=10, pady=12, sticky=S)

def start_button_pushed():
    entered_text = text_box.get()
    print(entered_text)  # or do something else with the text
    poem = """
    Nature's first green is gold,
    Her hardest hue to hold.
    Her early leaf's a flower;
    But only so an hour.
    Then leaf subsides to leaf.
    So Eden sank to grief,
    So dawn goes down to day.
    Nothing gold can stay.
    """
    ai_output.insert(tk.END, poem)
    ai_output.pack()
    show_button_below_poem()

button.configure(command=start_button_pushed)
button.grid(row=4, column=1, columnspan=10, pady=12, sticky=S)

root.mainloop()