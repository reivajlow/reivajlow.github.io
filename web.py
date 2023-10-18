from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/procesar-mensaje', methods=['POST'])
def procesar_mensaje():
    data = request.get_json()
    mensaje = data.get("mensaje", "")

    # Aquí puedes enviar el mensaje a la API de OpenAI y obtener una respuesta
    # respuesta = llamar_a_openai(mensaje)

    # Por ahora, vamos a simular una respuesta
    respuesta = "Respuesta simulada de OpenAI"

    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run()
