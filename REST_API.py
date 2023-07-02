import pickle
from flask import Flask, request, json, jsonify, render_template

app = Flask(__name__)

filename = 'churn.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/churn/v1/predict', methods=['POST'])
def predict():
    contract = request.form.get('Contract')
    tech_support = request.form.get('TechSupport')
    payment_method = request.form.get('PaymentMethod')
    internet_service = request.form.get('InternetService')
    paperless_billing = request.form.get('PaperlessBilling')
    senior_citizen = request.form.get('SeniorCitizen')
    streaming_movies = request.form.get('StreamingMovies')
    streaming_tv = request.form.get('StreamingTV')
    monthly_charges = float(request.form.get('MonthlyCharges'))

    features_list = [
        1 if contract == 'Month-to-month' else 0,
        1 if tech_support == 'Yes' else 0,
        1 if payment_method == 'Electronic check' else 0,
        1 if internet_service == 'Fiber optic' else 0,
        1 if paperless_billing == 'Yes' else 0,
        int(senior_citizen),
        1 if streaming_movies == 'Yes' else 0,
        1 if streaming_tv == 'Yes' else 0,
        monthly_charges
    ]

    prediction = loaded_model.predict([features_list])

    response = {
        'prediction': 'Yes' if prediction[0] == 1 else 'No',
    }

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
