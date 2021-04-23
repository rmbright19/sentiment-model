import streamlit as st
import pandas as pd
import numpy as np
import TextPreprocessing as tp
import pickle

loaded_classifier = pickle.load(open('sentiment_svc.pickle', 'rb'))
loaded_vectorizer = pickle.load(open('sentiment_tfidf.pickle', 'rb'))

st.title("Twitter Sentiment Analysis App")
text = st.text_input("Tweet to analyze:")
st.write("Tweet:")
st.write(text)

# Preprocess text
text_cleaned = tp.clean_tweet(text)

transformed_data = loaded_vectorizer.transform([text_cleaned])
prediction = loaded_classifier.predict(transformed_data)

if prediction[0] == 0:
	prediction_name = "Negative"
elif prediction[0] == 1:
	prediction_name = "Neutral"
else:
	prediction_name = "Positive"

st.write(f"Sentiment: {prediction_name}")
