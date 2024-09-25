# use as following
# python initdb.py

import sqlite3
#opening connection to database which will be created
connection = sqlite3.connect('./databases/database.db')

#opening schema.sql
with open('./schemas/schemas.sql') as f:

#Next you execute its contents using the executescript() method
#that executes multiple SQL statements at once, which will create the posts table
    connection.executescript(f.read())

#Create a Cursor object that allows you to process rows in a database.
#In this case, you’ll use the cursor’s execute() method to execute two 
# INSERT SQL statements to add two blog posts to your posts table
cur = connection.cursor()

# Tabla formaciones se importan en DB Browser SQLite
# Tabla ocupaciones se importan en DB Browser SQLite
# Tabla municipios se importan en DB Browser SQLite
# Tabla provincias se importan en DB Browser SQLite


cur.execute("INSERT INTO carnets ( \
                carnets_descripcion_carnet, \
                carnets_texto_libre \
            ) \
            VALUES \
                ('AM', 'texto prueba2'), \
                ('A1', 'texto prueba'), \
                ('A2', 'texto prueba'), \
                ('B1', 'texto prueba'), \
                ('B', 'texto prueba'), \
                ('C1', 'texto prueba'), \
                ('C', 'texto prueba'), \
                ('D1', 'texto prueba'), \
                ('D', 'texto prueba'), \
                ('BE', 'texto prueba'), \
                ('B1C', 'texto prueba'), \
                ('CE', 'texto prueba'), \
                ('D1E', 'texto prueba'), \
                ('DE', 'texto prueba') \
            ")

cur.execute("INSERT INTO `contratos` (\
                `contratos_descripcion_contrato`, \
                `contratos_descripcion_contrato_texto_libre` \
            ) \
            VALUES \
                ('Temporal', 'texto libre'), \
                ('Indefinido', 'texto libre') \
            ")

cur.execute("INSERT INTO `empresas` (\
                `empresas_cif`, \
                `empresas_nombre`, \
                `empresas_correo_electronico`, \
                `empresas_persona_contacto`, \
                `empresas_telefono` \
            ) \
            VALUES \
                ('B20861340', 'UECC', 'uecc@uecc.com', 'pepe viyuela', '943523550'), \
                ('A14151340', 'ACENOR', 'contacto@acenor.com', 'An Txon Urrusolo', '943143530') \
            ")

cur.execute("INSERT INTO `estados_ofertas` (\
                `estados_ofertas_descripcion_estado_oferta`, \
                `estados_ofertas_descripcion_estado_oferta_texto_libre` \
            ) \
            VALUES \
                ('Abierta', 'texto libre'), \
                ('Proceso selección', 'texto libre'), \
                ('Cerrada SIN contrato', 'texto libre'), \
                ('Cerrada CON contrato', 'texto libre') \
            ")

cur.execute("INSERT INTO `estados_trabajadores` (\
                `estados_trabajadores_descripcion_estado_trabajador`, \
                `estados_trabajadores_descripcion_estado_trabajador_texto_libre` \
            ) \
            VALUES \
                ('Apto', 'texto libre'), \
                ('No apto', 'texto libre'), \
                ('Contratado', 'texto libre') \
            ")

cur.execute("INSERT INTO `idiomas` (\
                `idiomas_descripcion_idioma`, \
                `idiomas_descripcion_idioma_texto_libre` \
            ) \
            VALUES \
                ('Inglés', 'texto libre'), \
                ('Francés', 'texto libre'), \
                ('Alemán', 'texto libre'), \
                ('Italiano', 'texto libre') \
            ")

cur.execute("INSERT INTO `jornadas` (\
                `jornadas_descipcion_jornada`, \
                `jornadas_descipcion_jornada_texto_libre` \
            ) \
            VALUES \
                ('Completa', 'texto libre'), \
                ('Parcial', 'texto libre') \
            ")


cur.execute("INSERT INTO `nivel_idiomas` (\
                `nivel_idiomas_descripcion_nivel_idioma`, \
                `nivel_idiomas_descripcion_nivel_idioma_texto_libre` \
            ) \
            VALUES \
                ('Alto', 'texto libre'), \
                ('Medio', 'texto libre'), \
                ('Bajo', 'texto libre') \
            ")

cur.execute("INSERT INTO `provincias` (\
                `provincias_descripcion_provincia`, \
                `provincias_descripcion_provincia_texto_libre` \
            ) \
            VALUES \
                ('ALAVA', 'texto libre'), \
                ('GUIPUZCOA', 'texto libre'), \
                ('LA RIOJA', 'texto libre'), \
                ('NAVARRA', 'texto libre'), \
                ('VIZCAYA', 'texto libre') \
            ")
cur.execute("INSERT INTO `vehiculos` (\
                `vehiculos_descripcion_vehiculo`, \
                `vehiculos_descripcion_vehiculo_texto_libre` \
            ) \
            VALUES \
                ('Ninguno', 'texto libre'), \
                ('Coche', 'texto libre'), \
                ('Moto', 'texto libre'), \
                ('Furgoneta', 'texto libre'), \
                ('Camión', 'texto libre') \
            ")

cur.execute("INSERT INTO `trabajadores_situaciones` (\
                `trabajadores_situaciones_descripcion_situacion`, \
                `trabajadores_situaciones_descripcion_situacion_texto_libre` \
            ) \
            VALUES \
                ('Libre', 'texto libre'), \
                ('Ocupado', 'texto libre') \
            ")

cur.execute("INSERT INTO `trabajadores` (\
                `trabajadores_nombre`, \
                `trabajadores_apellidos`, \
                `trabajadores_fecha_nacimiento`, \
                `trabajadores_doi`, \
                `trabajadores_id_municipio`, \
                `trabajadores_codigo_postal`, \
                `trabajadores_id_provincia`, \
                `trabajadores_id_vehiculo`, \
                `trabajadores_curriculum`, \
                `trabajadores_telefono_contacto`, \
                `trabajadores_correo_electronico`, \
                `trabajadores_id_situacion`, \
                `trabajadores_lopd` \
            ) \
            VALUES \
                ('Pepe', 'Viyuela Altamonte', '1972-10-10', '15150150D', 1, '20020', 1, 1, '', '680680680', 'pepe@pepe.com', 1, '1'), \
                ('Ana', 'Diosdado Lopez', '1992-10-10', '12345678H', 2, '20100', 2, 2, '', '688441442', 'adiosdado@text.com', 1, '1') \
            ")


#Commit the changes and close the connection
connection.commit()
connection.close()