import pandas as pd
from tkinter import filedialog
from app.choose_file import ChooseFile
from tkinter import messagebox
class ImportExcel:
    choose = None
    data = None
    data_frame = None

    def __init__(self):
        self.choose = ChooseFile()
        #self.data = pd.read_excel(path, engine='openpyxl')
        #validate = self.validate_header
        #if validate:
        #    self.data_frame = self.group_data()
        ##else:
            #return validate
        #    pass
        #print(data.columns.ravel())

    #
    def iniciar(self):
        path = self.choose.import_choose_file()
        self.data = pd.read_excel(path, engine='openpyxl')

        validate = self.validate_header()
        if validate:
            self.data_frame = self.group_data()
            return validate
        else:
            return validate

    #Analisas las cabeceras del excel, verificando si falta alguna
    def validate_header(self):
        error_file = []
        validate = True

        try:
            header = self.data.columns.ravel()

            if not 'departamento' in header and not 'DEPARTAMENTO' in header:
                error_file.append({
                    "error": "No se encontro la columna departamento"
                })
                validate = False

            if not 'municipio' in header and not 'MUNICIPIO' in header:
                error_file.append({
                    "error": "No se encontro la columna municipio"
                })
                validate = False

            if not 'zona' in header and not 'ZONA' in header:
                error_file.append({
                    "error": "No se encontro la columna zona"
                })
                validate = False

            if not 'codigo_puesto' in header and not 'CODIGO_PUESTO' in header:
                error_file.append({
                    "error": "No se encontro la columna codigo_puesto"
                })
                validate = False

            if not 'nombre_puesto' in header and not 'NOMBRE_PUESTO' in header:
                error_file.append({
                    "error": "No se encontro la columna nombre_puesto"
                })
                validate = False

            if not 'mesa' in header and not 'MESA' in header:
                error_file.append({
                    "error": "No se encontro la columna mesa"
                })
                validate = False

            if not 'partido' in header and not 'PARTIDO' in header:
                error_file.append({
                    "error": "No se encontro la columna partido"
                })
                validate = False

            if not 'candidato' in header and not 'CANDIDATO' in header:
                error_file.append({
                    "error": "No se encontro la columna candidato"
                })
                validate = False

            if not 'votos' in header and not 'VOTOS' in header:
                error_file.append({
                    "error": "No se encontro la columna votos"
                })
                validate = False

            if not 'latitud' in header and not 'LATITUD' in header:
                error_file.append({
                    "error": "No se encontro la columna latitud"
                })
                validate = False

            if not 'longitud' in header and not 'LONGITUD' in header:
                error_file.append({
                    "error": "No se encontro la columna longitud"
                })
                validate = False

            if validate:
                return True
            else:
                return error_file

        except Exception as e:
            print("Ocurrio un error al analizar las cabeceras info->", e)


    #agrupa los datos del excel
    def group_data(self):
        try:
            data_final = pd.DataFrame(self.data)
            df = data_final.groupby(['candidato', 'partido','codigo_puesto', 'municipio','departamento'])[['votos']].sum()
            print(df)
            return df
            #df.to_csv('prueba.csv')
            #df.to_excel('excelprueba.xlsx', sheet_name='Elecciones')
        except Exception as e:
            print("Ocurrio un error al agrupar los datos info->", e)

    #exportar a excel
    def export_to_excel(self):
        try:
            if self.data_frame is None:
                messagebox.showerror(message='Primero importe el documento', title='Error')
                return

            export_file = filedialog.asksaveasfilename(title='Save File', filetypes=[("XLSX", ".xlsx")])
            path = str(export_file) + '.xlsx'
            self.data_frame.to_excel(path, sheet_name='Elecciones')

            messagebox.showinfo(message='Datos exportador correctamente...', title='Success')

        except Exception as e:
            print("Ocurrio un error al agrupar los datos info->", e)
            messagebox.showerror(message='Ocurrio un error al exporta a xlsx', title='Error')
            return

    #export a csv
    def export_to_csv(self):
        try:
            if self.data_frame is None:
                messagebox.showerror(message='Primero importe el documento', title='Error')
                return

            export_file = filedialog.asksaveasfilename(title='Save File', filetypes=[("CSV", ".csv")])
            path = str(export_file) + ".csv"
            self.data_frame.to_csv(path)

            messagebox.showinfo(message='Datos exportador correctamente...', title='Success')

        except Exception as e:
            print("Ocurrio un error al exportar los datos info->", e)
            messagebox.showerror(message='Ocurrio un error al exporta a csv', title='Error')
            return