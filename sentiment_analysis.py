import streamlit as st
import joblib
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to predict sentiment
def predict_sentiment(text):
    text_transformed = vectorizer.transform([text])
    prediction = model.predict(text_transformed)
    return prediction[0]

# Streamlit app layout
st.title('Student Sentiment Analysis App ')
st.write('Enter a sentence to get its sentiment prediction.')

text_input = st.text_area('Input Text')

if st.button('Predict'):
    if text_input:
        sentiment = predict_sentiment(text_input)
        st.write(f'Sentiment: {sentiment}')
    else:
        st.write('Please enter some text.')
