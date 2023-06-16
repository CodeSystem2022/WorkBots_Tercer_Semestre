#Declaramos una variable
try:
    archivo = open("prueba.txt",'w', encoding = 'utf8') #la w es de Write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son: \nr: read(lee), \na: append(abre y agrega), \nw: write(escribe), \nx:crea archivo ademas regresa un error si no existe\n')
    archivo.write('t: esta es para texto o text, \nb: para archivos binarios, \nw+: escribe y lee, \nr+: lee y escribe (al reves de w+)\n')
    archivo.write('Saludos a los pibes de la wachitura\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #Siempre se ejecuta esto
    archivo.close() #Con esto se debe cerrar el archivo
# archivo.write('Todo quedo joie') ---> este es un error. ya se cerro el archivo


