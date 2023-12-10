from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'imagenes_recibidas'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def create_folders():
    # Crear una estructura de carpetas basada en la fecha actual
    today = datetime.today()
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], today.strftime('%Y/%m/%d'))
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


@app.route('/v1/imagenes/', methods=['POST'])
def recibir_imagen():
    try:
        # Obtener la imagen de la solicitud
        imagen = request.files['imagen']

        # Crear la estructura de carpetas basada en la fecha
        folder_path = create_folders()

        # Guardar la imagen en la carpeta correspondiente
        filename = os.path.join(folder_path, f"{datetime.now().strftime('%H-%M-%S')}.jpeg")
        imagen.save(filename)

        return jsonify({'mensaje': 'Imagen recibida exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
