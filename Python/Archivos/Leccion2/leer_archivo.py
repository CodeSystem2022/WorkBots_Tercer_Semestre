
archivo = open('prueba.txt','r', encoding = 'utf8') # las letras son: r: read, a: append(abre y agrega), w: write, x:crea archivo ademas regresa un error si no existe
#archivo = open('c:\\users\\nicof\Tecnicatura3Py\Archivos\Leccion02\prueba.txt') <- esto se usa cuando el archivo no esta en la misma carpeta que el py
#print(archivo.read())
#print(archivo.read(16)) # lee solo la cantidad de letras especificadas
#print(archivo.read(10)) #lee las siguitenes letras
# Continuamos desde la linea anterior
#print(archivo.readline()) #lee una linea completa
#print(archivo.readline())#lee la siguiente linea

#vamos a iterar el archivo, cada una de las lineas
#for linea in archivo:
    #print(linea) # iteramos los elementos del archivo
    #print(archivo.readlines()) # accedemos al archivo como si fuera una lista

#print(archivo.readlines()[0])# accedemos al archivo como si fuera lista y con el num entre corchete la linea que queremos ver

#creamos un nuevo archivo y anexamos la info del otro archivo
archivo2 = open('copia.txt','a',encoding='utf8')
archivo2.write(archivo.read())
archivo.close()# cerramos el primero
archivo2.close()#cerramos el segundo

print(f'se ha terminado el proceso de copiar ')
