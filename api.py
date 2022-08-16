# libraries
from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import sys

# Definicion del API
app = Flask(__name__)

# Ruta para acceder API con metodo POST.
@app.route('/predict', methods=['POST'])

#cargar modelo predictivo
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(lr.predict(query))

            return jsonify({'prediction': str(prediction)})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

#boilerplate code
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 12345 # codigo port por el cual accederiamos al API

    lr = joblib.load("model.pkl") # cargar "model.pkl"
    print ('Model loaded')
    model_columns = joblib.load("model_columns.pkl") # cargar "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)
