from mysql.connector import connect
from mysql.connector import Error as err
from mysql.connector import errorcode

try:
    # Creamos la conexion
    con = connect(username='username', password='password',
                  host='localhost', database='name_database')
    cur = con.cursor()
    eliminar_cliente = ("DELETE FROM cliente WHERE id=%s")
    id_del_cliente = [14]
    # Insertar nuevos clientes
    cur.execute(eliminar_cliente, id_del_cliente)
    emp_no = cur.lastrowid
    # Apruebas de que el dato sea seguro a la base de datos.
    con.commit()

except err:
    if err == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error ala conexion verifica tus datos!")
    elif err == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe!")
    else:
        print(err)
else:
    # Cierras el cursor y la conexion.
    cur.close()
    con.close()