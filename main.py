import tkinter
from tkinter import Tk, Button, Entry, messagebox

bandera_decimal = False
operador = None
numero1 = None
numero2 = None


def ingreso(ingreso):
    def resultado():
        if operador == "+":
            return str(numero1 + numero2)
        elif operador == "-":
            return str(numero1 - numero2)
        elif operador == "*":
            return str(numero1 * numero2)
        else:
            return str(numero1 / numero2)

    global bandera_decimal
    global operador
    global numero1
    global numero2

    if ingreso == "+" or ingreso == "-" or ingreso == "*" or ingreso == "/":
        operador = ingreso
        numero1 = float(pantalla.get())
        pantalla.delete(0, tkinter.END)
        bandera_decimal = False

    elif ingreso == "=":
        numero2 = float(pantalla.get())

        if numero1 is not None and numero2 is not None:
            pantalla.delete(0, tkinter.END)
            pantalla.insert(tkinter.END, resultado())

        bandera_decimal = False
        operador = None
        numero1 = None
        numero2 = None

    elif ingreso == ".":
        if not bandera_decimal:
            bandera_decimal = True
            pantalla.insert(tkinter.END, ingreso)
        else:
            messagebox.showerror("Error", "Ingreso invalido")

    else:
        pantalla.insert(tkinter.END, ingreso)


# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("")

# Configuración pantalla de salida 
pantalla = Entry(root, width=19, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1.5, pady=1)

# Configuración botones
boton_1 = Button(root, command=lambda: ingreso(1), text="1", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, command=lambda: ingreso(2), text="2", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, command=lambda: ingreso(3), text="3", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, command=lambda: ingreso(4), text="4", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, command=lambda: ingreso(5), text="5", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, command=lambda: ingreso(6), text="6", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, command=lambda: ingreso(7), text="7", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, command=lambda: ingreso(8), text="8", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, command=lambda: ingreso(9), text="9", width=9, height=3, bg="white", fg="red", borderwidth=0,
                 cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, command=lambda: ingreso("="), text="=", width=20, height=3, bg="red", fg="white",
                     borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, command=lambda: ingreso("."), text=".", width=9, height=3, bg="spring green", fg="black",
                     cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, command=lambda: ingreso("+"), text="+", width=9, height=3, bg="deep sky blue", fg="black",
                   borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, command=lambda: ingreso("-"), text="-", width=9, height=3, bg="deep sky blue", fg="black",
                     borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, command=lambda: ingreso("*"), text="*", width=9, height=3, bg="deep sky blue",
                              fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, command=lambda: ingreso("/"), text="/", width=9, height=3, bg="deep sky blue", fg="black",
                        borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
