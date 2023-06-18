from flask import Flask, request, jsonify, render_template
#from tensorflow.keras.models import load_model
#import tensorflow as tf


import pickle

app = Flask(__name__)

# Charger le modèle à partir du fichier pickle
filename = "ovr_sgd.pickle"
model = pickle.load(open(filename, "rb"))


# Charger le modèle
#model = load_model("embed_model.h5")

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
    app.run(debug=True)
"""
# Importer le modèle
from tensorflow.keras.models import load_model

# Charger le modèle
model = load_model("embed_model.h5")

# Définir l'API Flask
app = Flask(__name__)

@app.route("/", methods=["POST"])
def predict():
# Obtenir les données JSON
data = request.get_json(force=True)

# Convertir les données en DataFrame
df = pd.DataFrame(data)

# Préparer les données pour le modèle
x = df["sentence"].values

# Faire une prédiction avec le modèle
y_pred = model.predict(x)

# Retourner la prédiction sous forme de JSON
return jsonify(y_pred.tolist())"""