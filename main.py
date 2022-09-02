from tkinter import *
from tkinter import ttk, Tk, font, filedialog
import tkinter
from Analizador.gramatica import analizar_entrada
from Analizador.Singleton.Singleton import *

simbolos = []
errores = []
basesExistentes = []
basesDatos = []

def acercaDe():
    acerca_de = Toplevel()
    acerca_de.title("Acerca De")
    acerca_de.configure(background='#F4F4A6')
    info = """
    Datos del estudiante:
    ♥ Yeinny Melissa Catalán de León
    ♥ 202004725
    ♥ Organización de Lenguajes y Compiladores 2 Sección D
    ♥ Ingeniería en Ciencias y Sistemas
    ♥ 6to Semestre
    """
    prueba = Label(acerca_de, text=info, background='#F4F4A6', justify="left")
    prueba.place(x = 15, y= 10)
    acerca_de.geometry('600x200')
    acerca_de.resizable(width=False, height=False)
    acerca_de.mainloop()

def tablaSimbolos():
    tabla_simbolos = Toplevel()
    tabla_simbolos.title("Tabla de símbolos")
    tabla_simbolos.configure(background='#F4F4A6', padx=20, pady=20)
    tabla = ttk.Treeview(
    tabla_simbolos,
    columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6'),
    show='headings',
    selectmode='browse'
    )
    tabla.pack(fill='both')

    tabla.heading(0, text = 'ID')
    tabla.column(0, anchor='center', width=100)

    tabla.heading(1, text = 'Tipo Símbolo')
    tabla.column(1, anchor='center', width=100)

    tabla.heading(2, text = 'Tipo de Dato')
    tabla.column(2, anchor='center', width=100)

    tabla.heading(3, text = 'Ambito')
    tabla.column(3, anchor='center', width=100)

    tabla.heading(4, text = 'Fila')
    tabla.column(4, anchor='center', width=100)

    tabla.heading(5, text = 'Columna')
    tabla.column(5, anchor='center', width=100)

    insertarDatos(tabla, simbolos)
    tabla_simbolos.resizable(width=False, height=False)
    tabla_simbolos.mainloop()

def tablaErrores():
    tabla_errores = Toplevel()
    tabla_errores.title("Tabla de Errores")
    tabla_errores.configure(background='#F4F4A6', padx=20, pady=20)
    tabla = ttk.Treeview(
    tabla_errores,
    columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6'),
    show='headings',
    selectmode='browse'
    )
    tabla.pack(fill='both')

    tabla.heading(0, text = 'No.')
    tabla.column(0, anchor='center', width=100)

    tabla.heading(1, text = 'Descripción')
    tabla.column(1, anchor='center', width=100)

    tabla.heading(2, text = 'Ámbito')
    tabla.column(2, anchor='center', width=100)

    tabla.heading(3, text = 'Línea')
    tabla.column(3, anchor='center', width=100)

    tabla.heading(4, text = 'Columna')
    tabla.column(4, anchor='center', width=100)

    tabla.heading(5, text = 'Fecha y hora')
    tabla.column(5, anchor='center', width=100)

    insertarDatos(tabla, errores)
    tabla_errores.resizable(width=False, height=False)
    tabla_errores.mainloop()

def tablaBasesDatosExistentes():
    tabla_base = Toplevel()
    tabla_base.title("Tabla de bases de datos existentes")
    tabla_base.configure(background='#F4F4A6', padx=20, pady=20)
    tabla = ttk.Treeview(
    tabla_base,
    columns=('c1', 'c2', 'c3', 'c4'),
    show='headings',
    selectmode='browse'
    )
    tabla.pack(fill='both')

    tabla.heading(0, text = 'No.')
    tabla.column(0, anchor='center', width=100)

    tabla.heading(1, text = 'Nombre')
    tabla.column(1, anchor='center', width=100)

    tabla.heading(2, text = 'No. Tablas')
    tabla.column(2, anchor='center', width=100)

    tabla.heading(3, text = 'Línea')
    tabla.column(3, anchor='center', width=100)

    insertarDatos(tabla, basesExistentes)
    tabla_base.resizable(width=False, height=False)
    tabla_base.mainloop()

def tablaBasesDatos():
    tabla_base = Toplevel()
    tabla_base.title("Tabla de bases de datos")
    tabla_base.configure(background='#F4F4A6', padx=20, pady=20)
    tabla = ttk.Treeview(
    tabla_base,
    columns=('c1', 'c2', 'c3', 'c4'),
    show='headings',
    selectmode='browse'
    )
    tabla.pack(fill='both')

    tabla.heading(0, text = 'No.')
    tabla.column(0, anchor='center', width=100)

    tabla.heading(1, text = 'Nombre Tabla')
    tabla.column(1, anchor='center', width=100)

    tabla.heading(2, text = 'Nombre bases de datos')
    tabla.column(2, anchor='center', width=100)

    tabla.heading(3, text = 'Línea')
    tabla.column(3, anchor='center', width=100)

    insertarDatos(tabla, basesExistentes)
    tabla_base.resizable(width=False, height=False)
    tabla_base.mainloop()

def insertarDatos(tv, datos):
    for dato in datos: 
        tv.insert('', 'end', values=dato)

if __name__ == '__main__':
    entrada = """
    let mut x = 2+4; 
    let mut y : String = "true";
    let mut z : &str = "hola";
    z = "prueba";
    println!("{}", (-(5+3)*4)+3);
    """
    analizar_entrada(entrada)
    """#----------------------CREACION VENTANA----------------------
    ventana = Tk()
    ventana.title("DB-Rust")
    ventana.configure(background='#D2BBF6')
    ventana.defaultFont = font.nametofont("TkDefaultFont") 
    ventana.defaultFont.configure(family="Courier", 
                                size=11, 
                                weight=font.BOLD) 

    #-------------------------------MENU SUPERIOR--------------------------
    menubar = Menu(ventana)

    reportes = Menu(menubar)
    reportes.add_command(label="Reporte de tabla de símbolos", command=tablaSimbolos)
    reportes.add_command(label="Reporte de errores", command=tablaErrores)
    reportes.add_command(label="Reporte de base de datos existente", command= tablaBasesDatosExistentes)
    reportes.add_command(label="Reporte de tablas de base de datos", command=tablaBasesDatos)

    menubar.add_cascade(label="Editor de código")
    menubar.add_cascade(label="Reportes", menu=reportes)
    menubar.add_cascade(label="Acerca de", command=acercaDe)

    #------------------------------------EDITOR------------------------------
    scrollbar = Scrollbar(ventana)
    scrollbar.pack(side="right", fill="y")
    scrollbarx = Scrollbar(ventana, orient=HORIZONTAL)
    scrollbarx.pack(side="bottom", fill="x")
    editor = Text(ventana, height=32, width= 70, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    editor.place(x = 50, y = 50);
    botonEjecutar = Button(ventana, text='Ejecutar',bg="#F1F159")
    botonEjecutar.place(x=527, y=10)
    etiquetaEditor = Label(ventana, text="Editor", background="#D2BBF6")
    etiquetaEditor.place(x=50,y=10)
    consola = Text(ventana, height=32, width= 70, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    consola.place(x = 660, y = 50);
    consola.configure(state='disabled')
    etiquetaConsola = Label(ventana, text="Consola", background="#D2BBF6")
    etiquetaConsola.place(x=660,y=10)
    #-------------------CIERRE VENTANA-------------------------
    ventana.config(menu=menubar)
    ventana.geometry('1300x650')
    ventana.resizable(width=False, height=False)
    ventana.mainloop()"""