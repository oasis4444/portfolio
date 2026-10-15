"""Portfolio Création Logiciel Sur Mesure — serveur Flask pour PythonAnywhere.

Sert le site statique (index.html, demos/, img/) tel quel.
"""
import os
from flask import Flask, send_from_directory, abort

BASE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=None)


@app.route("/")
def accueil():
    return send_from_directory(BASE, "index.html")


@app.route("/<path:chemin>")
def fichier(chemin):
    if chemin.startswith(".") or chemin.endswith(".py"):
        abort(404)
    complet = os.path.join(BASE, chemin)
    if os.path.isdir(complet):
        chemin = os.path.join(chemin, "index.html")
    return send_from_directory(BASE, chemin)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
