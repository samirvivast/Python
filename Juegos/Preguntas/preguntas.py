#Juego de preguntas creado por Samir Vivas | 13-01-2026 | Contacto:  bryansamir@gmail.com
import tkinter as tk
from tkinter import PhotoImage, messagebox

# ------ AQUI VAN LAS IMAGENES Y PREGUNTAS DEL JUEGO -------- #
preguntas = [
    {"imagen": "imagenes/imagen1.png", "texto": "¿El sol es una estrella?"},
    {"imagen": "imagenes/imagen3.png", "texto": "¿Python es un lenguaje de programacion?"},
    {"imagen": "imagenes/imagen2.png", "texto": "¿La tierra es plana?"},
    {"imagen": "imagenes/imagen3.png", "texto": "¿El agua hierve a 50° grados?"},
    {"imagen": "imagenes/imagen3.png", "texto": "¿El numero 2 es par?"}
]

# ----------------- CLASE DEL JUEGO ----------------- #
class JuegoPreguntas:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Preguntas")
        self.root.geometry("600x600")
        self.root.config(bg="#f4f4f4")

        self.indice = 0

        # Imagen
        self.label_imagen = tk.Label(root, bg="#f4f4f4")
        self.label_imagen.pack(pady=20)


        # Titulo
        self.label_nombre = tk.Label(root, text="Pregunta:", font=("Arial", 20, "bold"), bg="#f4f4f4", wraplength=400)
        self.label_nombre.pack(pady=10)

        # Pregunta
        self.label_pregunta = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#f4f4f4", wraplength=400)
        self.label_pregunta.pack(pady=10)

        # Botones
        frame_botones = tk.Frame(root, bg="#f4f4f4")
        frame_botones.pack(pady=20)

        self.btn_si = tk.Button(frame_botones, text="Sí", width=10, bg="green", fg="white", font=("Arial", 12, "bold"),
                                command=lambda: self.responder("si"))
        self.btn_si.grid(row=0, column=0, padx=20)

        self.btn_no = tk.Button(frame_botones, text="No", width=10, bg="red", fg="white", font=("Arial", 12, "bold"),
                                command=lambda: self.responder("no"))
        self.btn_no.grid(row=0, column=1, padx=20)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.indice < len(preguntas):
            pregunta = preguntas[self.indice]

            # Cargar imagen (usar imagenes .PNG)
            try:
                img = PhotoImage(file=pregunta["imagen"])
                self.label_imagen.config(image=img)
                self.label_imagen.image = img
            except:
                self.label_imagen.config(image="", text="(Sin imagen)", font=("Arial", 12), fg="gray")

            # Mostrar pregunta
            self.label_pregunta.config(text=pregunta["texto"])
        else:
            messagebox.showinfo("Juego terminado", "Gracias por responder todas las preguntas.")
            self.root.quit()

    def responder(self, respuesta):
        # ----------------- LÓGICA DE IF / ELSE ----------------- #
        if self.indice == 0:  # Pregunta 1: ¿El sol es una estrella?
            if respuesta == "si":
                messagebox.showinfo("","Respuesta Correcta")
            else:
                messagebox.showerror("","Respuesta Incorrecta")
        elif self.indice == 1:  # Pregunta 2: ¿Python es un lenguaje de programacion?
            if respuesta == "si":
                messagebox.showinfo("","Respuesta Correcta")
            else:
                messagebox.showerror("","Respuesta Incorrecta")
        elif self.indice == 2:  # Pregunta 3: ¿La tierra es plana?
            if respuesta == "si":
                messagebox.showerror("","Respuesta Incorrecta")
            else:
                messagebox.showinfo("","Respuesta Correcta")
        elif self.indice == 3:  # Pregunta 4: ¿El agua hierve a 50° grados?
            if respuesta == "si":
                messagebox.showerror("","Respuesta Incorrecta")
            else:
                messagebox.showinfo("","Respuesta Correcta")
        elif self.indice == 4:  # Pregunta 5: ¿El numero 2 es par?
            if respuesta == "si":
                messagebox.showinfo("","Respuesta Correcta")
            else:
                messagebox.showerror("","Respuesta Incorrecta")

        # Pasar a la siguiente pregunta
        self.indice += 1
        self.mostrar_pregunta()


# ----------------- INICIAR JUEGO ----------------- 
root = tk.Tk()
juego = JuegoPreguntas(root)
root.mainloop()
