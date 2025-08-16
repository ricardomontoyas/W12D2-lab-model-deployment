#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import pandas as pd

def json_interpreter(data_json):
    """
    Convierte el JSON de entrada en un DataFrame de una fila con las columnas esperadas.
    """
    # Extraemos cada campo y lo ponemos en un dict
    d = {
        'Campaign Name': data_json['Campaign Name'],
        'Ad Set Name':   data_json['Ad Set Name'],
        'Ad Name':       data_json['Ad Name'],
        'Ad Format':     data_json['Ad Format'],
        'Campaign Budget': data_json['Campaign Budget'],
        'Ad Set Budget':   data_json['Ad Set Budget'],
        'Amount Spent (USD)': data_json['Amount Spent (USD)'],
        'CTR (porcentaje de clics en el enlace)': data_json['CTR (porcentaje de clics en el enlace)'],
        'CPC (Coste por clic en el enlace)': data_json['CPC (Coste por clic en el enlace)'],
        'CVR_Click_Results': data_json['CVR_Click_Results']
    }
    return pd.DataFrame([d])

def transform_data(df):
    """
    Aplica las transformaciones necesarias para generar las columnas que espera el RandomForest.
    """
    # Ejemplo: combinamos presupuestos
    df['Budget'] = (
        df['Campaign Budget'].astype(float)
      + df['Ad Set Budget'].astype(float)
    )
    # Ejemplo: detectamos si el nombre del anuncio incluye la palabra "video"
    df['Ad_Video'] = df['Ad Name'].str.contains('video', case=False, na=False).astype(int)

    # Selecciona SOLO las columnas de entrada que tu modelo espera:
    return df[[
        'Amount Spent (USD)',
        'CTR (porcentaje de clics en el enlace)',
        'CPC (Coste por clic en el enlace)',
        'CVR_Click_Results',
        'Budget',
        'Ad_Video'
    ]]

def run_model(df):
    """
    Carga el pickle del modelo y devuelve la predicción.
    """
    with open('best_model_W_Random_Forest.pkl', 'rb') as f:
        model = pickle.load(f)
    preds = model.predict(df)
    return float(preds[0])
