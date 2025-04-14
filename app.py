from flask import Flask, request, jsonify, flash, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import text
from flask_marshmallow import Marshmallow
import os, json 
import jwt, time
import requests
from dotenv import load_dotenv
load_dotenv()

# To run server
# \CapstoneProject\Project1\flask-server> .\venv\Scripts\activate
# \CapstoneProject\Project1\flask-server> flask run --debug  

app = Flask(__name__)
# Allowing access to Flask server to following ips, second IP is example for more ip's list case
CORS(app, origins=["http://localhost:3000", "http://192.168.0.27",
                    "http://127.0.0.1:5502",
                    "http://portfolio-jrg.free.nf",
                    "https://client-react-capstone.onrender.com",
                    "https://jrodriguez.ikasle.ceinpro.es", "*"])

print("CLAVE: ", os.getenv("PRIVATE_KEY"))

db_file = './databases/database.db'
# base application directory, where to save our sql table, where to place our sqlite database 
basedir = os.path.abspath(os.path.dirname(__file__))
# Connection config between SQLAlchemy y SQLite3 DB API
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, db_file)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# TO DO
#   -  create a secret key which will help us - ALLOW USING¿? FLASH("MESSAGE"), OTHERS¿?

db = SQLAlchemy(app) # to iterate with database
ma = Marshmallow(app) # to add structure to the database


# Los tipos de datos más comunes son los datos de formulario o los datos JSON.
# Para enviar los datos del formulario, pasa un objeto FormData poblado. 
# Esto utiliza el mismo formato que un formulario HTML, y se accedería con request.form en una vista Flask.

@app.route('/get_weather_trend', methods=["POST", "GET"])
def get_weather_trend():
    # https://pyjwt.readthedocs.io/en/stable/
    # https://cosasdedevs.com/posts/usar-requests-python-api-rest/
    # https://docs.python.org/3/library/time.html#time.localtime
    # https://docs.python.org/3/library/time.html#time.gmtime


    PRIVATE_KEY = b"-----BEGIN RSA PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC/3MgyqKVeYzALWeGXatp/XK32yir+MKp38CGxy1Dwhs//f7OFDQICrPbnvhF8oFyaHIjszHbppesndWKFZjce98trmTGVrfmjcREfc4fYT0+hpz3HL9wxamRG/75H3k3pPKNgEi/mgDFAIIPhYpDda4UC9s50neF/xzzavA3ztack/fTfVY1dcXLwG3WksCgXLogpGRsqmfqI6n0Yj6StPvqejKYWxuBphE3SXaywHOHMTdr4ewUfE6W93FEozJnbu13oVcMFSyeVNPz8fdNRyf0zeY1bq0gH8Uq6vJ5V7eFqrR8jLqLMvjKgKJWL93CMAh0mnN84e43S3/c4X6irAgMBAAECggEAEf3AkiuJUkgHzdCwXFQLSC0nLQC5NlvW6GdOqY7wuJVTtNhDO8NEAH86qfGDT0X0WQk698WWkwNZgTo7Mloq6g7/dsgHQ8tsINzt556cSvbo9zYpD2AYDFQ3MgcyTyfz816ZzVz3O+yicap642wsPG8kKmp9YqcZabODq9k9j7A76nrAUYFmlgAIMWsvZivdakSJjLABzHRM2hvuqbSqmXRFLicqE5dpal08cjZJjQw5b+zFDyPAtLeV7BrfVxBKx46yRtrwPDrCkF5H1tccnqOagA9bXmda5njhlPrApnAftJ+F47RjxI7w2VL6cW6HZxuW23NohNh4JgLycqWDvQKBgQDqZ3XMhXyyCuGplk10KKfjL+FXOZXlyKcJtQ2csgWZ6XK2o3M+QE82z+GjM0BvPbqxLxRpUw5IXgNXuP2kryE6Ezpu/gL/ARci6DfepviUvMRCuMiiLhdJ16IBHTaeeTdl3Q4Z02KVX/k4SDMnEh1zXFN3gBpqEXlsuwJf9CZLHQKBgQDRifRDwBAhjzq8myCORMOS8QJs5Ain2zT5bvV79gLlSi/sUWWrSjCN+GsgHagsn9xpIsQ5JJbLxceRE/qV+8HVYsI3RUAe4hDeaK22arnGZIZg8+AzpkS6kQuSmnKfsLD6Xbo+JHvIEahycvWWSFK3Z+s3kkuOPWYwPHTzksowZwKBgQDpkh53pawTXXRvoC2dycVBRLyuRdtwFPkdWyQtN9cM/uonw8daCIrme07DaJaUQlZ9qAQWz4Qz6Do8d0GHkFrzm6VmZAZoQ5XiWrMRUh/xVgfa1HZX5MWf9xafNZTvZKom/pbGdTSO1AtqYcdW714ZTa5+LVAk0TTFe7NqGcbuoQKBgCSBnnb3TVgrdhZKCKAAxvog10VVbVShUldqx4YzVEnSZQsNG2N+Z3s0nqVXxWcQ6vu+POWfxE34RU63Zl8fH6QnsqKihAtdY4b8QdeYPImeFfNqSdN10l+WyadfFT1RMWRNVBdjj9VJjklyUes+6npdtpNV/6fmdplMzytolaVdAoGBAMg6br792JlZ6rFhvExsWcv7jPUoPVyDQymlq/EbgDkKJTeuKGuF5P7JOMXKcoo8N8nXQNA0YLGwLld1GzjFLgzpt7vtL7VpOWPE0L5V12JVJKj5hXuJwwdaxexTiiWSQ/rEN+ekG7g3YmxJY6qZLk9dndoFAfIoPHtzk5UcllJI\n-----END RSA PRIVATE KEY-----\n"
    today = time
    # substracts 86400 seconds = 1 day
    yesterday = today.time() - 86400
    iat = today.time()
    exp = iat + 3600 # adds 3600 seconds = 1 hour
    print(iat)
    print(exp)
    print(today.strftime("%Y/%m/%d"))

    oHeader = {
        "alg": 'RS256',
        "typ": 'JWT'
    }
    oPayload =  {
        "aud": "met01.apikey",
        "iss": "test jason",
        "exp": exp,
        "version": "1.0.0",
        "iat": iat,
        "email": "jason_rg1@hotmail.com"
    }
    # token1 = jwt.encode(oPayload, PRIVATE_KEY, algorithm="RS256", headers=oHeader)
    token1 = jwt.encode(oPayload, PRIVATE_KEY, algorithm="RS256", headers=oHeader)
    print (token1)
    # decoded = jwt.decode(token1, options={"verify_signature": False}) # works in PyJWT >= v2.0
    # print (decoded)
    # print (decoded["aud"])
    # return jsonify({ "meta": "ok", "data": "respuesta del servidor back-end", "key": "Top SECRET!!"})

    oHeader = {
        "alg": 'RS256',
        "typ": 'JWT'
    }
    oPayload =  {
        "aud": "met01.apikey",
        "iss": "test jason",
        "exp": exp,
        "version": "1.0.0",
        "iat": iat,
        "email": "jason_rg1@hotmail.com"
    }

    url =  'https://api.euskadi.eus/euskalmet/weather/regions/basque_country/forecast/trends/at/'+ \
            today.strftime("%Y/%m/%d")+'/for/'+today.strftime("%Y%m%d")
            # time.strftime("%Y/%m/%d", time.localtime(yesterday))+'/for/'+time.strftime("%Y%m%d", time.localtime(yesterday))
    print(url)

    headers = {
        'Authorization': 'Bearer '+token1
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
    print(response.json())
    print(response.status_code)
    print(response.headers)

    return response.json()

# Process to save offerresults for one offerResults(ofertas_resultados)
@app.route('/save_offerresults/<id>', methods=['POST','PUT'])
def save_offerresults(id):
    offerEditMode = eval(request.form.get('offerEditMode').capitalize())
    print("imprimo offerEditMode:", offerEditMode)
    # Storing results
    offerResults= request.form.get('offerResults')
    offerResultsToSave= json.loads(offerResults) # Converting to list
    # NEW offerResult
    # Saving data for offerResults created/edited
    if offerEditMode:
        # Updating workerState(trabajador_estado) in case it was changed
        # Retrieving current data for offer in offerResults(ofertas_resultados)
        currentResult = db.session.execute(text('SELECT * FROM ofertas_resultados \
                                                    WHERE ofertas_resultados_id_oferta = '+id+';'))
        db.session.close() # ONLY .CLOSE WITH .FETCHALL(), THE REST IS .COMMIT() !!!
        # response = [] 
        myResult = currentResult.fetchall()
        myResultFieldsName = currentResult.keys()
        #Convert data to dictionary
        currentResultData = []
        for record in myResult:
            currentResultData.append(dict(zip(myResultFieldsName, record)))
        # Loop to change workerState(trabajador_estado) in case
        for each in offerResultsToSave:
            for eachCurrent in currentResultData:
                if each['trabajadores_id_trabajador'] == eachCurrent['ofertas_resultados_id_trabajador']:
                    print ("ALREADY EXISTS")
                    # Updating workerState(trabajador_estado)
                    db.session.execute(text('UPDATE ofertas_resultados SET \
                                                ofertas_resultados_trabajador_estado = "'+each['trabajador_estado']+'" \
                                            WHERE ofertas_resultados_id_trabajador = '+str(each['trabajadores_id_trabajador'])+' \
                                                    AND ofertas_resultados_id_oferta = '+id+';'))
                    db.session.commit()
                    break
    else:      
        # Creating and saving new offerResults
        # LOOP FOR offerResultsToSave adding each one to results record
        for each in offerResultsToSave:
            print(each)
            parameters = ({
                "id_oferta": id,
                "trabajadores_id_trabajador" : each["trabajadores_id_trabajador"],
                "trabajador_estado" : each["trabajador_estado"],
                "contratado" : each["trabajador_contratado"]
            })
            result = db.session.execute(text(
                f'INSERT INTO ofertas_resultados (\
                        ofertas_resultados_id_oferta, \
                        ofertas_resultados_id_trabajador, \
                        ofertas_resultados_trabajador_estado, \
                        ofertas_resultados_contratado) \
                    VALUES (:id_oferta, :trabajadores_id_trabajador, :trabajador_estado, :contratado) \
                    ;'), parameters)
            db.session.commit()
    # ResultId edited/created
    response = []
    if offerEditMode:
        print("Results Record Edited id: "+id)
    else: 
        print("Results Record Created id: "+id)
    response.append ({
        "id": id
    })
    print ("api save_offerresults ended ...")
    return response

# Process to get offerresults from one offer(oferta) or all
# Process requery the criteria every time the offer is saved
# In offerEditMode = False (new offer created) the results are presented as per criteria fields values, giving the posibility to
# change the status for one worker inside the offer to Suitable - Unfit - Hire
# In offerEditMode = True (offer is edited) the results presented could add or not new workers depending on Criteria fields, the
# behaviour is to add new workers or not each time one offer is edited
@app.route('/generate_offerresults/<id>', methods=['POST','GET'])
@app.route('/generate_offerresults', methods=['POST','GET'])
def generate_offerresults(id = None):
    sqlCriteriaString = request.get_json()['criteria']
    offerEditMode = request.get_json()['offerEditMode']
    # Generating new results if new offer with criteria string, if editing offer may be additional results could appear
    result = db.session.execute(text('\
            SELECT trabajadores.trabajadores_id_trabajador, \
                    trabajadores.trabajadores_nombre, \
                    trabajadores.trabajadores_apellidos, \
                    trabajadores.trabajadores_telefono_contacto, \
                    trabajadores_ocupaciones.trabajadores_ocupaciones_id_ocupacion, \
                    trabajadores_ocupaciones.trabajadores_ocupaciones_meses, \
                    trabajadores_formaciones.trabajadores_formaciones_id_formacion, \
                    trabajadores.trabajadores_id_vehiculo, \
                    trabajadores.trabajadores_id_situacion, \
                    trabajadores.trabajadores_curriculum, \
                    "x" as "trabajador_estado", \
                    "no contratado" as "trabajador_contratado" \
                    FROM trabajadores  \
                        LEFT JOIN trabajadores_ocupaciones ON trabajadores.trabajadores_id_trabajador = trabajadores_ocupaciones.trabajadores_ocupaciones_id_trabajador \
                        LEFT JOIN trabajadores_formaciones ON trabajadores.trabajadores_id_trabajador = trabajadores_formaciones.trabajadores_formaciones_id_trabajador \
                        LEFT JOIN vehiculos ON trabajadores.trabajadores_id_vehiculo = vehiculos.vehiculos_id_vehiculo \
                    WHERE '+sqlCriteriaString+' GROUP BY trabajadores.trabajadores_doi;'))
    db.session.close() # ONLY .CLOSE WITH .FETCHALL(), THE REST IS .COMMIT() !!!
    response = [] 
    myResult = result.fetchall()
    print("imprimo myResult:", myResult)
    myResultFieldsName = result.keys()
    #Convert data to dictionary
    for record in myResult:
        response.append(dict(zip(myResultFieldsName, record)))
    if offerEditMode:
        # EDITING offerResults(ofertas_resultados), additional worker(trabajador) data could appears
        # Only new data will be added to offerResult (ofertas_resultados)
        # Retrieving current data for offer in offerResults(ofertas_resultados)
        currentResult = db.session.execute(text('SELECT * FROM ofertas_resultados \
                                                    WHERE ofertas_resultados_id_oferta = '+id+';'))
        db.session.close() # ONLY .CLOSE WITH .FETCHALL(), THE REST IS .COMMIT() !!!
        myResultEdit = currentResult.fetchall()
        myResultEditFieldsName = currentResult.keys()
        #Convert data to dictionary
        currentResultData = []
        for record in myResultEdit:
            currentResultData.append(dict(zip(myResultEditFieldsName, record)))
        # print("imprimo currentResultData:", currentResultData)
        
        #If editing one offer result without current data and there are new offer results, they have to be added
        # by another way
        if len(currentResultData) == 0:
            print("no currentData")
            #Loop to Insert result data to empty offerResult
            print("Inserting offerResult in empty offer")
            print("Imprimo result:", result)
            for data in response:
                parameters = ({
                    "id_oferta": id,
                    "trabajadores_id_trabajador" : data["trabajadores_id_trabajador"],
                    "trabajador_estado" : 'x',
                    "contratado" : 'no contratado'
                })
                db.session.execute(text(
                    f'INSERT INTO ofertas_resultados (\
                            ofertas_resultados_id_oferta, \
                            ofertas_resultados_id_trabajador, \
                            ofertas_resultados_trabajador_estado, \
                            ofertas_resultados_contratado) \
                        VALUES (:id_oferta, :trabajadores_id_trabajador, :trabajador_estado, :contratado) \
                        ;'), parameters)
                db.session.commit()
        else:
            # Loop to check if additional worker added in case, to be added to offerResult
            updates = False
            for each in response:
                #
                # Check if worker(trabajador) already in currentResultData
                #
                exist = False
                newElementToAdd = []
                for eachCurrent in currentResultData:
                    if each['trabajadores_id_trabajador'] == eachCurrent['ofertas_resultados_id_trabajador']:
                        print ("ALREADY EXISTS")
                        # print (eachCurrent)
                        exist = True
                        # Updating workerState(trabajador_estado), could be status is changed
                        # Update response status with current offerResult status
                        each['trabajador_estado'] = eachCurrent['ofertas_resultados_trabajador_estado']
                        db.session.execute(text('UPDATE ofertas_resultados SET \
                                                    ofertas_resultados_trabajador_estado = "'+each['trabajador_estado']+'" \
                                                WHERE ofertas_resultados_id_trabajador = '+str(each['trabajadores_id_trabajador'])+' \
                                                        AND ofertas_resultados_id_oferta = '+id+';'))
                        db.session.commit()
                        break
                    else:
                        print ("DOESNT EXIST: ", each['trabajadores_id_trabajador'])
                        newElementToAdd = each
                        updates = True
                        # print("imprimo each: ", each)
                        # print("imprimo newElementToAdd: ",newElementToAdd)
            # In case currentResultData is empty with no OfferResults and myResult have data (new Result editing offer with no results)
                
                if exist == False:
                    # Adding newElement in offerResults(ofertas_resultados) from offerResultsToSave
                    print("ELEMENTO A AÑADIR")
                    print(newElementToAdd)
                    parameters = ({
                        "id_oferta": id,
                        "trabajadores_id_trabajador" : newElementToAdd["trabajadores_id_trabajador"],
                        "trabajador_estado" : newElementToAdd["trabajador_estado"],
                        "contratado" : newElementToAdd["trabajador_contratado"]
                    })
                    result = db.session.execute(text(
                        f'INSERT INTO ofertas_resultados (\
                                ofertas_resultados_id_oferta, \
                                ofertas_resultados_id_trabajador, \
                                ofertas_resultados_trabajador_estado, \
                                ofertas_resultados_contratado) \
                            VALUES (:id_oferta, :trabajadores_id_trabajador, :trabajador_estado, :contratado) \
                            ;'), parameters)
                    db.session.commit()
                if updates:
                    #In case any newElement retrieving current offerResults(ofertas_resultado) Data,
                    # now updated and stored in response
                    result = db.session.execute(text('\
                            SELECT trabajadores.trabajadores_id_trabajador, \
                                    trabajadores.trabajadores_nombre, \
                                    trabajadores.trabajadores_apellidos, \
                                    trabajadores.trabajadores_telefono_contacto, \
                                    trabajadores_ocupaciones.trabajadores_ocupaciones_id_ocupacion, \
                                    trabajadores_ocupaciones.trabajadores_ocupaciones_meses, \
                                    trabajadores_formaciones.trabajadores_formaciones_id_formacion, \
                                    trabajadores.trabajadores_id_vehiculo, \
                                    trabajadores.trabajadores_id_situacion, \
                                    trabajadores.trabajadores_curriculum, \
                                    ofertas_resultados.ofertas_resultados_trabajador_estado as "trabajador_estado", \
                                    ofertas_resultados.ofertas_resultados_contratado as "trabajador_contratado" \
                                    FROM trabajadores  \
                                        LEFT JOIN trabajadores_ocupaciones ON trabajadores.trabajadores_id_trabajador = trabajadores_ocupaciones.trabajadores_ocupaciones_id_trabajador \
                                        LEFT JOIN trabajadores_formaciones ON trabajadores.trabajadores_id_trabajador = trabajadores_formaciones.trabajadores_formaciones_id_trabajador \
                                        LEFT JOIN vehiculos ON trabajadores.trabajadores_id_vehiculo = vehiculos.vehiculos_id_vehiculo \
                                        LEFT JOIN ofertas_resultados ON trabajadores.trabajadores_id_trabajador = ofertas_resultados.ofertas_resultados_id_trabajador \
                                    WHERE ofertas_resultados.ofertas_resultados_id_oferta = '+id+
                                    ' GROUP BY trabajadores.trabajadores_doi \
                                    ORDER BY ofertas_resultados.ofertas_resultados_id_resultado;'))
                    db.session.close() # ONLY .CLOSE WITH .FETCHALL(), THE REST IS .COMMIT() !!!
                    response = [] 
                    myResult = result.fetchall()
                    myResultFieldsName = result.keys()
                    #Convert data to dictionary
                    response = []
                    for record in myResult:
                        response.append(dict(zip(myResultFieldsName, record)))
                    
    print("imprimiendo generate_offerresults")
    print(response)
    print ("api generate_offerresults ended ...")
    return jsonify(response)

# Process to delete one offer(oferta)
@app.route('/deleteoffer/<id>', methods=['DELETE'])
def deleteoffer(id):
    # To allow ON CASCADE statements and delete Ocupations Workers automatically from Workers/Trabajadores
    db.session.execute(text(f'PRAGMA foreign_keys = ON;'))
    db.session.execute(text(f'DELETE FROM ofertas WHERE ofertas_id_oferta = '+id+';'))
    db.session.commit()
    response = []
    response.append ({
        "id deleted": id
    })
    print("Offer Record Deleted id: "+id)
    print ("api deleteoffer ended ...")
    return jsonify(response)

# Process to add offers(ofertas)
@app.route('/addoffer', methods=["POST", "PUT"]) 
def addoffer(): 
    # Populating Offers/Ofertas table
    parameters = ({
        "id_empresa" : request.form.get("id_empresa"),
        "id_ocupacion" : request.form.get("id_ocupacion"),
        "meses_experiencia" : request.form.get("meses_experiencia"),
        "id_formacion" : request.form.get("id_formacion"),
        "id_carnet_conducir" : "1",                 #request.form.get("ofertas_id_carnet_conducir"),
        "id_vehiculo" : request.form.get("id_vehiculo"), 
        "id_municipio" : request.form.get("id_municipio"),
        "id_provincia" : request.form.get("id_provincia"),
        "puesto_descripcion" : request.form.get("puesto_descripcion"),
        "id_contrato" : request.form.get("id_contrato"),
        "id_jornada" : request.form.get("id_jornada"),
        "salario" : request.form.get("salario"),
        "id_estado_oferta" : request.form.get("id_estado_oferta"),
        "fecha_creacion" : request.form.get("fecha_creacion"),
        "priorityField1" : request.form.get("priorityField1"), #.capitalize(),
        "priorityField2" : request.form.get("priorityField2"), #.capitalize(),
        "priorityField3" : request.form.get("priorityField3"), #.capitalize(),
        "priorityField4" : request.form.get("priorityField4"), #.capitalize(),
    })
    result = db.session.execute(text(
        f'INSERT INTO ofertas (\
                ofertas_id_empresa, \
                ofertas_id_ocupacion, \
                ofertas_meses_experiencia, \
                ofertas_id_formacion, \
                ofertas_id_carnet_conducir, \
                ofertas_id_vehiculo, \
                ofertas_id_municipio, \
                ofertas_id_provincia, \
                ofertas_puesto_descripcion, \
                ofertas_id_contrato, \
                ofertas_id_jornada, \
                ofertas_salario, \
                ofertas_id_estado_oferta, \
                ofertas_fecha_creacion, \
                ofertas_priorityField1, \
                ofertas_priorityField2, \
                ofertas_priorityField3, \
                ofertas_priorityField4) \
            VALUES (:id_empresa, :id_ocupacion, :meses_experiencia, :id_formacion, :id_carnet_conducir, :id_vehiculo, :id_municipio, :id_provincia, \
                :puesto_descripcion, :id_contrato, :id_jornada, :salario, :id_estado_oferta, :fecha_creacion, :priorityField1, \
                :priorityField2, :priorityField3, :priorityField4) \
            ;'), parameters)
    db.session.commit()
    # New offerId created
    newCreatedId = result.lastrowid
    response = []
    response.append ({
        "id": newCreatedId
    })
    print("Offers Record Created id: "+str(newCreatedId))
    print ("api addoffers ended ...")
    return response

# Process to edit one offer(oferta)
@app.route('/editoffer/<id>', methods=["POST", "GET"])
def editoffer(id):
    parameters = ({
        "id_empresa" : request.form.get("id_empresa"),
        "id_ocupacion" : request.form.get("id_ocupacion"),
        "meses_experiencia" : request.form.get("meses_experiencia"),
        "id_formacion" : request.form.get("id_formacion"),
        "id_vehiculo" : request.form.get("id_vehiculo"),
        "id_carnet_conducir" : "1",                 #request.form.get("ofertas_id_carnet_conducir"),
        "id_municipio" : request.form.get("id_municipio"),
        "id_provincia" : request.form.get("id_provincia"),
        "puesto_descripcion" : request.form.get("puesto_descripcion"),
        "id_contrato" : request.form.get("id_contrato"),
        "id_jornada" : request.form.get("id_jornada"),
        "salario" : request.form.get("salario"),
        "id_estado_oferta" : request.form.get("id_estado_oferta"),
        "priorityField1" : request.form.get("priorityField1"),
        "priorityField2" : request.form.get("priorityField2"),
        "priorityField3" : request.form.get("priorityField3"),
        "priorityField4" : request.form.get("priorityField4"),
    })
    db.session.execute(text('UPDATE ofertas SET \
                ofertas_id_empresa = :id_empresa, \
                ofertas_id_ocupacion = :id_ocupacion, \
                ofertas_meses_experiencia = :meses_experiencia, \
                ofertas_id_formacion = :id_formacion, \
                ofertas_id_vehiculo = :id_vehiculo, \
                ofertas_id_vehiculo = :id_carnet_conducir, \
                ofertas_id_municipio = :id_municipio, \
                ofertas_id_provincia = :id_provincia, \
                ofertas_puesto_descripcion = :puesto_descripcion, \
                ofertas_id_contrato = :id_contrato, \
                ofertas_id_jornada = :id_jornada, \
                ofertas_salario = :salario, \
                ofertas_id_estado_oferta = :id_estado_oferta, \
                ofertas_priorityField1 = :priorityField1, \
                ofertas_priorityField2 = :priorityField2, \
                ofertas_priorityField3 = :priorityField3, \
                ofertas_priorityField4 = :priorityField4 \
            WHERE ofertas_id_oferta = '+id+';'), parameters) 
    db.session.commit()
    response = []
    response.append ({
        "id": id
    })
    print("Offers Record Modificated id: "+id)
    print ("api editoffers ended ...")
    return jsonify(response)

# Process to get offer_secundary_databases data
@app.route('/get_offer_secundary_databases', methods=['POST','GET'])
def get_offer_secundary_databases():
    # Creating databases list with fields, to be studied in the future with loop interation
    listTables = [  "empresas",
                    "ocupaciones",
                    "formaciones",
                    "vehiculos",
                    "municipios",
                    "provincias",
                    "contratos",
                    "jornadas",
                    "estados_ofertas",
    ]
    # Creating executions for each table
    result2 = db.session.execute(text(f'SELECT * FROM '+listTables[1]+';'))
    result1 = db.session.execute(text(f'SELECT * FROM '+listTables[0]+';'))
    result3 = db.session.execute(text(f'SELECT * FROM '+listTables[2]+';'))
    result4 = db.session.execute(text(f'SELECT * FROM '+listTables[3]+';'))
    result5 = db.session.execute(text(f'SELECT * FROM '+listTables[4]+';'))
    result6 = db.session.execute(text(f'SELECT * FROM '+listTables[5]+';'))
    result7 = db.session.execute(text(f'SELECT * FROM '+listTables[6]+';'))
    result8 = db.session.execute(text(f'SELECT * FROM '+listTables[7]+';'))
    result9 = db.session.execute(text(f'SELECT * FROM '+listTables[8]+';'))
    db.session.close()
    # Getting data from each executions
    response = []
    # Enterprises/Empresas Data
    myResult = result1.fetchall()
    myResultFieldsName = result1.keys()
    #Converting data to dictionary
    response1 = []
    for record in myResult:
        response1.append(dict(zip(myResultFieldsName, record)))

    # Ocupations/Ocupaciones Data
    myResult = result2.fetchall()
    myResultFieldsName = result2.keys()
    #Converting data to dictionary
    response2 = []
    for record in myResult:
        response2.append(dict(zip(myResultFieldsName, record)))

    # Formations/Formaciones Data
    myResult = result3.fetchall()
    myResultFieldsName = result3.keys()
    #Converting data to dictionary
    response3 = []
    for record in myResult:
        response3.append(dict(zip(myResultFieldsName, record)))

    # Vehicles/Vehiculos Data
    myResult = result4.fetchall()
    myResultFieldsName = result4.keys()
    #Converting data to dictionary
    response4 = []
    for record in myResult:
        response4.append(dict(zip(myResultFieldsName, record)))

    # Municipalities/Municipios Data
    myResult = result5.fetchall()
    myResultFieldsName = result5.keys()
    #Converting data to dictionary
    response5 = []
    for record in myResult:
        response5.append(dict(zip(myResultFieldsName, record)))

    # Provinces/Provincias Data
    myResult = result6.fetchall()
    myResultFieldsName = result6.keys()
    #Converting data to dictionary
    response6 = []
    for record in myResult:
        response6.append(dict(zip(myResultFieldsName, record)))

    # Contracts/Contratos Data
    myResult = result7.fetchall()
    myResultFieldsName = result7.keys()
    #Converting data to dictionary
    response7 = []
    for record in myResult:
        response7.append(dict(zip(myResultFieldsName, record)))

    # Days/Jornadas Data
    myResult = result8.fetchall()
    myResultFieldsName = result8.keys()
    #Converting data to dictionary
    response8 = []
    for record in myResult:
        response8.append(dict(zip(myResultFieldsName, record)))

    # Offers States/Estados Ofertas Data
    myResult = result9.fetchall()
    myResultFieldsName = result9.keys()
    #Converting data to dictionary
    response9 = []
    for record in myResult:
        response9.append(dict(zip(myResultFieldsName, record)))

    response =  {
                    f'{listTables[0]}': response1,
                    f'{listTables[1]}': response2,
                    f'{listTables[2]}': response3,
                    f'{listTables[3]}': response4,
                    f'{listTables[4]}': response5,
                    f'{listTables[5]}': response6,
                    f'{listTables[6]}': response7,
                    f'{listTables[7]}': response8,
                    f'{listTables[8]}': response9,
                }
    print ("api offers_secundary_databases ended ...")
    return jsonify(response)

# Route to SELECT all data from Enterprises(empresas) database
# for all or one Enterprise
@app.route('/get_listoffers', methods=["POST", "GET"])
@app.route('/get_listoffers/<id>', methods=["POST", "GET"])
def get_listoffers(id = None):
    sqlString = 'SELECT * FROM ofertas \
                    JOIN empresas ON empresas.empresas_id_empresa = ofertas.ofertas_id_empresa \
                    JOIN ocupaciones ON ocupaciones.ocupaciones_id_ocupacion = ofertas.ofertas_id_ocupacion \
                    JOIN formaciones ON formaciones.formaciones_id_formacion = ofertas.ofertas_id_formacion \
                    JOIN vehiculos ON vehiculos.vehiculos_id_vehiculo = ofertas.ofertas_id_vehiculo \
                    JOIN municipios ON municipios.municipios_id_municipio = ofertas.ofertas_id_municipio \
                    JOIN provincias ON provincias.provincias_id_provincia = ofertas.ofertas_id_provincia \
                    JOIN contratos ON contratos.contratos_id_contrato = ofertas.ofertas_id_contrato \
                    JOIN jornadas ON jornadas.jornadas_id_jornada = ofertas.ofertas_id_jornada '
    if (id != None):
        result = db.session.execute(text(sqlString + ' WHERE ofertas_id_oferta = '+id+';'))
        # result = db.session.execute(text('SELECT * FROM ofertas WHERE ofertas_id_oferta = '+id+';'))
    else:
        result = db.session.execute(text(sqlString))
    db.session.close() # ONLY .CLOSE WITH .FETCHALL(), THE REST IS .COMMIT() !!!
    response = [] 
    if request.method == 'POST' or request.method == 'GET':
        myResult = result.fetchall()
        myResultFieldsName = result.keys()
        #Convert data to dictionary
        response = []
        for record in myResult:
            response.append(dict(zip(myResultFieldsName, record)))
    print ("api get_listoffers ended ...")
    return jsonify(response)

# Route to add one enterprise(empresa)
@app.route('/addenterprise', methods=["POST", "PUT"]) 
def addenterprise(): 
    # Populating Enterprises/Empresas table
    parameters = ({
    "cif": request.form.get("cif"),
    "nombre": request.form.get("nombre"),
    "correo_electronico": request.form.get("correo_electronico"),
    "persona_contacto": request.form.get("persona_contacto"),
    "telefono": request.form.get("telefono")
    })
    result = db.session.execute(text(
        f'INSERT INTO empresas (\
                empresas_cif,\
                empresas_nombre,\
                empresas_correo_electronico,\
                empresas_persona_contacto,\
                empresas_telefono) \
            VALUES (:cif, :nombre, :correo_electronico, :persona_contacto, :telefono) \
            ;'), parameters)
    db.session.commit()
    # New enterpriseId created
    newCreatedId = result.lastrowid
    response = []
    response.append ({
        "id": newCreatedId
    })
    print("Enterprises Record Created id: "+str(newCreatedId))
    print ("api addenterprises ended ...")
    return jsonify(response)

# Route to edit one enterprise(empresa)
@app.route('/editenterprise/<id>', methods=["POST", "GET"])
def editenterprise(id): 
    parameters = ({
    "cif": request.form.get("cif"),
    "nombre": request.form.get("nombre"),
    "correo_electronico": request.form.get("correo_electronico"),
    "persona_contacto": request.form.get("persona_contacto"),
    "telefono": request.form.get("telefono")
    })
    db.session.execute(text('UPDATE empresas SET \
                empresas_cif = :cif, \
                empresas_nombre = :nombre, \
                empresas_correo_electronico = :correo_electronico, \
                empresas_persona_contacto = :persona_contacto, \
                empresas_telefono = :telefono \
            WHERE empresas_id_empresa = '+id+';'), parameters)
    db.session.commit()
    response = []
    response.append ({
        "id modificated": id
    })
    print("Enterprise Record Modificated id: "+id)
    print ("api editenterprise ended ...")
    return jsonify(response)

# Route to delete one enterprise
@app.route('/deleteenterprise/<id>', methods=['DELETE'])
def deleteenterprise(id):
    # To allow ON CASCADE statements and delete Ocupations Workers automatically from Workers/Trabajadores
    db.session.execute(text(f'PRAGMA foreign_keys = ON;'))
    db.session.execute(text(f'DELETE FROM empresas WHERE empresas_id_empresa = '+id+';'))
    db.session.commit()
    response = []
    response.append ({
        "id deleted": id
    })
    print("Enterprise Record Deleted id: "+id)
    print ("api deleteenterprise ended ...")
    return jsonify(response)

# Route to SELECT all data from Enterprises(empresas) database
# for all or one Enterprise
@app.route('/get_listenterprises', methods=["POST", "GET"])
@app.route('/get_listenterprises/<id>', methods=["POST", "GET"])
def get_listenterprises(id = None): 
    if (id != None):
        result = db.session.execute(text('SELECT * FROM empresas WHERE empresas_id_empresa = '+id+';'))
    else:
        result = db.session.execute(text('SELECT * FROM empresas;'))
    db.session.close() # ONLY CLOSE WITH .FETCHALL(), THE REST IS .COMMIT() !!!
    response = [] 
    if request.method == 'POST' or request.method == 'GET':
        myResult = result.fetchall()
        myResultFieldsName = result.keys()
        #Converting data to dictionary
        response = []
        for record in myResult:
            response.append(dict(zip(myResultFieldsName, record)))
    print ("api get_listenterprises ended ...")
    return jsonify(response)

# Route to select one enterprise cif (can not be repeated).
@app.route('/check_cifexist/<cif>', methods=["GET"])
def check_cifexist(cif): 
    result = db.session.execute(text(f'SELECT * FROM empresas WHERE empresas_cif = '+cif+';'))
    db.session.commit()
    myResult = result.fetchall()
    myResultFieldsName = result.keys()
    #Convert data to dictionary
    response = []
    for record in myResult:
        response.append(dict(zip(myResultFieldsName, record)))
    return jsonify(not(len(response) == 0))
    
# Route to select one worker doi (can not be repeated).
@app.route('/check_doiexist/<doi>', methods=["GET"])
def check_doiexist(doi): 
    result = db.session.execute(text(f'SELECT * FROM trabajadores WHERE trabajadores_doi = '+doi+';'))
    db.session.commit()
    myResult = result.fetchall()
    myResultFieldsName = result.keys()
    #Convert data to dictionary
    response = []
    for record in myResult:
        response.append(dict(zip(myResultFieldsName, record)))
    return jsonify(not(len(response) == 0))
#
#
#   FROM HERE UNTIL THE END, is the initial code from the begining, to improve a lot
#
#
# Route to get worker secundary databases
@app.route('/get_worker_secundary_databases', methods=['GET'])
def get_worker_secundary_databases():
    # Creating databases list
    listTables = [  "trabajadores_situaciones",
                    "carnets",
                    "vehiculos",
                    "provincias",
                    "municipios",
                    "ocupaciones",
                    "formaciones",
    ]
    # Creating executions for each table
    result1 = db.session.execute(text(f'SELECT * FROM '+listTables[0]+';'))
    result2 = db.session.execute(text(f'SELECT * FROM '+listTables[1]+';'))
    result3 = db.session.execute(text(f'SELECT * FROM '+listTables[2]+';'))
    result4 = db.session.execute(text(f'SELECT * FROM '+listTables[3]+';'))
    result5 = db.session.execute(text(f'SELECT * FROM '+listTables[4]+';'))
    result6 = db.session.execute(text(f'SELECT * FROM '+listTables[5]+';'))
    result7 = db.session.execute(text(f'SELECT * FROM '+listTables[6]+';'))
    db.session.commit()
    
    # Getting data from each executions
    response1 = [] 
    for each in result1: 
        dataList = list(each)
        response1.append({
            "id_situacion": dataList[0],
            "descripcion_situacion": dataList[1]
        })
    response2 = [] 
    for each in result2: 
        dataList = list(each)
        response2.append({
            "id_carnet": dataList[0],
            "descripcion_carnet": dataList[1]
        })
    response3 = [] 
    for each in result3: 
        dataList = list(each)
        response3.append({
            "id_vehiculo": dataList[0],
            "descripcion_vehiculo": dataList[1]
        })
   
    response4 = [] 
    for each in result4: 
        dataList = list(each)
        response4.append({
            "id_provincia": dataList[0],
            "descripcion_provincia": dataList[1]
        })
    response5 = [] 
    for each in result5: 
        dataList = list(each)
        response5.append({
            "id_municipio": dataList[0],
            "descripcion_municipio": dataList[1]
        })
    response6 = [] 
    for each in result6: 
        dataList = list(each)
        response6.append({
            "id_ocupacion": dataList[0],
            "descripcion_ocupacion": dataList[1]
        })
    response7 = [] 
    for each in result7: 
        dataList = list(each)
        response7.append({
            "id_formacion": dataList[0],
            "descripcion_formacion": dataList[1]
        })
    response =  {
                    f'{listTables[0]}': response1,
                    f'{listTables[1]}': response2,
                    f'{listTables[2]}': response3,
                    f'{listTables[3]}': response4,
                    f'{listTables[4]}': response5,
                    f'{listTables[5]}': response6,
                    f'{listTables[6]}': response7
                }
    print ("api workers_secundary_databases ended ...")
    return jsonify(response)

# Route to SELECT all data from workers(trabajadores) database
# for all or one Worker
@app.route('/get_listworkers', methods=["POST", "GET"])
@app.route('/get_listworkers/<id>', methods=["POST", "GET"])
def get_listworkers(id = None):
    # GET THE SQLALCHEMY RESULTPROXY OBJECT
    # result = db.session.execute(text(request.get_json()['query']))
    if id:
        result = db.session.execute(text('SELECT * FROM trabajadores WHERE trabajadores_id_trabajador='+id+';'))
    else:
        result = db.session.execute(text('SELECT * FROM trabajadores'))
    db.session.commit()
    response = [] 
    if request.method == 'POST' or request.method == 'GET':
        responseOcupaciones = []
        responseFormaciones = []
        if (id != None):
            # In case of "id" retrieving worker ocupations/formations data
            # Retrieving Ocupaciones/Ocupations DATA if id in use
            resultOcupaciones=db.session.execute(text(
                f'SELECT CAST(o.ocupaciones_id_ocupacion AS VARCHAR) AS ocupaciones_id_ocupacion, \
                        o.ocupaciones_descripcion_ocupacion, \
                        t.trabajadores_ocupaciones_meses \
                    FROM trabajadores_ocupaciones t \
                    JOIN ocupaciones o ON ocupaciones_id_ocupacion = trabajadores_ocupaciones_id_ocupacion \
                    WHERE t.trabajadores_ocupaciones_id_trabajador = '+id+';'))
            db.session.commit()
            # Creating 3rd level data Ocupaciones/Ocupations
            myResult = resultOcupaciones.fetchall()
            myResultFieldsName = resultOcupaciones.keys()
            for record in myResult:
                responseOcupaciones.append(dict(zip(myResultFieldsName, record)))
            # keys = ['a', 'b', 'c']
            # values = [1, 2, 3]
            # dictionary = dict(zip(keys, values))
            # print(dictionary) # {'a': 1, 'b': 2, 'c': 3}
            
            # ITERATE OVER EACH RECORD IN RESULT AND ADD IT  
            # IN A PYTHON LIST/DICT OBJECT 
            # Creating 3rd level data Ocupaciones/Ocupations
            # for each2 in resultOcupaciones: 
            #     dataList2 = list(each2)
            #     responseOcupaciones.append({
            #         "id_ocupacion": dataList2[0],
            #         "descripcion_ocupacion": dataList2[1],
            #         "meses": dataList2[2]
            #     })
            # Retrieving Formaciones/Formations DATA if id in use
            resultFormaciones=db.session.execute(text(
                f'SELECT CAST(f.trabajadores_formaciones_id_formacion AS VARCHAR) AS trabajadores_formaciones_id_formacion, \
                        e.formaciones_descripcion_formacion \
                    FROM trabajadores_formaciones f \
                    JOIN formaciones e ON formaciones_id_formacion = f.trabajadores_formaciones_id_formacion \
                    JOIN trabajadores t ON trabajadores_id_trabajador = f.trabajadores_formaciones_id_trabajador \
                    WHERE t.trabajadores_id_trabajador = '+id+';'))
            db.session.commit()
            # Creating 3rd level data Formaciones/Formations
            myResult = resultFormaciones.fetchall()
            myResultFieldsName = resultFormaciones.keys()
            for record in myResult:
                responseFormaciones.append(dict(zip(myResultFieldsName, record)))
            # ITERATE OVER EACH RECORD IN RESULT AND ADD IT  
            # IN A PYTHON LIST/DICT OBJECT 
            # Creating 3rd level data Formaciones/Formations
            # for each2 in resultFormaciones: 
            #     dataList2 = list(each2)
            #     responseFormaciones.append({
            #         "id_formacion": dataList2[0],
            #         "descripcion_formacion": dataList2[1],
            #     })
        # ITERATE OVER EACH RECORD IN RESULT AND ADD IT  
        # IN A PYTHON LIST/DICT OBJECT 
        # i = 1
        # Creating response fields
        # for each in result: 
        #     responseOcupaciones = []
        #     responseFormaciones = []
        #     resultOcupaciones=db.session.execute(text(
        #         f'SELECT o.ocupaciones_id_ocupacion, o.ocupaciones_descripcion_ocupacion, \
        #                 t.trabajadores_ocupaciones_meses \
        #             FROM trabajadores_ocupaciones t \
        #             JOIN ocupaciones o ON ocupaciones_id_ocupacion = trabajadores_ocupaciones_id_ocupacion \
        #             WHERE t.trabajadores_ocupaciones_id_trabajador = '+id+';'))
        #     db.session.commit()
        myResult = result.fetchall()
        myResultFieldsName = result.keys()
        #Convert data to dictionary
        response = []
        for record in myResult:
            myDict = {}
            myDict = dict(zip(myResultFieldsName, record))
            myDict['ocupaciones'] = responseOcupaciones
            myDict['formaciones'] = responseFormaciones
            response.append(myDict)
            # response.append(dict(zip(myResultFieldsName, record)))

            # if (id != None):
            #     # In case of "id" retrieving worker ocupations/formations data
            #     # Retrieving Ocupaciones/Ocupations DATA if id in use
            #     resultOcupaciones=db.session.execute(text(
            #         f'SELECT o.ocupaciones_id_ocupacion, o.ocupaciones_descripcion_ocupacion, \
            #                 t.trabajadores_ocupaciones_meses \
            #             FROM trabajadores_ocupaciones t \
            #             JOIN ocupaciones o ON ocupaciones_id_ocupacion = trabajadores_ocupaciones_id_ocupacion \
            #             WHERE t.trabajadores_ocupaciones_id_trabajador = '+id+';'))
            #     db.session.commit()
            #     # ITERATE OVER EACH RECORD IN RESULT AND ADD IT  
            #     # IN A PYTHON LIST/DICT OBJECT 
            #     # Creating 3rd level data Ocupaciones/Ocupations
            #     for each2 in resultOcupaciones: 
            #         dataList2 = list(each2)
            #         responseOcupaciones.append({
            #             "id_ocupacion": dataList2[0],
            #             "descripcion_ocupacion": dataList2[1],
            #             "meses": dataList2[2]
            #         })
            #     # Retrieving Formaciones/Formations DATA if id in use
            #     resultFormaciones=db.session.execute(text(
            #         f'SELECT f.trabajadores_formaciones_id_formacion, e.formaciones_descripcion_formacion \
            #             FROM trabajadores_formaciones f \
            #             JOIN formaciones e ON formaciones_id_formacion = f.trabajadores_formaciones_id_formacion \
            #             JOIN trabajadores t ON trabajadores_id_trabajador = f.trabajadores_formaciones_id_trabajador \
            #             WHERE t.trabajadores_id_trabajador = '+id+';'))
            #     db.session.commit()
            #     # ITERATE OVER EACH RECORD IN RESULT AND ADD IT  
            #     # IN A PYTHON LIST/DICT OBJECT 
            #     # Creating 3rd level data Formaciones/Formations
            #     for each2 in resultFormaciones: 
            #         dataList2 = list(each2)
            #         responseFormaciones.append({
            #             "id_formacion": dataList2[0],
            #             "descripcion_formacion": dataList2[1],
            #         })
            # # Retrieving Trabajador/Worker DATA
            # dataList = list(each)
            # response.append({
            #     "id": dataList[0],
            #     "nombre": dataList[1],
            #     "apellidos": dataList[2],
            #     "fecha_nacimiento": dataList[3],
            #     "doi": dataList[4],
            #     "id_municipio": dataList[5],
            #     "codigo_postal": dataList[6],
            #     "id_provincia": dataList[7],
            #     "id_vehiculo": dataList[8],
            #     "curriculum": dataList[9],
            #     "telefono_contacto": dataList[10],
            #     "correo_electronico": dataList[11],
            #     "id_situacion": dataList[12],
            #     "lopd": bool(dataList[13]),
            #     "ocupaciones": responseOcupaciones,
            #     "formaciones": responseFormaciones
            #     })
            # i+= 1
    print ("api get_listworker ended ...")
    return jsonify(response)


# Route to delete one worker(trabajador)
@app.route('/deleteworker/<id>', methods=['DELETE'])
def deleteworker(id):
    # To allow ON CASCADE statements and delete Ocupations Workers automatically from Workers/Trabajadores
    db.session.execute(text(f'PRAGMA foreign_keys = ON;'))
    db.session.execute(text(f'DELETE FROM trabajadores WHERE trabajadores_id_trabajador = '+id+';'))
    db.session.commit()
    response = []
    response.append ({
        "id deleted": id
    })
    print("Worker Record Deleted id: "+id)
    print ("api deleteworker ended ...")
    return response

# Route to add worker in the database
@app.route('/addworker', methods=["POST", "GET"]) 
def addworker(): 
    # Populating Workers/trabajadores table
    parameters = ({
        "nombre" : request.form.get("trabajadores[trabajadores_nombre]"),
        "apellidos" : request.form.get("trabajadores[trabajadores_apellidos]"),
        "fecha_nacimiento" : request.form.get("trabajadores[trabajadores_fecha_nacimiento]"),
        "doi" : request.form.get("trabajadores[trabajadores_doi]"), 
        "id_municipio" : request.form.get("trabajadores[trabajadores_id_municipio]"),
        "codigo_postal" : request.form.get("trabajadores[trabajadores_codigo_postal]"),
        "id_provincia" : request.form.get("trabajadores[trabajadores_id_provincia]"),
        "id_vehiculo" : request.form.get("trabajadores[trabajadores_id_vehiculo]"),
        "curriculum" : request.form.get("trabajadores[trabajadores_curriculum]"),
        "telefono_contacto" : request.form.get("trabajadores[trabajadores_telefono_contacto]"),
        "correo_electronico" :  request.form.get("trabajadores[trabajadores_correo_electronico]"),
        "id_situacion" :  request.form.get("trabajadores[trabajadores_id_situacion]"),
        "lopd" : request.form.get("trabajadores[trabajadores_lopd]")
    })
    result = db.session.execute(text(
        f'INSERT INTO trabajadores (\
                trabajadores_nombre,\
                trabajadores_apellidos,\
                trabajadores_fecha_nacimiento,\
                trabajadores_doi,\
                trabajadores_id_municipio,\
                trabajadores_codigo_postal,\
                trabajadores_id_provincia, \
                trabajadores_id_vehiculo, \
                trabajadores_curriculum, \
                trabajadores_telefono_contacto, \
                trabajadores_correo_electronico, \
                trabajadores_id_situacion, \
                trabajadores_lopd)\
            VALUES (:nombre, :apellidos, :fecha_nacimiento, :doi, :id_municipio, \
                :codigo_postal, :id_provincia, :id_vehiculo, :curriculum, :telefono_contacto, \
                :correo_electronico, :id_situacion, :lopd) \
                ;'), parameters)

    db.session.commit()
    # New workerId created
    newCreatedId = result.lastrowid
    # Populating Ocupations table
    ocupations = request.form.get("trabajadores[trabajadores_ocupaciones]")
    ocupations2= json.loads(ocupations) # Converting to list
    for each in ocupations2:
        parametersOcupationsWorker = ({
            "id_trabajador" : newCreatedId,
            # "id_ocupacion" : each['id_ocupacion'],
            "id_ocupacion" : each['ocupaciones_id_ocupacion'],
            "meses" : int(each['trabajadores_ocupaciones_meses'])
        })
        result = db.session.execute(text(
            f'INSERT INTO trabajadores_ocupaciones (\
                    trabajadores_ocupaciones_id_trabajador,\
                    trabajadores_ocupaciones_id_ocupacion,\
                    trabajadores_ocupaciones_meses) \
                VALUES (:id_trabajador, :id_ocupacion, :meses) \
                ;'), parametersOcupationsWorker) 
    # Populating Formations table
    formations = request.form.get("trabajadores[trabajadores_formaciones]")
    formations2= json.loads(formations) # Converting to list
    for each in formations2:
        parametersFormationsWorker = ({
            "id_trabajador" : newCreatedId,
            "id_formacion" : each['trabajadores_formaciones_id_formacion'],
        })
        result = db.session.execute(text(
            f'INSERT INTO trabajadores_formaciones (\
                    trabajadores_formaciones_id_trabajador,\
                    trabajadores_formaciones_id_formacion) \
                VALUES (:id_trabajador, :id_formacion) \
                ;'), parametersFormationsWorker) 
    db.session.commit()
    response = []
    response.append ({
        "id": newCreatedId
    })
    print("Worker Record Created id: "+str(newCreatedId))
    print ("api addworker ended ...")
    return response

# Route to edt worker(trabajador) in the database
@app.route('/editworker/<id>', methods=["POST", "GET"])
def editworker(id): 
    parameters = ({
        "nombre" : request.form.get("trabajadores[trabajadores_nombre]"),
        "apellidos" : request.form.get("trabajadores[trabajadores_apellidos]"),
        "fecha_nacimiento" : request.form.get("trabajadores[trabajadores_fecha_nacimiento]"),
        "doi" : request.form.get("trabajadores[trabajadores_doi]"), 
        "id_municipio" : request.form.get("trabajadores[trabajadores_id_municipio]"),
        "codigo_postal" : request.form.get("trabajadores[trabajadores_codigo_postal]"),
        "id_provincia" : request.form.get("trabajadores[trabajadores_id_provincia]"),
        "id_vehiculo" : request.form.get("trabajadores[trabajadores_id_vehiculo]"),
        "curriculum" : request.form.get("trabajadores[trabajadores_curriculum]"),
        "telefono_contacto" : request.form.get("trabajadores[trabajadores_telefono_contacto]"),
        "correo_electronico" : request.form.get("trabajadores[trabajadores_correo_electronico]"),
        "id_situacion" : request.form.get("trabajadores[trabajadores_id_situacion]"),
        "lopd" : request.form.get("trabajadores[trabajadores_lopd]")
    })
    result = db.session.execute(text(
        f'UPDATE trabajadores SET \
                trabajadores_nombre = :nombre, \
                trabajadores_apellidos = :apellidos, \
                trabajadores_fecha_nacimiento = :fecha_nacimiento, \
                trabajadores_doi = :doi, \
                trabajadores_id_municipio = :id_municipio, \
                trabajadores_codigo_postal = :codigo_postal, \
                trabajadores_id_provincia = :id_provincia, \
                trabajadores_id_vehiculo = :id_vehiculo, \
                trabajadores_curriculum = :curriculum, \
                trabajadores_telefono_contacto = :telefono_contacto, \
                trabajadores_correo_electronico = :correo_electronico, \
                trabajadores_id_situacion = :id_situacion, \
                trabajadores_lopd = :lopd \
            WHERE trabajadores_id_trabajador = '+id+';'), parameters) 
    # Deleting old Ocupations/Formations via ON CASCADE on Worker table
    result0 = db.session.execute(text(f'PRAGMA foreign_keys = ON;'))
    db.session.execute(text(
        'DELETE FROM trabajadores_ocupaciones \
            WHERE trabajadores_ocupaciones.trabajadores_ocupaciones_id_trabajador = '+id+';'))
    db.session.execute(text(
        'DELETE FROM trabajadores_formaciones \
            WHERE trabajadores_formaciones.trabajadores_formaciones_id_trabajador = '+id+';'))
    # Populating Ocupations table with new values
    ocupations = request.form.get("trabajadores[trabajadores_ocupaciones]")
    ocupations2= json.loads(ocupations) # Converting to list
    for each in ocupations2:
        parametersOcupationsWorker = ({
            "id_trabajador" : id,
            "id_ocupacion" : each['ocupaciones_id_ocupacion'],
            "meses" : int(each['trabajadores_ocupaciones_meses'])
        })
        result = db.session.execute(text(
            f'INSERT INTO trabajadores_ocupaciones (\
                    trabajadores_ocupaciones_id_trabajador,\
                    trabajadores_ocupaciones_id_ocupacion,\
                    trabajadores_ocupaciones_meses) \
                VALUES (:id_trabajador, :id_ocupacion, :meses) \
                ;'), parametersOcupationsWorker) 

    # Populating Formations table with new values
    formations = request.form.get("trabajadores[trabajadores_formaciones]")
    formations2= json.loads(formations) # Converting to list
    print(formations2)
    for each in formations2:
        # print(each)
        parametersFormationsWorker = ({
            "id_trabajador" : id,
            "id_formacion" : each['trabajadores_formaciones_id_formacion'],
        })
        result = db.session.execute(text(
            f'INSERT INTO trabajadores_formaciones (\
                    trabajadores_formaciones_id_trabajador,\
                    trabajadores_formaciones_id_formacion) \
                VALUES (:id_trabajador, :id_formacion) \
                ;'), parametersFormationsWorker) 

    db.session.commit()
    response = []
    response.append ({
        "id modificated": id
    })
    print("Workers Record Modificated id: "+id)
    print ("api editworker ended ...")
    return jsonify(response)


if __name__ == '__main__':
    # use_reloaded to avoid echo on reply from Flask
    app.run(port=5000, host="0.0.0.0", debug=False, use_reloader=False)
    # app.run(port=5000, host="localhost", debug=True, use_reloader=False)

