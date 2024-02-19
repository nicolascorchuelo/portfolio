import pandas as pd
from flask import Flask, jsonify, request
from etl import etl_data_obj
from flask_swagger_ui import get_swaggerui_blueprint

app= Flask(__name__)

SWAGGER_URL= "/swagger"
API_URL= "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL,API_URL,config={'app_name': 'Access API'})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.get('/consult')
def get_data():
    id = request.args.get('id')
    table = request.args.get('table')
    d=etl_data_obj.get_details(id,table)
    print('value returned',d) 
    return jsonify(d)

@app.post('/load')
def post_data():
    data = request.json
    k=etl_data_obj.post_data(data['file'],data['table'],data['delete_data'])
    return jsonify(data)

if __name__=="__main__":
   app.run(host = "0.0.0.0",port = 8010,debug = True)