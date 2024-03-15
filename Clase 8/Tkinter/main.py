from tkinter import *
from tkinter import messagebox


nombre = "a"

def enviar(nombre_):
    messagebox.showinfo("Nombre", nombre_)

def main():
    root = Tk()
    root.geometry('300x200')
    root.configure(bg='#EBD49F')

    label1 = Label(root, text="Nombre", bg='#EBCDB9')
    label1.place(x=10, y=5)
    #label1.pack()

    inputNombre = Entry(root, textvariable=nombre)
    inputNombre.place(x=15, y=30)

    button = Button(root, text='Aceptar', command=lambda:enviar(inputNombre.get()))
    button.place(x=15, y=55)
    root.mainloop()

if __name__ == "__main__":
    main()