from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import duckdb
import pandas as pd

app = Flask(__name__)
CORS(app)

modelo_regresion = joblib.load('modelo_regresion.pkl')
modelo_clasificacion = joblib.load('modelo_clasificacion.pkl')

db = duckdb.connect('warehouse.db', read_only=True)

@app.route('/api/olap/top_areas', methods=['GET'])
def get_top_areas():
    query = """
    SELECT community, ROUND(AVG(price_usd), 2) as precio_promedio
    FROM fact_sales 
    GROUP BY community 
    ORDER BY precio_promedio DESC 
    LIMIT 5
    """
    df_olap = db.execute(query).df()
    return jsonify(df_olap.to_dict(orient='records'))

@app.route('/api/predecir', methods=['POST'])
def predecir():
    data = request.json
    df_input = pd.DataFrame([data])
    
    precio_estimado = modelo_regresion.predict(df_input)[0]
    es_freehold = modelo_clasificacion.predict(df_input)[0]
    
    return jsonify({
        'precio_estimado_usd': float(precio_estimado),
        'is_freehold': int(es_freehold)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)