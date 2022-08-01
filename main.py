from tkinter import *
from tkinter import ttk, Tk, font, filedialog
import tkinter

if __name__ == '__main__':
    #----------------------CREACION VENTANA----------------------
    ventana = Tk()
    ventana.title("DB-Rust")
    ventana.configure(background='#D2BBF6')
    ventana.defaultFont = font.nametofont("TkDefaultFont") 
    ventana.defaultFont.configure(family="Courier", 
                                size=11, 
                                weight=font.BOLD) 
    #--------------------CREACION DE PESTAÑAS--------------------
    notebook = ttk.Notebook(ventana)
    notebook.pack(fill='both', expand= 'yes')
    #-----------------------PESTAÑA CARGAR------------------------
    pesEditor = tkinter.Frame(notebook, background="#D2BBF6")
    scrollbar = Scrollbar(pesEditor)
    scrollbar.pack(side="right", fill="y")
    scrollbarx = Scrollbar(pesEditor, orient=HORIZONTAL)
    scrollbarx.pack(side="bottom", fill="x")
    editor = Text(pesEditor, height=32, width= 70, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    editor.place(x = 50, y = 50);
    consola = Text(pesEditor, height=32, width= 70, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarx.set)
    consola.place(x = 660, y = 50);
    consola.configure(state='disabled')
    notebook.add(pesEditor, text="Editor")
    #--------------------PESTAÑA REPORTES------------------------
    pesReportes = tkinter.Frame(notebook, background="#F6F6BB")
    notebook.add(pesReportes, text="Reportes")
    #-------------------PESTAÑA AYUDA-------------------------
    pesAcercaDe = tkinter.Frame(notebook, background="#F6BBEF")
    notebook.add(pesAcercaDe, text="Acerca De")
    #-------------------CIERRE VENTANA-------------------------
    ventana.geometry('1300x650')
    ventana.mainloop()