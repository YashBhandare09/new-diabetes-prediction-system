import pandas as pd
import streamlit as st
from joblib import load
import numpy as np
import random
from datetime import datetime, timedelta

# Load the model
model = load('random_forest_model.joblib')

# Load the existing dataset
existing_dataset_path = 'C:/Users/Yash Bhandare/.vscode/python/model code version 3/NewDiabetespatient4_data.csv'
existing_dataset = pd.read_csv(existing_dataset_path)

# Set starting Patient ID
starting_patient_id = 20000

# Fake Indian names for referred by (with prefix 'Dr') and lab
doctors = ["Dr. Gupta", "Dr. Singh", "Dr. Patel", "Dr. Kumar", "Dr. Shah", "Dr. Joshi", "Dr. Rao", "Dr. Mishra", "Dr. Reddy", "Dr. Sharma"]
labs = ["Indian Diagnostic Centre", "Sai Labs", "Ganesh Pathology Lab", "Indian Health Lab", "Mahajan Diagnostics", "Jain Lab Services", "Shree Path Lab", "Nirvana Diagnostics"]

# Function to predict diabetes class
def predict_diabetes_class(age, bmi, fbg, postprandial_glucose, hba1c, urine_microalbumin, urine_glucose, urine_ketones, lipid_profile, systolic_bp, diastolic_bp):
    user_input = [age, bmi, fbg, postprandial_glucose, hba1c, urine_microalbumin, urine_glucose, urine_ketones, lipid_profile, systolic_bp, diastolic_bp]
    prediction = model.predict([user_input])
    if prediction == 0:
        return "Non-Diabetic"
    elif prediction == 1:
        return "Diabetic"
    else:
        return "Prediabetic"

# Function to generate fake values for additional columns
def generate_fake_values():
    global starting_patient_id
    patient_id = str(starting_patient_id)
    starting_patient_id += 1
    date = datetime.now().strftime("%Y-%m-%d")
    referred_by = random.choice(doctors)
    lab = random.choice(labs)
    return patient_id, date, referred_by, lab

# Streamlit UI elements for input
st.title('Welcome to Diabetes Prediction System')

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Home", "Lab Report"])

if page == "Home":
    with st.form("Diabetes Prediction System Details"):
        name = st.text_input("Enter Your Name")
        gender = st.number_input("Gender (0: Male, 1: Female)")
        age = st.slider("Select Your Age", 0, 150)
        bmi = st.number_input("BMI")
        fbg = st.number_input("FBG")
        postprandial_glucose = st.number_input("2 Hour Postprandial Glucose")
        hba1c = st.number_input("Hba1c")
        family_history = st.number_input("Family History (1: Yes, 0: No)")
        urine_microalbumin = st.number_input("Urine Microalbumin")
        urine_glucose = st.number_input("Urine Glucose (0: Normal, 1: Abnormal)")
        urine_ketones = st.number_input("Urine Ketones (0: Normal, 1: Abnormal)")
        lipid_profile = st.number_input("Lipid Profile (0: Normal, 1: Abnormal)")
        physical_activity = st.number_input("Physical Activity (0: No, 1: Yes, 2: Someday)")
        systolic_bp = st.number_input("Systolic BP")
        diastolic_bp = st.number_input("Diastolic BP")

        submitted = st.form_submit_button("Predict")

    # Save user input and prediction result in session state
    if submitted:
        prediction_result = predict_diabetes_class(age, bmi, fbg, postprandial_glucose, hba1c, urine_microalbumin, urine_glucose, urine_ketones, lipid_profile, systolic_bp, diastolic_bp)
        st.session_state['prediction_result'] = prediction_result
        st.session_state['name'] = name
        st.session_state['age'] = age
        st.session_state['bmi'] = bmi
        st.session_state['gender'] = gender
        st.session_state['fbg'] = fbg
        st.session_state['postprandial_glucose'] = postprandial_glucose
        st.session_state['hba1c'] = hba1c
        st.session_state['urine_microalbumin'] = urine_microalbumin
        st.session_state['urine_glucose'] = urine_glucose
        st.session_state['urine_ketones'] = urine_ketones
        st.session_state['lipid_profile'] = lipid_profile
        st.session_state['systolic_bp'] = systolic_bp
        st.session_state['diastolic_bp'] = diastolic_bp



        # Generate fake values for additional columns
        patient_id, date, referred_by, lab = generate_fake_values()



        # Append user input to existing dataset
        new_row = {
            'Patient ID': patient_id,
            'Date': date,
            'Referred by': referred_by,
            'Lab': lab,
            'Name': name,
            'Age': age,
            'Gender': gender,
            'BMI': bmi,
            'FBG': fbg,
            '2 Hour Postprandial Glucose': postprandial_glucose,
            'Hba1c': hba1c,
            'Urine Microalbumin': urine_microalbumin,
            'Urine Glucose': urine_glucose,
            'Urine Ketones': urine_ketones,
            'Lipid Profile': lipid_profile,
            'Systolic BP': systolic_bp,
            'Diastolic BP': diastolic_bp,
            'Diabetes Prediction': prediction_result
        }
        existing_dataset = existing_dataset.append(new_row, ignore_index=True)
        existing_dataset.to_csv(existing_dataset_path, index=False)
