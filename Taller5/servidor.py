""" Rutina del servidor que realiza las operaciones REST
"""
from flask import render_template
import connexion

# Crear la instancia de la aplicacion y definir la ruta del archivo yml
app = connexion.App(__name__, specification_dir='./')

# Leer el archivo yml para configurar la api
app.add_api('swagger.yml')

# Crear la ruta URL "/" en la aplicacion
@app.route('/')
def home():
    """
    Esta funcion solo responde en el navegador al URL
    localhost:8000/
    :return:        el template 'home.html' (ubicado en la carpeta templates)
    """
    return render_template('home.html')

# Si esta ejecutando en modo stand alone
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)