🌱 AI-Based Plant Disease Diagnosis System
📌 Project Overview

The AI-Based Plant Disease Diagnosis System is a machine learning–powered web application designed to identify plant diseases from leaf images. Farmers or users can upload images of plant leaves, and the system predicts the disease and provides basic remedy suggestions.

This project leverages Deep Learning (CNN) techniques using MobileNetV2 for efficient and accurate disease classification. To improve transparency and trust, Grad-CAM visualization is integrated to highlight the affected regions of the leaf used by the model during prediction.

🎯 Objectives

Detect plant diseases accurately using leaf images

Assist farmers with early disease identification

Provide an easy-to-use web-based interface

Improve model interpretability using Grad-CAM

Enable real-world deployment using a lightweight deep learning model

🧠 Technologies Used
Machine Learning & AI

TensorFlow / Keras

MobileNetV2 (Transfer Learning)

Grad-CAM (Explainable AI)

NumPy, Pillow

Backend

Flask (REST API)

Python

Frontend

Streamlit

Dataset

PlantVillage Dataset

📂 Project Structure
plant_disease_detection/
│
├── dataset/
│   ├── train/
│   └── valid/
│
├── model/
│   └── plant_disease_model.h5
│
├── backend/
│   ├── app.py
│   ├── remedies.py
│   └── gradcam.py
│
├── training/
│   └── train_model.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md

📊 Features

Upload plant leaf images

Disease prediction with confidence score

Grad-CAM heatmap visualization

Fast inference using MobileNetV2

User-friendly interface

📈 Future Enhancements

Mobile application support

Multilingual interface for farmers

Offline prediction support

Integration with weather and soil data

Detailed treatment and pesticide recommendations

🧪 Results

High accuracy on test dataset

Efficient performance on low-resource systems

Improved interpretability using Grad-CAM

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project with proper attribution.

👩‍💻 Author

Nishu Kumari
Computer Science Student
AI / ML | Web Development | Data Science

AI-Based Plant Disease Diagnosis System 
