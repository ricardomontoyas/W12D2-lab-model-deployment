from flask import Flask, render_template, request, jsonify
from helper import run_model, transform_data, json_interpreter
import sys
import pandas as pd
from datetime import datetime

app = Flask("__name__")

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        # Obtener JSON y llaves recibidas
        data_json = request.get_json()
        input_keys = set(data_json.keys())
        # Campos requeridos para json_interpreter
        required_fields = { 'Campaign Name',
                             'Ad Set Name',
                             'Ad Name',
                             'Ad Format'
                             'Campaign Budget',
                             'Ad Set Budget',
                             'Amount Spent (USD)',
                             'CTR (porcentaje de clics en el enlace)',
                             'CPC (Coste por clic en el enlace)',
                             #'CPM (coste por 1000 impresiones)',
                             'CVR_Click_Results'}

        try:
            # Interpretar y transformar datos
            df = json_interpreter(data_json),
            dt = transform_data(df)
            prediction = run_model(dt)
            return {"Prediction": prediction}
            datetime.strptime(data["date"], "%d-%m-%Y")
        except ValueError:
             return jsonify({
            "status": "error",
            "message": "'date' must have this format 'DD-MM-YYYY'."
        }), 400
        except KeyError as e:
            # Error por llave faltante internamente
            return jsonify(
                status='error',
                message=f"Missing Field: {e.args[0]}"), 400
        
        except ValueError as e:
        # Error en tipos o validación
            return jsonify (
                status='error',
                message="Verify the entries"
            ), 400
           
    else:    # Para GET devuelve estado de vida
        return {"status":"alive"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)