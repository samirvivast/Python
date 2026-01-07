import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

#Funciones----------------
def calcular_cuota():
    try:
        prestamo = float(entry_prestamo.get())
        tasa = float(entry_tasa.get()) / 100 / 12  # Tasa mensual
        meses = int(entry_meses.get())

        if tasa == 0:  # Caso sin intereses
            cuota = prestamo / meses
        else:
            cuota = prestamo * (tasa * (1 + tasa) ** meses) / ((1 + tasa) ** meses - 1)

        label_resultado.config(
            text=f"Cuota mensual: ${cuota:,.2f}",
            fg="green",
            font=("Arial", 12, "bold")
        )

        global datos_credito
        datos_credito = (prestamo, tasa, meses, cuota)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")


def generar_amortizacion(prestamo, tasa, meses, cuota):
    tabla = []
    saldo = prestamo
    for mes in range(1, meses + 1):
        interes = saldo * tasa
        abono_capital = cuota - interes
        saldo -= abono_capital
        tabla.append((mes, cuota, interes, abono_capital, max(saldo, 0)))
    return tabla


def mostrar_resumen():
    try:
        prestamo, tasa, meses, cuota = datos_credito
    except:
        messagebox.showerror("Error", "Primero debes calcular la cuota.")
        return

    total_pagado = cuota * meses
    intereses_totales = total_pagado - prestamo
    tabla = generar_amortizacion(prestamo, tasa, meses, cuota)

    resumen_win = tk.Toplevel(root)
    resumen_win.title("Resumen del Crédito")
    resumen_win.geometry("720x520")

    tk.Label(resumen_win, text=f"Préstamo solicitado: ${prestamo:,.2f}", font=("Arial", 11, "bold")).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Meses: {meses}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Cuota mensual: ${cuota:,.2f}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Total pagado: ${total_pagado:,.2f}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
    tk.Label(resumen_win, text=f"Intereses totales: ${intereses_totales:,.2f}", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)

    cols = ("Mes", "Cuota", "Interés", "Abono Capital", "Saldo")
    tree = ttk.Treeview(resumen_win, columns=cols, show="headings", height=15)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    for fila in tabla:
        tree.insert("", "end", values=(
            fila[0],
            f"${fila[1]:,.2f}",
            f"${fila[2]:,.2f}",
            f"${fila[3]:,.2f}",
            f"${fila[4]:,.2f}"
        ))

# Botones de exportación
    btn_excel = tk.Button(resumen_win, text="📊 Exportar a Excel", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"),
                          command=lambda: exportar_excel(tabla))
    btn_excel.pack(side="left", padx=20, pady=10)

    btn_pdf = tk.Button(resumen_win, text="📄 Exportar a PDF", bg="#2196F3", fg="white", font=("Arial", 10, "bold"),
                        command=lambda: exportar_pdf(tabla))
    btn_pdf.pack(side="left", padx=20, pady=10)


#EXPORTACIÓN ----------------

def exportar_excel(tabla):
    archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])
    if not archivo:
        return

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Amortización"

    ws.append(["Mes", "Cuota", "Interés", "Abono Capital", "Saldo"])
    for fila in tabla:
        ws.append([fila[0], fila[1], fila[2], fila[3], fila[4]])

    wb.save(archivo)
    messagebox.showinfo("Éxito", f"Tabla exportada a Excel:\n{archivo}")


def exportar_pdf(tabla):
    archivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
    if not archivo:
        return

    c = canvas.Canvas(archivo, pagesize=letter)
    c.setFont("Helvetica", 10)
    c.drawString(200, 770, "Tabla de Amortización")

    columnas = ["Mes", "Cuota", "Interés", "Abono Capital", "Saldo"]
    x = 50
    y = 740
    for col in columnas:
        c.drawString(x, y, col)
        x += 100

    y -= 20
    for fila in tabla:
        x = 50
        for valor in fila:
            c.drawString(x, y, f"{valor:,.2f}" if isinstance(valor, float) else str(valor))
            x += 100
        y -= 20
        if y < 50:  # Crear nueva página si se llena
            c.showPage()
            c.setFont("Helvetica", 10)
            y = 750

    c.save()
    messagebox.showinfo("Éxito", f"Tabla exportada a PDF:\n{archivo}")


#INTERFAZ PRINCIPAL ----------------

root = tk.Tk()
root.title("Simulador de Crédito - Libre Inversión")
root.geometry("420x300")
root.config(bg="#f4f4f4")

frame = tk.Frame(root, bg="#f4f4f4", padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text="Valor del préstamo:", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
entry_prestamo = tk.Entry(frame, width=20)
entry_prestamo.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Tasa de interés anual (%):", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")
entry_tasa = tk.Entry(frame, width=20)
entry_tasa.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Número de meses:", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w")
entry_meses = tk.Entry(frame, width=20)
entry_meses.grid(row=2, column=1, pady=5)

btn_calcular = tk.Button(frame, text="Calcular cuota", command=calcular_cuota, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_calcular.grid(row=3, columnspan=2, pady=10)

btn_resumen = tk.Button(frame, text="Ver Resumen", command=mostrar_resumen, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_resumen.grid(row=4, columnspan=2, pady=10)




label_resultado = tk.Label(frame, text="", bg="#f4f4f4", font=("Arial", 10))
label_resultado.grid(row=5, columnspan=2, pady=10)


tk.Label(frame, text="Creado por Samir Vivas | 2025", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w")
tk.Label(frame, text="bryansamir@gmail.com", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=7, column=0, sticky="w")



root.mainloop()
