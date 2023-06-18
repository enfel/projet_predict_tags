# Importer le modèle
from tensorflow.keras.models import load_model
import tensorflow as tf

app = Flask(__name__)

# Charger le modèle
model = load_model("embed_model.h5")

# Créer une fonction pour prédire les tags à partir d'une question
def predict_tags(question):
    # Prédire les tags à partir du modèle
    tags = model.predict(question)
    # Retourner les tags au format JSON
    return jsonify(tags)

# Créer une route pour l'API
@app.route("/api/tags", methods=["POST"])
def api_tags():
    # Récupérer la question envoyée par le client
    question = request.json.get("question")
    # Appeler la fonction de prédiction
    tags = predict_tags(question)
    # Retourner les tags au client
    return tags

# Créer une route pour la page d'accueil
@app.route("/")
def index():
    # Renvoyer le modèle index.html
    return render_template("index.html")

# Lancer le serveur en mode debug
if __name__ == "__main__":
    app.run(debug=True)




"""
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
import tensorflow as tf

#import pickle

app = Flask(__name__)

# Charger le modèle à partir du fichier pickle
#filename = "ovr_sgd.pickle"
#model = pickle.load(open(filename, "rb"))


# Charger le modèle
model = load_model("embed_model.h5")

@app.route("/api/tags", methods=["POST"])
def predict_tags():
    # Récupérer la question envoyée par le client
    question = request.json.get("question")
    # Prédire les tags à partir du modèle
    tags = model.predict(question)
    # Retourner les tags au format JSON
    return jsonify(tags)

@app.route("/")
def index():
    # Renvoyer le modèle index.html
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)"""