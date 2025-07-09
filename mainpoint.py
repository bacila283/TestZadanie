from flask import Flask
# from webController import web_bp
from flask_service.Controllers.NumberRecognerController import webapi_number_recogner
from Services.Init_car_number_model import get_model

app = Flask(__name__)

app.register_blueprint(webapi_number_recogner)

if __name__ == "__main__":

    get_model("AIModels\micromodel.cbm")#init ai model
    
    app.run(
        host='0.0.0.0',
        port=8082
    )