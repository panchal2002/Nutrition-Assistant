import requests
from bs4 import BeautifulSoup
from streamlit_lottie import st_lottie
import streamlit as st
import time


def weight_loss_calculator():
    st.title("Weight Loss Calculator")

    # Ask for user input
    gender = st.radio("Select your gender:", ("Male", "Female"))
    age = st.slider("Age:", 16, 80)
    height_cm = st.slider("Height (cm):", 100, 250)
    weight_kg = st.slider("Weight (kg):", 30, 200)
    activity_level = st.selectbox("Select your activity level:", (
        "Sedentary", "Lightly Active", "Moderately Active", "Very Active"))

    # Calculate BMR using Mifflin-St Jeor equation
    if gender == "Male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # Calculate TDEE based on activity level
    if activity_level == "Sedentary":
        tdee = bmr * 1.2
    elif activity_level == "Lightly Active":
        tdee = bmr * 1.375
    elif activity_level == "Moderately Active":
        tdee = bmr * 1.55
    else:
        tdee = bmr * 1.725

    # Calculate calorie deficit for weight loss
    calorie_deficit = st.slider(
        "Select calorie deficit for weight loss:", 250, 1000, 500)
    daily_calorie_intake = int(tdee - calorie_deficit)

    # Display daily calorie intake for weight loss
    st.info(
        f"Your daily calorie intake for weight loss is {daily_calorie_intake} calories.")


weight_loss_calculator()
