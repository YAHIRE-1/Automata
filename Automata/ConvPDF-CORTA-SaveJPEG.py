import os
from PyPDF2 import PdfWriter, PdfFileReader #Esta libreria importa metodos para leer PDF
from pdf2image import convert_from_path     #Esta libreria importa metodos para convertir PDF a JPG  
from icecream import ic #Esta libreria hace que se vea ordenado al entregar datos
from math import ceil, trunc #Esta libreria ayuda a dividir y cortar las paginas de los pdf
from tkinter import Tk # Esta libreria ayuda con los cuadros de texto
from tkinter.filedialog import askopenfilename, asksaveasfilename #Esta libreria ayuda a seleccionar el archivo PDF

#Esta linea es la ruta para los archivos que convierten PDF
poppler_path= r"Agrega tu ruta a la carpeta poppler"

#Esta linea es la funcion que selecciona el archivo pdf a convertir
pdf_path = askopenfilename(title="Selecciona el archivo PDF de entrada", filetypes=[("Archivos PDF", "*.pdf")])

#Esta linea convierte el archivo pdf a jpg
pages= convert_from_path(pdf_path= pdf_path, poppler_path=poppler_path)

#Esta linea selecciona donde se van a guardar las imagenes
saving_folder= r"ruta a la carpeta de destino"

#Aqui se cortan y guargan las paginas 
c=1

for page in pages:
    img_name= f"img-{c}.jpeg"
    page.save(os.path.join(saving_folder,img_name),"JPEG")
    c+=1

ic ("Conversión completa")
