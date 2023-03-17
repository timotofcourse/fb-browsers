import os
import tkinter # In some code editors it may seem tkinter is not used but it's required to import it to use customtkinter
import customtkinter

# App Properties

customtkinter.set_appearance_mode("system") # Auto change to dark and light mode
customtkinter.set_default_color_theme("blue") # Accent Color
app = customtkinter.CTk()
app.geometry("300x500") # Window Size
app.title('FB Browsers') # Window Title
app.iconbitmap('icon.ico') # Window Icon
app.resizable(False, False)

home = os.path.expanduser('~')

# Functions to install the browsers

def installbrave():
    brave = 'winget install -e --id Brave.Brave'
    os.system(brave)

def installchrome():
    chrome = 'winget install -e --id Brave.Brave'
    os.system(chrome)

def installfirefox():
    firefox = 'winget install -e --id Mozilla.Firefox'
    os.system(firefox)

def installopera():
    opera = 'winget install -e --id Opera.Opera'
    os.system(opera)

def installoperagx():
    operagx = 'winget install -e --id Opera.OperaGX'
    os.system(operagx)

def installvivaldi():
    vivaldi = 'winget install -e --id VivaldiTechnologies.Vivaldi'
    os.system(vivaldi)


# UI Widgets

label = customtkinter.CTkLabel(master=app, text="Click on the browser you want to install")
bravebtn = customtkinter.CTkButton(master=app, text="Install Brave", command=installbrave)
chromebtn = customtkinter.CTkButton(master=app, text="Install Chrome", command=installchrome)
firefoxbtn = customtkinter.CTkButton(master=app, text="Install Firefox", command=installfirefox)
operabtn = customtkinter.CTkButton(master=app, text="Install Opera", command=installopera)
operagxbtn = customtkinter.CTkButton(master=app, text="Install OperaGx", command=installoperagx)
vivaldibtn = customtkinter.CTkButton(master=app, text="Install Vivaldi", command=installvivaldi)
label.pack(padx=20, pady=20)
bravebtn.pack(padx=20, pady=20)
chromebtn.pack(padx=20, pady=20)
firefoxbtn.pack(padx=20, pady=20)
operabtn.pack(padx=20, pady=20)
operagxbtn.pack(padx=20, pady=20)
vivaldibtn.pack(padx=20, pady=20)

app.mainloop() # Launch App
