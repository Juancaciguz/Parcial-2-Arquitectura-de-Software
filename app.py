from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/<int:n>', methods=['GET'])
def calcular_factorial(n):
    if n < 0:
        return jsonify({
            "error": "El factorial solo está definido para números enteros no negativos."
        }), 400

    try:
        resultado_factorial = math.factorial(n)
        
    except OverflowError:
        resultado_factorial = str(math.factorial(n)) 

    if n == 0 or n == 1:
        etiqueta_paridad = "impar"
    else: 
        etiqueta_paridad = "par"


    respuesta = {
        "numero_recibido": n,
        "factorial": resultado_factorial,
        "etiqueta": etiqueta_paridad
    }

    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)