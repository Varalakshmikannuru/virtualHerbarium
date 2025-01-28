from flask import Flask, request, jsonify, render_template
import os
import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load the saved model
model_path = "optimized_model_vgg19.h5"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")
model = tf.keras.models.load_model(model_path)

# Define the class labels
# class_labels = ["Aloevera", "Castor", "Catharanthus", "Curry", "Doddpathre"]
class_labels = ["Aloevera", "Bhrami", "Neem", "Papaya", "Tamarind"]

# Load the Excel file containing medicinal benefits and traditional uses
excel_file = 'leaves_XL.xlsx'
if not os.path.exists(excel_file):
    raise FileNotFoundError(f"Excel file not found at {excel_file}")
df = pd.read_excel(excel_file)
df.columns = df.columns.str.strip()

# Function to preprocess and predict an image
def predict_leaf(image_path):
    try:
        img = load_img(image_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        predictions = model.predict(img_array)
        confidence_score = np.max(predictions)  # Confidence score
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_labels[predicted_class_index]

        # Apply confidence threshold
        if confidence_score < 0.6:
            return "Other", confidence_score
        else:
            return predicted_class_label, confidence_score
    except Exception as e:
        raise ValueError(f"Error during prediction: {str(e)}")

def get_plant_info(label):
    plant_info = df[df['Class Label'] == label]
    if not plant_info.empty:
        medicinal_benefits = plant_info['Medicinal Benefits'].values[0]
        traditional_uses = plant_info['Traditional Uses'].values[0]
        botanical_name = plant_info['Botanical Name'].values[0]  # Extract botanical name
        habitat = plant_info['Habitat'].values[0]  # Extract habitat
        return medicinal_benefits, traditional_uses, botanical_name, habitat
    else:
        return None, None, None, None

# Fetch plant details by common name (Feature from Code 1)
@app.route('/get-leaf-details')
def get_leaf_details():
    try:
        # Get the leaf name from the query parameters
        leaf_name = request.args.get('leaf')
        
        # Filter data from the Excel sheet
        plant_info = df[df['Class Label'] == leaf_name]
        
        if not plant_info.empty:
            plant_data = plant_info.iloc[0]  # Get the first matching row
            response = {
                "class_name": plant_data['Class Label'],
                "botanical_name": plant_data['Botanical Name'],
                "traditional_uses": plant_data['Traditional Uses'],
                "medicinal_benefits": plant_data['Medicinal Benefits'],
                "habitat": plant_data['Habitat']
            }
            return jsonify(response)  # Return the response as JSON
        else:
            return jsonify({"error": f"No details found for {leaf_name}"}), 404
    except Exception as e:
        return jsonify({"error": f"Failed to fetch details: {str(e)}"}), 500


# Render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Predict the plant from an uploaded image
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            predicted_label, confidence_score = predict_leaf(filepath)
            medicinal_benefits, traditional_uses, botanical_name, habitat = get_plant_info(predicted_label)
            
            if medicinal_benefits and traditional_uses and botanical_name and habitat:
                return jsonify({
                    'label': predicted_label,
                    'confidence': f"{confidence_score:.2f}",
                    'benefits': medicinal_benefits,
                    'uses': traditional_uses,
                    'botanical_name': botanical_name,
                    'habitat': habitat
                })
            else:
                return jsonify({'error': f'No data found for {predicted_label}'}), 404
        return jsonify({'error': 'Something went wrong'}), 500
    except Exception as e:
        return jsonify({'error': f"Failed to predict: {str(e)}"}), 500

# Ensure the uploads directory exists
if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
