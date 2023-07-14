from flask import Flask
from flask import request
import joblib

app = Flask(__name__)

def retrieve_model(path):
    return joblib.load(path)

lgbr_cars = retrieve_model("lgbr_cars.model")

def make_prediction(trained_model, single_input):
    return (trained_model.predict(single_input))[0]

#/predictCarPrice?vehicleType=-1&gearbox=1&powerPS=0&model=118&kilometer=150000&monthOfRegistration=0&fuelType=1&brand=38
@app.get('/predictCarPrice')
def predictingCarPrice():
    vehicleType = request.args.get('vehicleType')
    gearbox = request.args.get('gearbox')
    powerPS = request.args.get('powerPS')
    model = request.args.get('model')
    kilometer = request.args.get('kilometer')
    monthOfRegistration = request.args.get('monthOfRegistration')
    fuelType = request.args.get('fuelType')
    brand = request.args.get('brand')
    print(type(vehicleType))
    input = [[int(vehicleType),int(gearbox),int(powerPS),int(model),int(kilometer),int(monthOfRegistration),int(fuelType),int(brand)]]
    predicted_price=make_prediction(lgbr_cars,input)
    return "Predicted price = "+str(round(predicted_price,2))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)