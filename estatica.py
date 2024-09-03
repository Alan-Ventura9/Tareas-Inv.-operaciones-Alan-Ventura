import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

calificaciones = []

for i in range(5):
    calificacion = int(simpledialog.askstring("Input", "Captura la calificación:"))
    calificaciones.append(calificacion)

print("Las calificaciones capturadas son:", calificaciones)