import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
import numpy as np
from PIL import Image
from ingredient_map import FOOD_INGREDIENTS
import io

class FoodClassifier:
    def __init__(self):
        print("Loading EfficientNetB0 model for better food detection...")
        self.model = EfficientNetB0(weights='imagenet', include_top=True)
        self.img_size = (224, 224)
        print("Model loaded successfully - Enhanced food recognition enabled")
    
    def preprocess_image(self, img_stream):
        img = Image.open(img_stream)
        
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        img = img.resize(self.img_size, Image.Resampling.LANCZOS)
        
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        
        return img_array
    
    def map_imagenet_to_food(self, predictions):
        decoded = decode_predictions(predictions, top=5)[0]
        
        # Debug: Print what ImageNet actually detected
        print("DEBUG - ImageNet predictions:")
        for i, (class_id, class_name, confidence) in enumerate(decoded):
            print(f"  {i+1}. {class_name}: {confidence:.3f}")
        
        # Direct ImageNet to food mappings (only high confidence)
        food_mappings = {
            'pizza': 'pizza',
            'cheeseburger': 'burger',
            'hamburger': 'burger',
            'hot_dog': 'hot dog',
            'french_loaf': 'bread',
            'bagel': 'bagel',
            'guacamole': 'guacamole',
            'mashed_potato': 'mashed potato',
            'consomme': 'soup',
            'trifle': 'dessert',
            'burrito': 'burrito',  # Keep burrito as burrito
            'plate': 'plate',
            'tray': 'tray',
            # Asian food mappings
            'hot_pot': 'ramen',  # Hot pot often contains ramen
            'soup_bowl': 'ramen',  # Soup bowls with noodles = ramen
            'carbonara': 'pasta',
            'wok': 'stir fry',
        }
        
        # FIRST: Check direct mappings (highest priority)
        # This ensures cheeseburger→burger, hot_pot→ramen, etc.
        for pred in decoded:
            class_id, class_name, confidence = pred
            
            if class_name in food_mappings:
                mapped_food = food_mappings[class_name]
                if mapped_food in FOOD_INGREDIENTS:
                    return mapped_food, float(confidence), FOOD_INGREDIENTS[mapped_food]
        
        # SECOND: Check exact matches in our ingredient database
        for pred in decoded:
            class_id, class_name, confidence = pred
            class_name_lower = class_name.lower().replace('_', ' ')
            
            # Direct exact match in FOOD_INGREDIENTS
            for food_name in FOOD_INGREDIENTS.keys():
                if food_name.lower() == class_name_lower:
                    return food_name, float(confidence), FOOD_INGREDIENTS[food_name]
        
        # Third: Keyword search in class names
        for pred in decoded:
            class_id, class_name, confidence = pred
            class_name_lower = class_name.lower().replace('_', ' ')
            
            # Common food keywords - ORDER MATTERS! Specific foods first, generic last
            keywords = {
                # Specific dishes first
                'ramen': 'ramen',
                'pho': 'pho',
                'udon': 'udon',
                'soba': 'soba',
                'spaghetti': 'spaghetti',
                'fettuccine': 'fettuccine',
                'pizza': 'pizza',
                'sushi': 'sushi',
                'burger': 'burger',
                'sandwich': 'sandwich',
                'burrito': 'burrito',
                'taco': 'tacos',
                'biryani': 'biryani',
                'curry': 'curry',
                'salad': 'salad',
                'steak': 'steak',
                'cake': 'cake',
                # Generic categories last
                'noodle': 'ramen',  # Default noodles to ramen
                'pasta': 'pasta',
                'soup': 'soup',  # Very generic, check last
                'rice': 'fried rice',
                'chicken': 'chicken',
                'fish': 'fish',
                'bread': 'bread',
                'ice_cream': 'ice cream',
                'coffee': 'espresso',
            }
            
            for keyword, food_name in keywords.items():
                if keyword in class_name_lower:
                    if food_name in FOOD_INGREDIENTS:
                        return food_name, float(confidence), FOOD_INGREDIENTS[food_name]
        
        # If nothing found, return unknown
        top_pred = decoded[0]
        return 'unknown food', float(top_pred[2]), ['ingredients unavailable']
    
    def predict(self, img_stream):
        img_array = self.preprocess_image(img_stream)
        
        predictions = self.model.predict(img_array, verbose=0)
        
        food_name, confidence, ingredients = self.map_imagenet_to_food(predictions)
        
        return {
            'food': food_name,
            'confidence': confidence,
            'ingredients': ingredients
        }