from tkinter import *
from tkinter import messagebox
import sqlite3
import webbrowser

# ---------------------- Funciones ----------------------
def conexionBBDD():
    miConexion=sqlite3.connect("usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))       
            ''')
        
        messagebox.showinfo("Conectar", "Conexión realizada con éxito")
    except:
        messagebox.showwarning("Alerta", "La Base de datos ya existe!")

def salirAplicacion():  #Funcion
    valor=messagebox.askquestion("Salir", "Desea Salir de la Aplicacion?")
    if valor == "yes":
        root.destroy()

def LimpiarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    textoComentario.delete(1.0, END)



def borrar_campos():
    cuadroID.delete(0, END)
    cuadroNombre.delete(0, END)
    cuadroPass.delete(0, END)
    cuadroApellido.delete(0, END)
    cuadroDireccion.delete(0, END)
    textoComentario.delete("1.0", END)

def crear():
    miConexion=sqlite3.connect("usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+ miNombre.get() +
        "','"+ miPass.get() +
        "','"+ miApellido.get() +
        "','"+ miDireccion.get() + 
        "','"+ textoComentario.get("1.0", END) +  "')")
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Insertado con Exito!")

def leer():
    miConexion=sqlite3.connect("usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0, usuario[5])

    miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+miNombre.get() +
        "', PASSWORD='"+ miPass.get() +
        "', APELLIDO='"+ miApellido.get() +
        "', DIRECCION='"+ miDireccion.get() + 
        "', COMENTARIOS='"+ textoComentario.get("1.0", END) + 
        "' WHERE ID=" + miId.get())
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Actualizado con Exito!")

def eliminar():
    miConexion=sqlite3.connect("usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+miId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Borrado con Exito!")

def licencia():
    messagebox.showinfo("Licencia", "Producto con fines educativos")

def acerca_de():
    messagebox.showinfo("Acerca de", "Creado por Samir Vivas | contacto: bryansamir@gmail.com ")

def donaciones():
    webbrowser.open("https://sites.google.com/view/samirvivast/donaciones")



# ---------------------- Ventana principal ----------------------
root = Tk()
root.title("Aplicación CRUD con Tkinter")
root.geometry("400x400")
root.config(width=400, height=400)

# ---------------------- Menú ----------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=400, height=400)

# Menú BBDD
bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)

# Menú Borrar
borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrar_campos)
borrarMenu.add_command(label="Limpiar campos", command=LimpiarCampos)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)



# Menú CRUD
crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

# Menú Ayuda
ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Donaciones", command=donaciones)
ayudaMenu.add_command(label="Licencia", command=licencia)
ayudaMenu.add_command(label="Acerca de…", command=acerca_de)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# ---------------------- Comienzo de campos ----------------------
miFrame = Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

# Campo ID
cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

# Campo Nombre
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

# Campo Password
cuadroPass = Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

# Campo Apellido
cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

# Campo Dirección
cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

# Campo Comentarios
textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)

# Scrollbar para comentarios
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# ---------------------- Aqui comienza los Label ----------------------
idLabel=Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Contraseña: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario: ")
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# ---------------------- Aqui van los Botones ----------------------
miFrame2 = Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


# ---------------------- Loop principal ----------------------
root.mainloop()
