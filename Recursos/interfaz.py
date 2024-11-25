from tkinter import *
from tkinter import messagebox as message


def calcular(par1, par2):
    if par1 == "AA" or par2 == "AA":
        message.showinfo("Probabilidad de ojos claros", "O(cero) si uno de los progenitores es Homocigota Dominante.")
        ojos_ma.set("")
        ojos_pa.set("")
    elif par1 == "Aa" and par2 == "Aa":
        message.showinfo("Probabilidad de ojos claros", "Ambas personas son Heterocigotas, la probabilidad será de 25%.")
        ojos_ma.set("")
        ojos_pa.set("")
    elif par1 == "Aa" and par2 == "aa":
        message.showinfo("Probabilidad de ojos claros", "Alelos maternos Heterocigotas y paternos Homocigotas Recesivos, la probabilidad será de un 50%.")
        ojos_ma.set("")
        ojos_pa.set("")
    elif par1 == "aa" and par2 == "Aa":
        message.showinfo("Probabilidad de ojos claros", "Alelos maternos Homocigotas Recesivos y paternos Heterocigotas, la probabilidad será de un 50%.")
        ojos_ma.set("")
        ojos_pa.set("")
    elif par1 == "aa" and par2 == "aa":
        message.showinfo("Probabilidad de ojos claros", "Ambos son Homocigotas Recesivos. Salvo una mutación, la probabilidad será del 100%.")
        ojos_ma.set("")
        ojos_pa.set("")
    else:
        message.showerror("Error!", "Solo coloque letras a mayúsculas o minúsculas")


app = Tk()

app.geometry("1300x800")
app.config(background="blueviolet")
app.title("Fenotipos y Genotipos")

campo_1 = Label(app,
                text="Calculadora Genética",
                bg="purple",
                fg="white",
                font="impact, 50")
campo_1.place(x="350", y="50")
campo_2 = Label(app,
                text="Colocar el porcentaje de ojos claros que puede tener",
                bg="purple",
                fg="white",
                font="courier, 25")
campo_2.place(x="300", y="150")
campo_2_1 = Label(app,
                  text="una persona según los alelos de los padres",
                  bg="purple",
                  fg="white",
                  font="courier, 25")
campo_2_1.place(x="365", y="210")
campo_3 = Label(app,
                text="Alelos maternos: ",
                bg="purple",
                fg="white",
                font="Sitka, 15")
campo_3.place(x="183", y="315")
campo_4 = Label(app,
                text="Alelos paternos: ",
                bg="purple",
                fg="white",
                font="Sitka, 15",
                width="14")
campo_4.place(x="183", y="370")

ojos_ma = StringVar()
ojos_pa = StringVar()

input_1 = Entry(app, textvariable=ojos_ma, bg="#FFFFFF", width="25")
input_1.place(x="350", y="320")
input_2 = Entry(app, textvariable=ojos_pa, bg="#FFFFFF", width="25")
input_2.place(x="350", y="375")

b_calcular = Button(app,
                    text="CALCULAR FENOTIPO Y GENOTIPO",
                    command=lambda: calcular(ojos_ma.get(), ojos_pa.get()),
                    overrelief="flat",
                    bg="purple",
                    activebackground="black",
                    activeforeground="purple",
                    fg="white",
                    font="impact, 20")
b_calcular.place(x="200", y="485")

app.mainloop()
