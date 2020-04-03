import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

model = pickle.load(open('./Model/model1.pkl', 'rb'))


@app.route('/', methods=['POST'])
def predict():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])

    labels = {0: 'No Heart Disease', 1: "Heart Disease Present"}
    y = model.predict([[age, sex, cp, trestbps, chol, fbs,
                        restecg, thalach, exang, oldpeak, slope, ca, thal]])
    return labels[int(y)]


if __name__ == '__main__':
    app.run(debug=True)
