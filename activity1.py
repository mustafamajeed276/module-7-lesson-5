from tkinter import *
root = Tk()
root.title('main')
root.geometry("400x300")
def topwin():
    top = Toplevel()
    top.title("top window")
    top.geometry("180x100")
    l2 = Label(top, text = "tricked you haha!!!")
    l2.pack()
    top.mainloop()
l = Label(root, text = "this is the root window!!!")
btn = Button(root, text = "tap this to exit", command = topwin)
l.pack()
btn.pack()
root.mainloop()