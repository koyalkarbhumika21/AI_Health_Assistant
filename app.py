from flask import Flask, render_template, request

app = Flask(__name__)

# Disease database
disease_data = {
    "fever": {
        "disease": "Flu",
        "precaution": "Take rest and drink plenty of water",
        "diet": "Soup and warm fluids"
    },

    "cough": {
        "disease": "Common Cold",
        "precaution": "Avoid cold drinks and rest well",
        "diet": "Warm water and fruits"
    },

    "headache": {
        "disease": "Migraine",
        "precaution": "Sleep properly and reduce stress",
        "diet": "Drink enough water"
    },

    "stomach pain": {
        "disease": "Gastritis",
        "precaution": "Avoid spicy foods",
        "diet": "Light and bland food"
    }
}


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Predict disease
@app.route('/predict', methods=['POST'])
def predict():

    symptoms = request.form['symptom'].lower().split(',')

    disease = "Unknown Disease"
    precaution = "Consult a doctor"
    diet = "Healthy balanced diet"

    for symptom in symptoms:

        symptom = symptom.strip()

        if symptom in disease_data:

            disease = disease_data[symptom]["disease"]
            precaution = disease_data[symptom]["precaution"]
            diet = disease_data[symptom]["diet"]

            break

    return render_template(
        'index.html',
        result=disease,
        precaution=precaution,
        diet=diet
    )

# Run app
if __name__ == '__main__':
    app.run(debug=True)