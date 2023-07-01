import psycopg2


conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'Ticketera'
)
try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO productos (descripcion, precio) VALUES (%s, %s) ' # Placeholder
            valores = (input("Ingreso de producto nuevo\nIngrese nombre de producto: "), input('Ingrese precio del producto: ')) #es una tupla
            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
            # conexion.commit() # esto no lo vamos a usar, se utiliza para guardar los cambios en la base de datos
            registros_insertados = cursor.rowcount # Recupera todos los registros de la sentencia, que seran una lista
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()