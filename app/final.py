import streamlit as st
import pandas as pd
import joblib
import numpy as np
import base64
from sklearn.preprocessing import LabelEncoder

# Function to get base64 string of an image
def get_base64_of_file(file_path):
    with open(file_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')

# Function to set a background image using custom CSS
def set_bg_image(image_file):
    bin_str = get_base64_of_file(image_file)
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

# Set the background image using the path to your image
set_bg_image("C:\\Final\\image.jpg")  # Adjust path as needed

# Define the ExtendedLabelEncoder within your Streamlit application
class ExtendedLabelEncoder(LabelEncoder):
    def fit(self, y):
        unique_classes = np.unique(y)
        super().fit(np.append(unique_classes, '<unknown>'))
        return self

    def transform(self, y):
        new_y = np.array([item if item in self.classes_ else '<unknown>' for item in y])
        return super().transform(new_y)

# Load the trained model and encoders
model = joblib.load('best_model.pkl')

# Load your dataset
data = pd.read_csv('Trafficviolations.csv')  # adjust path as needed

# Filter options to only include the most common entries
data['Make'] = data['Make'].where(data['Make'].map(data['Make'].value_counts()) > 100, 'Other')
data['Description'] = data['Description'].where(data['Description'].map(data['Description'].value_counts()) > 100, 'Other Violation')
data['Location'] = data['Location'].where(data['Location'].map(data['Location'].value_counts()) > 100, 'Other Location')

# Function to encode inputs
def encode_inputs(make, description, location, driver_state, gender):
    make_encoder = joblib.load('make_encoder.pkl')
    description_encoder = joblib.load('description_encoder.pkl')
    location_encoder = joblib.load('location_encoder.pkl')
    driver_state_encoder = joblib.load('driver_state_encoder.pkl')
    gender_encoder = joblib.load('gender_encoder.pkl')
    
    make_encoded = make_encoder.transform([make])
    description_encoded = description_encoder.transform([description])
    location_encoded = location_encoder.transform([location])
    driver_state_encoded = driver_state_encoder.transform([driver_state])
    gender_encoded = gender_encoder.transform([gender])
    
    return [make_encoded[0], description_encoded[0], location_encoded[0], driver_state_encoded[0], gender_encoded[0]]

# Main app
st.title('Traffic Violation Type Prediction')
st.write('Please enter the details of the traffic violation to predict the type of violation.')

with st.form("prediction_form"):
    make = st.selectbox('Car Make', options=np.unique(data['Make'].dropna()))
    description = st.selectbox('Violation Description', options=np.unique(data['Description'].dropna()))
    location = st.selectbox('Location of Violation', options=np.unique(data['Location'].dropna()))
    driver_state = st.selectbox('Driver State', options=['MD', 'VA', 'PA', 'NY', 'CA'])
    gender = st.selectbox('Gender', options=['M', 'F'])
    submit_button = st.form_submit_button("Predict")

if submit_button:
    encoded_features = encode_inputs(make, description, location, driver_state, gender)
    features = pd.DataFrame([encoded_features], columns=['Make', 'Description', 'Location', 'Driver State', 'Gender'])
    prediction = model.predict(features)
    st.success(f'Predicted Violation Type: {prediction[0]}')

st.sidebar.info('Enter the required fields and click predict to see the output.')
