from tkinter import filedialog

class ChooseFile:

    def __init__(self):
        print('iniciando..')

    #permite obteber una ruta especifica de un archivo
    def import_choose_file(self):
        try:
            path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])

            return path
        except:
            print("Ocurrio una error al buscar el file")