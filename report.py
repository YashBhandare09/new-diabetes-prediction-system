import streamlit as st
import random
from datetime import datetime


# Set starting Patient ID
starting_patient_id = 20000

# Fake Indian names for referred by (with prefix 'Dr') and lab
doctors = ["Dr. Gupta", "Dr. Singh", "Dr. Patel", "Dr. Kumar", "Dr. Shah", "Dr. Joshi", "Dr. Rao", "Dr. Mishra", "Dr. Reddy", "Dr. Sharma"]
labs = ["Indian Diagnostic Centre", "Sai Labs", "Ganesh Pathology Lab", "Indian Health Lab", "Mahajan Diagnostics", "Jain Lab Services", "Shree Path Lab", "Nirvana Diagnostics"]

# Function to generate fake values for additional columns
def generate_fake_values():
    global starting_patient_id
    patient_id = str(starting_patient_id)
    starting_patient_id += 1
    date = datetime.now().strftime("%Y-%m-%d")
    referred_by = random.choice(doctors)
    lab = random.choice(labs)
    return patient_id, date, referred_by, lab


# Lab report page
if 'prediction_result' in st.session_state:
    prediction_result = st.session_state['prediction_result']
    name = st.session_state['name']
    age = st.session_state['age']
    gender = st.session_state['gender']
    fbg = st.session_state['fbg']
    postprandial_glucose = st.session_state['postprandial_glucose']
    hba1c = st.session_state['hba1c']
    urine_microalbumin = st.session_state['urine_microalbumin']
    urine_glucose = st.session_state['urine_glucose']
    urine_ketones = st.session_state['urine_ketones']
    lipid_profile = st.session_state['lipid_profile']
    systolic_bp = st.session_state['systolic_bp']
    diastolic_bp = st.session_state['diastolic_bp']

    # Generate fake values for additional columns
    patient_id, date, referred_by, lab = generate_fake_values()

    st.write("# Pathology Lab Report")
    st.write("----------------------------------------------------")
    st.write(f"Patient ID: {patient_id}")
    st.write(f"Date: {date}")
    st.write(f"Referred by: {referred_by}")
    st.write(f"Lab: {lab}")
    st.write("----------------------------------------------------")
    st.write(f"Patient Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {'Male' if gender == 0 else 'Female'}")
    st.write("----------------------------------------------------")
    st.write("Test Results:")
    st.write(f"Fasting Blood Glucose: {fbg}")
    st.write(f"2 Hour Postprandial Glucose: {postprandial_glucose}")
    st.write(f"Hba1c: {hba1c}")
    st.write(f"Urine Microalbumin: {urine_microalbumin}")
    st.write(f"Urine Glucose: {'Abnormal' if urine_glucose == 1 else 'Normal'}")
    st.write(f"Urine Ketones: {'Abnormal' if urine_ketones == 1 else 'Normal'}")
    st.write(f"Lipid Profile: {'Abnormal' if lipid_profile == 1 else 'Normal'}")
    st.write(f"Systolic BP: {systolic_bp}")
    st.write(f"Diastolic BP: {diastolic_bp}")
    st.write("----------------------------------------------------")
    st.write(f"Diabetes Prediction: {prediction_result}")
