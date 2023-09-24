import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('your_model.pkl')  # Replace 'your_model.pkl' with the correct path

# Create a Streamlit web app
st.title('Depression Prediction Dashboard')

# Create input widgets for user data
age = st.slider('Age', 18, 99, 25)
gender = st.radio('Gender', ['Male', 'Female'])
exercise_frequency = st.selectbox('Exercise Frequency', ['None', 'Rarely', 'Occasionally', 'Regularly'])
stress_level = st.slider('Stress Level', 0, 10, 5)

# Map 'Gender' to numerical values
gender_mapping = {'Male': 0, 'Female': 1}
gender_numeric = gender_mapping.get(gender, -1)  # Default to -1 if not found

# Map 'Exercise Frequency' to numerical values
exercise_mapping = {'None': 0, 'Rarely': 1, 'Occasionally': 2, 'Regularly': 3}
exercise_numeric = exercise_mapping.get(exercise_frequency, -1)  # Default to -1 if not found

# Make predictions based on user input
if st.button('Predict'):
    # Prepare user input as a DataFrame with the selected features
    user_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender_numeric],
        'Exercise Frequency': [exercise_numeric],
        'Stress Level': [stress_level]
    })

    # Make predictions using the trained model
    prediction = model.predict(user_data)

    # Display the prediction result
    if prediction[0] == 1:
        st.error('You may be at risk of depression. Please consult a healthcare professional.')
    else:
        st.success('You are not at risk of depression. Continue to take care of your mental health.')
