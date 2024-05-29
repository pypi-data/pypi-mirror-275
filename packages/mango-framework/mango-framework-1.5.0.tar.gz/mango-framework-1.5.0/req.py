import tkinter as tk
from tkinter import Text, ttk 
from tkinter import messagebox
app = tk.Tk()
app.title("test note pad")
app.config(height=500,width=680)




T = Text(
    app,
)


def c1():
    TEXT2 = T.get("1.0","end-1c")
    sub = tk.Toplevel()
    sub.title("save options")
    sub.config(height=240,width=240)
    
    def CS():
        sub.destroy()

    bs = ttk.Button(
        sub,
        text = "close",
        command = CS
    )


    e1 = ttk.Entry(
        sub,
        width=37
    )
    
    def GET():
        TEXT = e1.get() + ".txt"
        EXEC = ".txt"
        with open(TEXT,"w") as f:
            f.write(TEXT2)
            messagebox.showinfo("file saved","check your folder")
            

    bx = ttk.Button(
        sub,
        text="save",
        command = GET
)
        
    

    e1 = ttk.Entry(
        sub,
        width=37
    )

    bx.place(x=140,y=200)
    e1.place(x=5,y=100)
    bs.place(x=20,y=200)
    sub.mainloop()


def c2():
    TEXT2 = T.get("1.0","end-1c")
    sub = tk.Toplevel()
    sub.title("save as")
    sub.config(height=240,width=240)

    e1 = ttk.Entry(
        sub,
        width=37
    )
    def c5():
        TEXT3 = e1.get()
        TEXT4 = TEXT3 + ".bat"
        with open(TEXT4,"w") as f:
            f.write(TEXT2)
            messagebox.showinfo("saved file","check the folder")

    def c6():
        TEXT3 = e1.get()
        TEXT4 = TEXT3 + ".txt"
        with open(TEXT4,"w") as f:
            f.write(TEXT2)
            messagebox.showinfo("saved file","check the folder")

    def c7():
        TEXT3 = e1.get()
        TEXT4 = TEXT3 + ".ps1"
        with open(TEXT4,"w") as f:
            f.write(TEXT2)
            messagebox.showinfo("saved file","check the folder")
    

    def c8():
        TEXT3 = e1.get()
        TEXT4 = TEXT3 + ".sh"
        with open(TEXT4,"w") as f:
            f.write(TEXT2)
            messagebox.showinfo("saved file","check the folder")
    
    def c9():
        sub.destroy()
            

    ba = ttk.Button(
        sub,
        text = ".bat",
        command = c5
    )

    ba1 = ttk.Button(
        sub,
        text = ".txt",
        command = c6
    )

    ba2 = ttk.Button(
        sub,
        text = ".ps1",
        command = c7
    )

    ba3 = ttk.Button(
        sub,
        text = ".sh",
        command = c8
    )

    ba4 = ttk.Button(
        sub,
        text = "close",
        command = c9
    )
    ba2.place(x=5, y=170)
    ba3.place(x=160, y=170)
    ba4.place(x=82, y=200)
    ba1.place(x=160, y=200)
    ba.place(x=5,y=200)
    e1.place(x=5,y=100)
    sub.mainloop()

b = ttk.Button(
    app,
    text="save",
    command= c1
)

b1 = ttk.Button(
    app,
    text= "save as",
    command = c2
)

def cx():
    app.destroy()

b2 = ttk.Button(
    app,
    text = "close",
    command = cx
)
b2.place(x=580,y=450)
b1.place(x=300, y=450)
b.place(x=30,y=450)
T.place(x=15,y=10)
app.mainloop()
