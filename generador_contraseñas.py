import tkinter as tk
import random
import string

def generar_pass():
    pass_longitud = int(longitud.get())
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(pass_longitud))
    resultado_pass.delete(0, tk.END)
    resultado_pass.insert(0, password)

def index():
    global longitud  # Declarar la variable longitud como global
    global resultado_pass
    principal = tk.Tk()
    principal.title("PASSWORD GENERATOR By Juancarlos Fernandez")
    principal.geometry("700x150")

    tk.Label(principal, text="Indica la longitud de caracteres para tu contraseña:").grid(row=0, columnspan=2, padx=20, pady=10)
    longitud = tk.Entry(principal)
    longitud.grid(row=0, column=2, padx=10)

    tk.Label(principal, text="Tu contraseña generada es:").grid(row=1, columnspan=2, padx=20, pady=10)
    resultado_pass = tk.Entry(principal,width=40)
    resultado_pass.grid(row=1, column=2, padx=10)

    boton1 = tk.Button(principal, text="Generar", command=generar_pass)
    boton1.grid(row=2, columnspan=3, pady=10)

    principal.mainloop()

index()






