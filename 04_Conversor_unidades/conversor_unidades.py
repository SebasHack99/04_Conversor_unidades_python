# Importaciones necesarias para crear nuestra aplicación
import tkinter as tk  # Tkinter es como el juguete que usamos para construir la ventana y los botones.
from tkinter import ttk, messagebox  # ttk nos da botones más bonitos. messagebox nos deja mostrar mensajes como "¡Ups!" si hay un error.

# Función mágica que hace las conversiones
def convertir():
    """
    Aquí es donde ocurre la magia de convertir cosas.
    Tomamos un número, lo transformamos según lo que elijas, y te mostramos el resultado.
    """
    try:
        # Leemos el número que escribiste en la cajita de texto
        valor = float(entry_valor.get())  # Convertimos lo que escribiste en un número (porque necesitamos números para sumar y multiplicar).

        # Vemos qué conversión elegiste en el menú desplegable
        unidad = combo_tipo_conversion.get()  # Esto es como preguntarte: "¿Qué quieres convertir?"

        # Dependiendo de lo que elegiste, hacemos una operación diferente
        if unidad == "Celsius a Fahrenheit":  # Si quieres convertir grados Celsius a Fahrenheit...
            resultado = (valor * 9/5) + 32  # Aquí hacemos la cuenta mágica.
            etiqueta_resultado.config(text=f"{resultado:.2f} °F")  # Mostramos el resultado.
        elif unidad == "Metros a Pies":  # Si quieres convertir metros a pies...
            resultado = valor * 3.28084  # Otra cuenta mágica.
            etiqueta_resultado.config(text=f"{resultado:.2f} ft")  # Mostramos el resultado.
        elif unidad == "Kilogramos a Libras":  # Si quieres convertir kilos a libras...
            resultado = valor * 2.20462  # Otra operación mágica.
            etiqueta_resultado.config(text=f"{resultado:.2f} lb")  # Mostramos el resultado.
        else:
            # Si no elegiste nada, te decimos que elijas algo
            etiqueta_resultado.config(text="Por favor, selecciona una conversión")
    except ValueError:
        # Si escribiste algo que no es un número, te mostramos un mensaje de error
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

# Configuramos la ventana donde jugarás con las conversiones
ventana = tk.Tk()  # Esta es nuestra ventanita.
ventana.title("Conversor de Unidades")  # Le damos un título a la ventana.
ventana.geometry("400x300")  # Le decimos qué tan grande será.
ventana.resizable(False, False)  # No dejamos que cambies el tamaño de la ventana.

# Un título grande y bonito para nuestra aplicación
etiqueta_titulo = tk.Label(ventana, text="Conversor de Unidades", font=("Arial", 16))
etiqueta_titulo.pack(pady=10)  # Lo colocamos con un espacio arriba y abajo.

# Un lugar para escribir el número que quieres convertir
frame_valor = tk.Frame(ventana)  # Hacemos un espacio para los elementos relacionados al valor.
frame_valor.pack(pady=10)  # Le ponemos espacio arriba y abajo.

# Una etiqueta que dice "Escribe tu número aquí"
tk.Label(frame_valor, text="Escribe el número: ", font=("Arial", 12)).grid(row=0, column=0, padx=5)

# Una cajita donde escribes el número
entry_valor = tk.Entry(frame_valor, font=("Arial", 12), width=10)
entry_valor.grid(row=0, column=1, padx=5)  # La ponemos al lado de la etiqueta.

# Un menú para elegir qué tipo de conversión quieres hacer
frame_conversion = tk.Frame(ventana)  # Otro espacio para organizar cosas.
frame_conversion.pack(pady=10)

# Una etiqueta que dice "Elige qué convertir"
tk.Label(frame_conversion, text="Elige la conversión: ", font=("Arial", 12)).grid(row=0, column=0, padx=5)

# El menú donde eliges qué convertir
combo_tipo_conversion = ttk.Combobox(frame_conversion, font=("Arial", 12), width=20)
combo_tipo_conversion["values"] = ["Celsius a Fahrenheit", "Metros a Pies", "Kilogramos a Libras"]  # Opciones para elegir.
combo_tipo_conversion.grid(row=0, column=1, padx=5)  # Lo ponemos al lado de la etiqueta.

# Un botón para que inicies la conversión
boton_convertir = tk.Button(ventana, text="Convertir", font=("Arial", 12), command=convertir)
boton_convertir.pack(pady=10)  # Lo colocamos con espacio alrededor.

# Un lugar donde aparecerá el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 14), fg="blue")
etiqueta_resultado.pack(pady=10)  # Le damos espacio arriba y abajo.

# Esto hace que la ventana se quede abierta hasta que la cierres
ventana.mainloop()
