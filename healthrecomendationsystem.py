# health_recommendation.py
import streamlit as st

st.set_page_config(page_title="Health Recommendation System", page_icon="💊")

st.title(" Health Recommendation System")
st.write("Enter your details below to get personalized health recommendations:")

# User input
age = st.number_input("Age (years)", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.number_input("Weight (kg)", min_value=1, max_value=300, value=70)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active"])
goal = st.selectbox("Health Goal", ["Maintain Weight", "Lose Weight", "Gain Muscle", "Improve Fitness"])

# Calculate BMI
bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is: {bmi:.2f}")

# Recommendations
def get_recommendation(bmi, activity_level, goal):
    rec = []

    # BMI recommendations
    if bmi < 18.5:
        rec.append("You are underweight. Consider a balanced diet with more calories.")
    elif 18.5 <= bmi < 24.9:
        rec.append("You have a normal weight. Maintain your healthy lifestyle.")
    elif 25 <= bmi < 29.9:
        rec.append("You are overweight. Focus on a healthy diet and exercise.")
    else:
        rec.append("You are obese. Consult a healthcare professional and focus on weight loss.")

    # Activity recommendations
    if activity_level == "Sedentary":
        rec.append("Try to include light exercises like walking or stretching daily.")
    elif activity_level == "Light":
        rec.append("Maintain light activity, and gradually increase intensity for better health.")
    elif activity_level == "Moderate":
        rec.append("Keep your activity level consistent and include some strength training.")
    else:
        rec.append("Great! Continue your active lifestyle, but remember to rest adequately.")

    # Goal-based tips
    if goal == "Lose Weight":
        rec.append("Focus on a calorie deficit diet with regular exercise.")
    elif goal == "Gain Muscle":
        rec.append("Increase protein intake and follow a strength training routine.")
    elif goal == "Improve Fitness":
        rec.append("Include cardio, strength, and flexibility exercises in your routine.")

    return rec

if st.button("Get Recommendations"):
    recommendations = get_recommendation(bmi, activity_level, goal)
    st.subheader(" Your Recommendations:")
    for i, r in enumerate(recommendations, 1):
        st.write(f"{i}. {r}")
