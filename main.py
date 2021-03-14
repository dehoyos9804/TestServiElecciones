
#import
import tkinter as tk
from tkinter import filedialog
from app.choose_file import ChooseFile
from app.import_excel import ImportExcel

#instancia de la clase chooseFile
i = ImportExcel()


#inicio del formulario
app = tk.Tk()
app.title('Análisis elecciones')

#centrar ventana
x_windows = app.winfo_screenwidth() // 2 - 300 // 2
y_windows = app.winfo_screenheight()//2 - 300 // 2

position = str(300) + "x" + str(300) + "+" + str(x_windows) + "+" + str(y_windows)
app.geometry(position)
app.resizable(0, 0)

canvas = tk.Canvas(app, width=300, height=300, bg='lightsteelblue')

#creación de componentes
label = tk.Label(text='Análsis de los resultados\n de las elecciones en el país\n por mesas de votación', bg='lightsteelblue', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 100, window=label)

btnimport = tk.Button(text='Importa excel a analizar', command=i.iniciar, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 150, window=btnimport)

btnExportCsv = tk.Button(text='Exportar a CSV', command=i.export_to_csv, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150,200, window=btnExportCsv)

btnExportExcel = tk.Button(text='Exportar a XLSX', command=i.export_to_excel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150,250, window=btnExportExcel)
#fin componentes

canvas.pack()

app.mainloop()
