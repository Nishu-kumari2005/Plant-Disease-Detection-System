import streamlit as st
import requests
from backend.remedies import get_remedy
import base64


# -----------------------------
# SET BACKGROUND IMAGE
# -----------------------------
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()


    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)

# Call the function
set_background("assets/background1.webp")

# -----------------------------
# APP TITLE
# -----------------------------
st.title("🌱 Plant Disease Detection System")
st.write("Upload a leaf image and the model will predict the disease and suggest remedies.")

# -----------------------------
# FILE UPLOADER
# -----------------------------
uploaded_file = st.file_uploader("Upload Leaf Image", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Leaf", width=400)

    if st.button("Predict Disease"):
        with st.spinner("Predicting... 🌿"):
            try:
                # -----------------------------
                # SEND IMAGE TO FLASK BACKEND
                # -----------------------------
                response = requests.post(
                    "http://localhost:5000/predict",
                    files={"image": uploaded_file}
                )
                
                # -----------------------------
                # CHECK RESPONSE
                # -----------------------------
                if response.status_code != 200:
                    st.error("⚠️ Error from backend API!")
                else:
                    result = response.json()
                    disease = result.get("disease", "Unknown")
                    confidence = result.get("confidence", 0.0)

                    # -----------------------------
                    # GET REMEDY FROM remedies.py
                    # -----------------------------
                    remedy = get_remedy(disease)

                    # -----------------------------
                    # DISPLAY RESULTS
                    # -----------------------------
                    st.success(f"🌱 Disease: {disease}")
                    st.info(f"💯 Confidence: {confidence:.2f}%")
                    st.info(f"🛠️ Remedy: {remedy}")

            except requests.exceptions.ConnectionError:
                st.error("⚠️ Could not connect to the backend. Make sure Flask server is running on port 5000.")
