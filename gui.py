import customtkinter
from customtkinter import *

ctk = customtkinter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("GameGenious")
root.geometry("500x350")

def interface():
	print("beep beep")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = ctk.CTkLabel(master=frame,text="Game Genious",font=('Roboto',24))
label.pack(pady=12,padx=10)


#in here connect command=main
button = ctk.CTkButton(master=frame,text="Start")
button.pack(side=BOTTOM)
root.mainloop()