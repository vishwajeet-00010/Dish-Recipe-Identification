from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import io
from PIL import Image
from backend_model import FoodClassifier
from groq_validator import GroqValidator

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILE_SIZE = 5 * 1024 * 1024 # 5MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize the food classifier
classifier = FoodClassifier()

# Initialize Groq validator (MUCH faster than Gemini!)
GROQ_API_KEY = "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"
groq_validator = GroqValidator(api_key=GROQ_API_KEY)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_image(file_stream):
    try:
        img = Image.open(file_stream)
        img.verify()
        file_stream.seek(0)
        return True
    except:
        return False

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'model_loaded': classifier.model is not None})

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Only jpg, jpeg, png allowed'}), 400
    
    file_bytes = file.read()
    
    if len(file_bytes) > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large. Max 5MB'}), 400
    
    file_stream = io.BytesIO(file_bytes)
    
    if not validate_image(file_stream):
        return jsonify({'error': 'Invalid or corrupted image'}), 400
    
    file_stream.seek(0)
    
    try:
        # Step 1: Primary model prediction
        result = classifier.predict(file_stream)
        
        print(f"🔍 Primary Model: {result['food']} ({result['confidence']*100:.1f}%)")
        
        # Step 2: Groq validation (if available and confidence is low)
        if groq_validator.client and result['confidence'] < 0.7:
            print("🤖 Low confidence - asking Groq for validation...")
            file_stream.seek(0)  # Reset stream
            result = groq_validator.validate_food(file_stream, result)
            
            if result.get('corrected'):
                print(f"✅ Groq corrected: {result['food']} ({result['confidence']*100:.1f}%)")
        
        # Step 3: Return result
        return jsonify(result), 200
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

@app.route('/recipe', methods=['POST'])
def get_recipe():
    """Generate recipe for detected food using recipe database"""
    try:
        data = request.get_json()
        food_name = data.get('food')
        
        if not food_name:
            return jsonify({'error': 'No food name provided'}), 400
        
        # Use recipe database (fast and reliable!)
        from recipe_database import get_recipe as get_recipe_from_db
        recipe = get_recipe_from_db(food_name)
        
        return jsonify({'recipe': recipe}), 200
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({'error': f'Recipe generation failed: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting Food Ingredient Detection API...")
    print("Model loading...")
    app.run(host='0.0.0.0', port=5000, debug=False)
