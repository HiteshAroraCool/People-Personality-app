from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model from the pickle file
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract data from form fields
            age = int(request.form['Age'])
            gender = int(request.form['gender'])
            education = int(request.form['edu'])
            interest = int(request.form['Interest'])
            introversion = float(request.form['introversion'])
            sensor = float(request.form['Sensor'])
            thinking = float(request.form['Thinking'])
            judging = float(request.form['Judging'])

            # Create input array for model
            features = [age, gender, education, interest, introversion, sensor, thinking, judging]

            mbti_types = {
                "ISTJ": {
                    "type": "Introverted, Sensing, Thinking, Judging",
                    "nickname": "The Inspector",
                    "traits": ["Responsible", "Organized", "Practical"]
                },
                "ISFJ": {
                    "type": "Introverted, Sensing, Feeling, Judging",
                    "nickname": "The Protector",
                    "traits": ["Compassionate", "Detail-oriented", "Loyal"]
                },
                "INFJ": {
                    "type": "Introverted, Intuition, Feeling, Judging",
                    "nickname": "The Advocate",
                    "traits": ["Idealistic", "Insightful", "Principled"]
                },
                "INTJ": {
                    "type": "Introverted, Intuition, Thinking, Judging",
                    "nickname": "The Architect",
                    "traits": ["Strategic", "Analytical", "Independent"]
                },
                "ISTP": {
                    "type": "Introverted, Sensing, Thinking, Perceiving",
                    "nickname": "The Virtuoso",
                    "traits": ["Adventurous", "Logical", "Hands-on"]
                },
                "ISFP": {
                    "type": "Introverted, Sensing, Feeling, Perceiving",
                    "nickname": "The Composer",
                    "traits": ["Artistic", "Gentle", "Spontaneous"]
                },
                "INFP": {
                    "type": "Introverted, Intuition, Feeling, Perceiving",
                    "nickname": "The Mediator",
                    "traits": ["Creative", "Empathetic", "Idealistic"]
                },
                "INTP": {
                    "type": "Introverted, Intuition, Thinking, Perceiving",
                    "nickname": "The Logician",
                    "traits": ["Curious", "Analytical", "Independent"]
                },
                "ESTP": {
                    "type": "Extraverted, Sensing, Thinking, Perceiving",
                    "nickname": "The Entrepreneur",
                    "traits": ["Energetic", "Pragmatic", "Action-oriented"]
                },
                "ESFP": {
                    "type": "Extraverted, Sensing, Feeling, Perceiving",
                    "nickname": "The Entertainer",
                    "traits": ["Sociable", "Lively", "Spontaneous"]
                },
                "ENFP": {
                    "type": "Extraverted, Intuition, Feeling, Perceiving",
                    "nickname": "The Campaigner",
                    "traits": ["Enthusiastic", "Imaginative", "Sociable"]
                },
                "ENTP": {
                    "type": "Extraverted, Intuition, Thinking, Perceiving",
                    "nickname": "The Debater",
                    "traits": ["Innovative", "Energetic", "Intellectually curious"]
                },
                "ESTJ": {
                    "type": "Extraverted, Sensing, Thinking, Judging",
                    "nickname": "The Executive",
                    "traits": ["Organized", "Assertive", "Pragmatic"]
                },
                "ESFJ": {
                    "type": "Extraverted, Sensing, Feeling, Judging",
                    "nickname": "The Consul",
                    "traits": ["Caring", "Social", "Organized"]
                },
                "ENFJ": {
                    "type": "Extraverted, Intuition, Feeling, Judging",
                    "nickname": "The Protagonist",
                    "traits": ["Charismatic", "Empathetic", "Organized"]
                },
                "ENTJ": {
                    "type": "Extraverted, Intuition, Thinking, Judging",
                    "nickname": "The Commander",
                    "traits": ["Confident", "Strategic", "Decisive"]
                }
            }
            
            # Make prediction
            prediction = model.predict(features)
            # Get the predicted MBTI type
            predicted_mbti = mbti_types.get(prediction[0], {})

            # Construct prediction text
            if predicted_mbti:
                prediction_text = f"Boom! 🎉 Your personality type is {predicted_mbti.get('type')}.\
                    You’re all about being {predicted_mbti.get('nickname')}, and your vibe is {', '.join(predicted_mbti.get('traits'))}."
            else:
                prediction_text = "Prediction not found."
            return render_template('index.html', prediction_text=prediction_text)
        except Exception as e:
            return render_template('index.html', prediction_text=f"Error in prediction: {str(e)}")
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)