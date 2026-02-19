"""
Groq AI validator for food detection
Much faster and more reliable than Gemini!
"""
from groq import Groq

class GroqValidator:
    def __init__(self, api_key=None):
        """
        Initialize Groq validator
        Free tier: 14,400 requests/day (10x more than Gemini!)
        """
        self.api_key = api_key
        self.client = None
        
        if api_key:
            try:
                self.client = Groq(api_key=api_key)
                print("✅ Groq AI initialized! (Ultra-fast validation enabled)")
            except Exception as e:
                print(f"⚠️ Groq initialization failed: {e}")
                self.client = None
        else:
            print("ℹ️ No Groq API key. Running without AI validation.")
    
    def validate_food(self, image_stream, primary_prediction):
        """
        Use Groq to validate the primary model's prediction
        MUCH faster than Gemini (< 1 second vs 3-5 seconds)
        """
        if not self.client:
            return primary_prediction
        
        try:
            # Create validation prompt
            prompt = f"""You are a food recognition expert. A computer vision model detected:

Food: {primary_prediction['food']}
Confidence: {primary_prediction['confidence']*100:.0f}%

Common errors: dosa→burrito, idli→muffin, vada→donut

Is this correct? Reply ONLY in this format:
VERDICT: CORRECT or WRONG
FOOD: [corrected name if wrong, same if correct]
CONFIDENCE: [0.0-1.0]"""

            # Call Groq API (blazing fast!)
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Fast and accurate
                messages=[
                    {"role": "system", "content": "You are a food recognition expert. Be concise."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100,
                temperature=0.3
            )
            
            result = self._parse_response(response.choices[0].message.content, primary_prediction)
            
            if result.get('corrected'):
                print(f"🤖 Groq: {primary_prediction['food']} → {result['food']}")
            else:
                print(f"✅ Groq: {result['food']} OK")
            
            return result
            
        except Exception as e:
            print(f"⚠️ Groq error: {str(e)[:50]}")
            return primary_prediction
    
    def _parse_response(self, response_text, primary_prediction):
        """Parse Groq's response"""
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
                elif 'FOOD:' in line:
                    corrected_food = line.split('FOOD:')[1].strip().lower()
            
            # If Groq says it's correct
            if verdict and 'CORRECT' in verdict.upper():
                return {
                    'food': primary_prediction['food'],
                    'confidence': max(confidence or 0.7, primary_prediction['confidence']),
                    'ingredients': primary_prediction.get('ingredients', []),
                    'validated_by': 'groq-ai'
                }
            
            # If Groq suggests correction
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
                    'validated_by': 'groq-ai',
                    'corrected': True
                }
            
            # Default: return original
            return primary_prediction
                
        except Exception as e:
            print(f"⚠️ Parse error: {e}")
            return primary_prediction
