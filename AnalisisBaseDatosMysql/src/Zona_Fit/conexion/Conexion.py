from mysql.connector import connect
from mysql.connector import Error as err
from mysql.connector import errorcode

try:
    # Creamos la conexion.
    con = connect(username='username', password='password',
                  host='localhost', database='name_database')
except err:
    if err == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error ala conexion verifica tus datos!")
    elif err == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe!")
    else:
        print(err)
else:
    # Cerramos la conexion
    con.close()