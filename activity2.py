from tkinter import *
from tkinter import messagebox
from PIL import image, imagetk
root = Tk()
root.title("note converter app menu")
root.configure(bg = "light blue")
root.geometry("650x400")
upload = Image.open("dollar-banknotes-frame_1150-6686.avif")
upload = upload.resize((300, 300))
image = imagetk.PhotoImage(upload)
label = Label(root, image=image, bg = 'light blue')
label.place(x = 180, y = 20)