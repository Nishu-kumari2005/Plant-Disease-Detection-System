# remedies.py
# ============================
# Plant Disease Remedies Module
# ============================

REMEDIES = {
    "Apple___Apple_scab": "Use fungicides like captan or mancozeb. Remove infected leaves and maintain good air circulation.",
    "Apple___Black_rot": "Remove infected fruits and branches, apply copper-based sprays regularly, and prune trees for better airflow.",
    "Apple___Cedar_apple_rust": "Remove nearby juniper plants, apply fungicides preventively, and monitor for early signs.",
    "Apple___healthy": "No treatment needed. Maintain regular care and monitor for disease.",
    "Blueberry___healthy": "No treatment needed. Maintain proper irrigation and pruning.",
    "Cherry_(including_sour)___Powdery_mildew": "Apply sulfur-based fungicides, prune affected shoots, and ensure proper spacing.",
    "Cherry_(including_sour)___healthy": "No treatment needed. Maintain healthy practices.",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "Use resistant varieties, rotate crops, and apply fungicides when needed.",
    "Corn_(maize)___Common_rust_": "Plant resistant hybrids, remove infected residue, and apply rust fungicides.",
    "Corn_(maize)___Northern_Leaf_Blight": "Use resistant seeds, crop rotation, and foliar fungicides at early stages.",
    "Corn_(maize)___healthy": "No treatment needed. Keep field clean and monitor regularly.",
    "Grape___Black_rot": "Remove infected leaves and berries, apply fungicides, and prune to improve air circulation.",
    "Grape___Esca_(Black_Measles)": "Remove infected wood, disinfect pruning tools, and use fungicides preventively.",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "Remove affected leaves, apply copper or systemic fungicides, and ensure good airflow.",
    "Grape___healthy": "No treatment needed. Maintain good irrigation and pruning.",
    "Orange___Haunglongbing_(Citrus_greening)": "Remove infected trees, control psyllid vectors, and use certified disease-free plants.",
    "Peach___Bacterial_spot": "Remove infected leaves, apply copper-based sprays, and prune trees to improve air circulation.",
    "Peach___healthy": "No treatment needed. Keep trees healthy with proper irrigation and fertilization.",
    "Pepper,_bell___Bacterial_spot": "Remove infected plants, rotate crops, and use copper sprays preventively.",
    "Pepper,_bell___healthy": "No treatment needed. Maintain good soil and monitor regularly.",
    "Potato___Early_blight": "Use fungicides like chlorothalonil, rotate crops, and remove infected foliage.",
    "Potato___Late_blight": "Apply systemic fungicides, remove infected plants promptly, and avoid overhead irrigation.",
    "Potato___healthy": "No treatment needed. Maintain proper irrigation and crop hygiene.",
    "Raspberry___healthy": "No treatment needed. Keep plants healthy and monitor for pests.",
    "Soybean___healthy": "No treatment needed. Rotate crops and maintain proper fertilization.",
    "Squash___Powdery_mildew": "Apply sulfur or potassium bicarbonate sprays, ensure airflow, and remove infected leaves.",
    "Strawberry___Leaf_scorch": "Remove infected leaves, apply copper fungicides, and maintain good irrigation practices.",
    "Strawberry___healthy": "No treatment needed. Keep plants healthy and weed-free.",
    "Tomato___Bacterial_spot": "Remove infected leaves, apply copper sprays, and avoid overhead watering.",
    "Tomato___Early_blight": "Use fungicides like chlorothalonil, rotate crops, and remove infected foliage.",
    "Tomato___Late_blight": "Apply systemic fungicides like metalaxyl, remove infected plants, and avoid overhead irrigation.",
    "Tomato___Leaf_Mold": "Use fungicide sprays, improve ventilation, and reduce humidity.",
    "Tomato___Septoria_leaf_spot": "Remove affected leaves, use fungicides, and maintain crop rotation.",
    "Tomato___Spider_mites Two-spotted_spider_mite": "Use miticides, release natural predators like ladybugs, and reduce dust.",
    "Tomato___Target_Spot": "Remove infected leaves, apply fungicides, and rotate crops.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Control whitefly vectors, remove infected plants, and use resistant varieties.",
    "Tomato___Tomato_mosaic_virus": "Use virus-free seeds, disinfect tools, and remove infected plants.",
    "Tomato___healthy": "No treatment needed. Maintain proper watering and monitor regularly."
}

def get_remedy(disease_name):
    """
    Returns the remedy for a given disease.
    If disease is not found, returns a default message.
    """
    return REMEDIES.get(disease_name, "Consult agriculture expert for advice.")
