import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open(r'C:\Users\mercy\Downloads\Binge_trial\binge.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    #For rendering results on HTML GUI
    
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    
    
    return render_template('home.html', prediction_text='Your binge eating level is: {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)