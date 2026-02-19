import google.generativeai as genai
from PIL import Image
import io

class GeminiValidator:
    def __init__(self, api_key=None):
        """
        Initialize Gemini validator
        Get your FREE API key from: https://aistudio.google.com/app/apikey
        No credit card required!
        """
        self.api_key = api_key
        self.model = None
        self.model_name = None
        
        if api_key:
            try:
                genai.configure(api_key=api_key)
                
                # Use the ACTUAL working model name from API
                # Found via list_models() - this is what actually works!
                models_to_try = [
                    'models/gemini-2.5-flash',   # ✅ This one works!
                    'models/gemini-1.5-flash',   # Backup
                    'gemini-1.5-flash',          # Alternative
                ]
                
                for model_name in models_to_try:
                    try:
                        print(f"🔍 Trying: {model_name}...")
                        self.model = genai.GenerativeModel(model_name)
                        # Quick test
                        test_response = self.model.generate_content("Hi")
                        self.model_name = model_name
                        print(f"✅ Gemini working: {model_name}")
                        return  # Success! Exit early
                    except Exception as e:
                        error_msg = str(e)[:80]
                        print(f"❌ {model_name} failed: {error_msg}")
                        continue
                
                # If we get here, no models worked
                print("⚠️  No Gemini models available with this API key")
                print("ℹ️  System will work without Gemini validation")
                self.model = None
                    
            except Exception as e:
                print(f"⚠️ Gemini setup failed: {e}")
                print("ℹ️  Continuing with primary model only")
                self.model = None
        else:
            print("ℹ️  No Gemini API key. Running without validation.")
    
    def validate_food(self, image_stream, primary_prediction):
        """
        Use Gemini to validate the primary model's prediction
        Uses text-based reasoning (no image analysis)
        """
        if not self.model:
            return primary_prediction
        
        try:
            # Shorter, faster prompt
            prompt = f"""Food: {primary_prediction['food']}, Confidence: {primary_prediction['confidence']*100:.0f}%

Is this correct? Common errors: dosa→burrito, idli→muffin.

Reply ONLY:
VERDICT: CORRECT or WRONG
FOOD: [corrected name if wrong, same if correct]
CONFIDENCE: [0.0-1.0]"""

            # Generate response with timeout
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=100,  # Limit response length
                    temperature=0.3,  # More deterministic
                )
            )
            
            result = self._parse_response(response.text, primary_prediction)
            
            if result.get('corrected'):
                print(f"🤖 Gemini: {primary_prediction['food']} → {result['food']}")
            else:
                print(f"✅ Gemini: {result['food']} OK")
            
            return result
            
        except Exception as e:
            print(f"⚠️ Gemini timeout/error: {str(e)[:50]}")
            return primary_prediction
    
    def _parse_response(self, response_text, primary_prediction):
        """Parse Gemini's response"""
        try:
            lines = response_text.strip().split('\n')
            verdict = None
            confidence = None
            corrected_food = None
            
            for line in lines:
                line = line.strip()
                if 'VERDICT:' in line:
                    verdict = line.split('VERDICT:')[1].strip()
                elif 'CONFIDENCE:' in line:
                    try:
                        conf_str = line.split('CONFIDENCE:')[1].strip()
                        confidence = float(conf_str)
                    except:
                        confidence = 0.7
                elif 'FOOD:' in line or 'CORRECTED_FOOD:' in line:
                    # Handle both formats
                    if 'CORRECTED_FOOD:' in line:
                        corrected_food = line.split('CORRECTED_FOOD:')[1].strip().lower()
                    else:
                        corrected_food = line.split('FOOD:')[1].strip().lower()
            
            # If Gemini says it's correct
            if verdict and 'CORRECT' in verdict.upper():
                return {
                    'food': primary_prediction['food'],
                    'confidence': max(confidence or 0.7, primary_prediction['confidence']),
                    'ingredients': primary_prediction.get('ingredients', []),
                    'validated_by': f'gemini-{self.model_name}'
                }
            
            # If Gemini suggests correction
            if corrected_food and corrected_food != primary_prediction['food']:
                from ingredient_map import FOOD_INGREDIENTS
                ingredients = FOOD_INGREDIENTS.get(
                    corrected_food,
                    primary_prediction.get('ingredients', ['ingredients unavailable'])
                )
                
                return {
                    'food': corrected_food,
                    'confidence': confidence or 0.75,
                    'ingredients': ingredients,
                    'validated_by': f'gemini-{self.model_name}',
                    'corrected': True
                }
            
            # Default: return original
            return primary_prediction
                
        except Exception as e:
            print(f"⚠️ Parse error: {e}")
            return primary_prediction

    def generate_recipe(self, food_name, ingredients):
        """Generate cooking recipe using Gemini AI"""
        try:
            # Create recipe prompt
            ingredients_list = ', '.join(ingredients) if ingredients else 'common ingredients'
            
            prompt = f"""Create a simple, easy-to-follow recipe for {food_name}.

Ingredients: {ingredients_list}

Provide:
1. Brief description (1 line)
2. Prep time and cook time
3. Step-by-step instructions (numbered, clear, concise)
4. Serving suggestions

Keep it practical and beginner-friendly. Format nicely."""

            # Generate recipe
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=500,
                    temperature=0.7,
                )
            )
            
            return response.text
            
        except Exception as e:
            print(f"⚠️ Recipe generation error: {e}")
            return f"Unable to generate recipe for {food_name}. Please try again."
