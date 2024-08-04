import streamlit as st
import os
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
image_path = "C:/Users/91981/sentiment image.png"
if not os.path.isfile(image_path):
    print(f"Error: The file {image_path} does not exist.")
else:
    image = Image.open(image_path)
image = Image.open(image_path)
st.image(image, use_column_width=True)

st.write('Enter a sentence to get its sentiment prediction.')

text_input = st.text_area('Input Text')

if st.button('Predict'):
    if text_input:
        sentiment = predict_sentiment(text_input)
        st.write(f'Sentiment: {sentiment}')
    else:
        st.write('Please enter some text.')
