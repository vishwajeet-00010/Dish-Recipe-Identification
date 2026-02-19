"""
Recipe database with pre-defined recipes for common foods
"""

RECIPES = {
    'pizza': {
        'name': 'Classic Pizza',
        'prep_time': '20 minutes',
        'cook_time': '15 minutes',
        'servings': '4',
        'description': 'A delicious homemade pizza with crispy crust and flavorful toppings.',
        'instructions': [
            'Preheat oven to 475°F (245°C)',
            'Roll out pizza dough on a floured surface to desired thickness',
            'Transfer dough to a pizza pan or baking sheet',
            'Spread tomato sauce evenly over the dough, leaving a small border',
            'Sprinkle mozzarella cheese generously over the sauce',
            'Add your favorite toppings (pepperoni, vegetables, etc.)',
            'Drizzle with olive oil and season with salt, pepper, and dried basil',
            'Bake for 12-15 minutes until crust is golden and cheese is bubbly',
            'Let cool for 2-3 minutes before slicing',
            'Serve hot and enjoy!'
        ]
    },
    'burger': {
        'name': 'Classic Beef Burger',
        'prep_time': '15 minutes',
        'cook_time': '10 minutes',
        'servings': '4',
        'description': 'Juicy homemade beef burgers with all the fixings.',
        'instructions': [
            'Mix ground beef with salt, pepper, and your favorite seasonings',
            'Form into 4 equal patties, slightly larger than your buns',
            'Make a small indent in the center of each patty to prevent puffing',
            'Heat a grill or skillet over medium-high heat',
            'Cook patties for 4-5 minutes per side for medium doneness',
            'Add cheese in the last minute if desired',
            'Toast burger buns lightly on the grill',
            'Assemble: bottom bun, lettuce, tomato, patty, onion, pickles, top bun',
            'Add ketchup, mustard, or mayo to taste',
            'Serve immediately with fries or salad'
        ]
    },
    'ramen': {
        'name': 'Simple Ramen Bowl',
        'prep_time': '10 minutes',
        'cook_time': '15 minutes',
        'servings': '2',
        'description': 'A comforting bowl of ramen with rich broth and toppings.',
        'instructions': [
            'Bring 4 cups of water to a boil in a large pot',
            'Add ramen noodles and cook according to package directions',
            'In a separate pot, heat broth (chicken, pork, or vegetable)',
            'Add soy sauce, miso paste, and a splash of sesame oil to broth',
            'Drain noodles and divide between bowls',
            'Pour hot broth over noodles',
            'Top with sliced boiled egg, green onions, and seaweed',
            'Add optional toppings: corn, mushrooms, bamboo shoots',
            'Drizzle with chili oil if you like it spicy',
            'Serve immediately while hot'
        ]
    },
    'pasta': {
        'name': 'Classic Pasta',
        'prep_time': '10 minutes',
        'cook_time': '15 minutes',
        'servings': '4',
        'description': 'Simple and delicious pasta with your choice of sauce.',
        'instructions': [
            'Bring a large pot of salted water to a rolling boil',
            'Add pasta and cook according to package directions (usually 8-12 minutes)',
            'While pasta cooks, heat your favorite sauce in a pan',
            'Reserve 1 cup of pasta water before draining',
            'Drain pasta and add to the sauce pan',
            'Toss pasta with sauce, adding pasta water if needed for consistency',
            'Add grated Parmesan cheese and fresh basil',
            'Season with salt, pepper, and red pepper flakes to taste',
            'Drizzle with olive oil for extra richness',
            'Serve hot with garlic bread'
        ]
    },
    'spaghetti': {
        'name': 'Spaghetti with Marinara',
        'prep_time': '10 minutes',
        'cook_time': '20 minutes',
        'servings': '4',
        'description': 'Classic spaghetti with homemade marinara sauce.',
        'instructions': [
            'Bring a large pot of salted water to boil',
            'Add spaghetti and cook for 8-10 minutes until al dente',
            'Heat olive oil in a pan, sauté minced garlic until fragrant',
            'Add crushed tomatoes, salt, pepper, and Italian herbs',
            'Simmer sauce for 15 minutes, stirring occasionally',
            'Drain spaghetti, reserving 1 cup pasta water',
            'Toss spaghetti with marinara sauce',
            'Add pasta water if sauce is too thick',
            'Top with fresh basil and grated Parmesan',
            'Serve hot with garlic bread'
        ]
    },
    'sushi': {
        'name': 'Homemade Sushi Rolls',
        'prep_time': '30 minutes',
        'cook_time': '20 minutes',
        'servings': '4',
        'description': 'Fresh and delicious homemade sushi rolls.',
        'instructions': [
            'Cook sushi rice according to package directions',
            'Mix rice vinegar, sugar, and salt; fold into cooked rice',
            'Let rice cool to room temperature',
            'Place nori sheet shiny-side down on bamboo mat',
            'Spread thin layer of rice on nori, leaving 1 inch at top',
            'Add your fillings in a line: fish, avocado, cucumber',
            'Roll tightly using the bamboo mat, applying gentle pressure',
            'Seal the edge with a bit of water',
            'Cut roll into 6-8 pieces with a sharp, wet knife',
            'Serve with soy sauce, wasabi, and pickled ginger'
        ]
    },
    'cake': {
        'name': 'Simple Vanilla Cake',
        'prep_time': '20 minutes',
        'cook_time': '30 minutes',
        'servings': '8',
        'description': 'A moist and fluffy vanilla cake perfect for any occasion.',
        'instructions': [
            'Preheat oven to 350°F (175°C) and grease a 9-inch cake pan',
            'Mix flour, baking powder, and salt in a bowl',
            'In another bowl, cream butter and sugar until fluffy',
            'Beat in eggs one at a time, then add vanilla extract',
            'Alternately add dry ingredients and milk to butter mixture',
            'Pour batter into prepared pan and smooth the top',
            'Bake for 25-30 minutes until a toothpick comes out clean',
            'Cool in pan for 10 minutes, then turn out onto a wire rack',
            'Let cool completely before frosting',
            'Frost with your favorite frosting and decorate as desired'
        ]
    },
    'tacos': {
        'name': 'Beef Tacos',
        'prep_time': '15 minutes',
        'cook_time': '15 minutes',
        'servings': '4',
        'description': 'Flavorful beef tacos with fresh toppings.',
        'instructions': [
            'Brown ground beef in a skillet over medium-high heat',
            'Drain excess fat and add taco seasoning with water',
            'Simmer for 5 minutes until sauce thickens',
            'Warm taco shells in the oven or microwave',
            'Fill shells with seasoned beef',
            'Top with shredded lettuce, diced tomatoes, and cheese',
            'Add sour cream, salsa, and guacamole',
            'Garnish with cilantro and lime wedges',
            'Serve immediately while warm',
            'Enjoy with Mexican rice and beans'
        ]
    },
    'burrito': {
        'name': 'Chicken Burrito',
        'prep_time': '20 minutes',
        'cook_time': '15 minutes',
        'servings': '4',
        'description': 'Hearty chicken burritos packed with flavor.',
        'instructions': [
            'Cook seasoned chicken breast and slice into strips',
            'Warm large flour tortillas',
            'Layer rice, beans, and chicken in center of tortilla',
            'Add cheese, lettuce, tomatoes, and sour cream',
            'Fold in sides of tortilla, then roll tightly from bottom',
            'Optional: grill burrito seam-side down for crispy exterior',
            'Cut in half diagonally',
            'Serve with salsa, guacamole, and chips',
            'Can be wrapped in foil for easy eating',
            'Store leftovers wrapped in refrigerator'
        ]
    },
    'sandwich': {
        'name': 'Classic Sandwich',
        'prep_time': '10 minutes',
        'cook_time': '0 minutes',
        'servings': '1',
        'description': 'A simple and satisfying sandwich.',
        'instructions': [
            'Choose your favorite bread (white, wheat, or sourdough)',
            'Spread mayo, mustard, or butter on both slices',
            'Layer your choice of deli meat (turkey, ham, or roast beef)',
            'Add cheese slices (cheddar, Swiss, or provolone)',
            'Top with fresh lettuce, tomato slices, and onion',
            'Add pickles, peppers, or other favorite toppings',
            'Season with salt, pepper, and oregano if desired',
            'Place top slice of bread',
            'Cut diagonally for easier eating',
            'Serve with chips or a side salad'
        ]
    },
    'salad': {
        'name': 'Fresh Garden Salad',
        'prep_time': '15 minutes',
        'cook_time': '0 minutes',
        'servings': '4',
        'description': 'Crisp and refreshing garden salad.',
        'instructions': [
            'Wash and dry mixed greens (lettuce, spinach, arugula)',
            'Chop vegetables: tomatoes, cucumbers, bell peppers',
            'Slice red onion thinly',
            'Add shredded carrots and radishes',
            'Toss all vegetables in a large bowl',
            'Add croutons, nuts, or seeds for crunch',
            'Drizzle with your favorite dressing',
            'Toss gently to coat evenly',
            'Top with grated cheese if desired',
            'Serve immediately while fresh and crisp'
        ]
    },
    'soup': {
        'name': 'Vegetable Soup',
        'prep_time': '15 minutes',
        'cook_time': '30 minutes',
        'servings': '6',
        'description': 'Hearty and healthy vegetable soup.',
        'instructions': [
            'Heat olive oil in a large pot over medium heat',
            'Sauté diced onions, carrots, and celery until soft',
            'Add minced garlic and cook for 1 minute',
            'Pour in vegetable or chicken broth',
            'Add diced tomatoes, potatoes, and green beans',
            'Season with salt, pepper, thyme, and bay leaves',
            'Bring to a boil, then reduce heat and simmer for 20 minutes',
            'Add any quick-cooking vegetables in last 5 minutes',
            'Taste and adjust seasonings',
            'Serve hot with crusty bread'
        ]
    },
    'steak': {
        'name': 'Pan-Seared Steak',
        'prep_time': '5 minutes',
        'cook_time': '10 minutes',
        'servings': '2',
        'description': 'Perfectly cooked steak with a golden crust.',
        'instructions': [
            'Remove steak from refrigerator 30 minutes before cooking',
            'Pat steak dry and season generously with salt and pepper',
            'Heat a cast-iron skillet over high heat until very hot',
            'Add a small amount of oil to the pan',
            'Place steak in pan and don\'t move it for 3-4 minutes',
            'Flip steak and cook another 3-4 minutes for medium-rare',
            'Add butter, garlic, and herbs in last minute, baste steak',
            'Remove from heat and let rest for 5 minutes',
            'Slice against the grain',
            'Serve with your favorite sides'
        ]
    },
    'chicken': {
        'name': 'Roasted Chicken',
        'prep_time': '15 minutes',
        'cook_time': '1 hour',
        'servings': '4',
        'description': 'Juicy roasted chicken with crispy skin.',
        'instructions': [
            'Preheat oven to 425°F (220°C)',
            'Pat chicken dry inside and out',
            'Rub chicken with olive oil, salt, pepper, and herbs',
            'Stuff cavity with lemon, garlic, and fresh herbs',
            'Tie legs together with kitchen twine',
            'Place chicken breast-side up in roasting pan',
            'Roast for 15 minutes, then reduce heat to 375°F',
            'Continue roasting for 45 minutes until internal temp reaches 165°F',
            'Let rest for 10 minutes before carving',
            'Serve with roasted vegetables'
        ]
    },
    'fish': {
        'name': 'Baked Fish Fillet',
        'prep_time': '10 minutes',
        'cook_time': '15 minutes',
        'servings': '2',
        'description': 'Light and flaky baked fish.',
        'instructions': [
            'Preheat oven to 400°F (200°C)',
            'Pat fish fillets dry with paper towels',
            'Place fish in a greased baking dish',
            'Drizzle with olive oil and lemon juice',
            'Season with salt, pepper, and herbs',
            'Top with thin lemon slices',
            'Bake for 12-15 minutes until fish flakes easily',
            'Fish is done when it reaches 145°F internal temperature',
            'Garnish with fresh parsley',
            'Serve with rice and steamed vegetables'
        ]
    },
    'rice': {
        'name': 'Perfect White Rice',
        'prep_time': '5 minutes',
        'cook_time': '20 minutes',
        'servings': '4',
        'description': 'Fluffy and perfectly cooked white rice.',
        'instructions': [
            'Rinse rice in cold water until water runs clear',
            'Combine 1 cup rice with 2 cups water in a pot',
            'Add a pinch of salt',
            'Bring to a boil over high heat',
            'Reduce heat to low, cover with tight-fitting lid',
            'Simmer for 18 minutes without lifting lid',
            'Remove from heat and let stand covered for 5 minutes',
            'Fluff with a fork',
            'Serve as a side dish or base for stir-fries',
            'Store leftovers in refrigerator for up to 3 days'
        ]
    },
    'fried rice': {
        'name': 'Vegetable Fried Rice',
        'prep_time': '15 minutes',
        'cook_time': '10 minutes',
        'servings': '4',
        'description': 'Quick and flavorful fried rice.',
        'instructions': [
            'Use day-old cooked rice (freshly cooked rice is too moist)',
            'Heat oil in a large wok or skillet over high heat',
            'Add beaten eggs and scramble, then set aside',
            'Stir-fry diced vegetables (carrots, peas, corn)',
            'Add rice and break up any clumps',
            'Stir-fry for 3-4 minutes until rice is heated through',
            'Add soy sauce, sesame oil, and white pepper',
            'Mix in scrambled eggs',
            'Garnish with green onions',
            'Serve hot as a main dish or side'
        ]
    },
    'bread': {
        'name': 'Simple Homemade Bread',
        'prep_time': '2 hours',
        'cook_time': '30 minutes',
        'servings': '1 loaf',
        'description': 'Fresh homemade bread with a crispy crust.',
        'instructions': [
            'Mix warm water, yeast, and sugar; let sit 5 minutes until foamy',
            'Add flour, salt, and oil to yeast mixture',
            'Knead dough for 8-10 minutes until smooth and elastic',
            'Place in greased bowl, cover, and let rise 1 hour',
            'Punch down dough and shape into a loaf',
            'Place in greased loaf pan, let rise 30 minutes',
            'Preheat oven to 375°F (190°C)',
            'Bake for 30-35 minutes until golden brown',
            'Bread should sound hollow when tapped',
            'Cool on wire rack before slicing'
        ]
    },
    'ice cream': {
        'name': 'Vanilla Ice Cream',
        'prep_time': '30 minutes',
        'cook_time': '4 hours freezing',
        'servings': '8',
        'description': 'Creamy homemade vanilla ice cream.',
        'instructions': [
            'Whisk together cream, milk, sugar, and vanilla extract',
            'Pour mixture into ice cream maker',
            'Churn according to manufacturer\'s instructions (about 20 minutes)',
            'Ice cream will be soft-serve consistency',
            'Transfer to freezer-safe container',
            'Freeze for at least 4 hours until firm',
            'Let sit at room temperature 5 minutes before scooping',
            'Scoop into bowls or cones',
            'Top with your favorite toppings',
            'Store in freezer for up to 2 weeks'
        ]
    },
    'dessert': {
        'name': 'Simple Dessert',
        'prep_time': '15 minutes',
        'cook_time': '25 minutes',
        'servings': '6',
        'description': 'A sweet treat to end your meal.',
        'instructions': [
            'Preheat oven to 350°F (175°C)',
            'Prepare your chosen dessert base (cake, cookies, or brownies)',
            'Mix wet and dry ingredients separately, then combine',
            'Pour or scoop into prepared baking dish or pan',
            'Bake according to recipe time',
            'Test for doneness with a toothpick',
            'Cool completely before serving',
            'Add frosting, glaze, or toppings as desired',
            'Cut into portions',
            'Serve with ice cream or whipped cream'
        ]
    },
    'dosa': {
        'name': 'South Indian Dosa',
        'prep_time': '8 hours soaking',
        'cook_time': '20 minutes',
        'servings': '6',
        'description': 'Crispy fermented rice and lentil crepes.',
        'instructions': [
            'Soak rice and lentils separately for 6-8 hours',
            'Grind into a smooth batter, adding water as needed',
            'Ferment batter overnight in a warm place',
            'Heat a non-stick griddle or tawa over medium heat',
            'Pour a ladleful of batter in the center',
            'Spread in a circular motion to make a thin crepe',
            'Drizzle oil around the edges',
            'Cook until bottom is golden and crispy',
            'Fold in half or roll',
            'Serve hot with sambar and coconut chutney'
        ]
    },
    'idli': {
        'name': 'Soft Idli',
        'prep_time': '8 hours soaking',
        'cook_time': '15 minutes',
        'servings': '12 idlis',
        'description': 'Steamed rice cakes, soft and fluffy.',
        'instructions': [
            'Soak rice and urad dal separately for 6-8 hours',
            'Grind into smooth batters separately',
            'Mix batters together with salt',
            'Ferment overnight until doubled in volume',
            'Grease idli molds with oil',
            'Pour batter into molds, filling 3/4 full',
            'Steam in idli steamer for 10-12 minutes',
            'Test with a toothpick - it should come out clean',
            'Let cool for 2 minutes before removing from molds',
            'Serve hot with sambar and chutney'
        ]
    },
    'samosa': {
        'name': 'Potato Samosa',
        'prep_time': '30 minutes',
        'cook_time': '20 minutes',
        'servings': '12 samosas',
        'description': 'Crispy fried pastries filled with spiced potatoes.',
        'instructions': [
            'Make dough with flour, oil, and water; rest for 30 minutes',
            'Boil and mash potatoes, mix with peas and spices',
            'Roll dough into thin circles, cut in half',
            'Form each half into a cone shape',
            'Fill with potato mixture, seal edges with water',
            'Heat oil for deep frying to 350°F',
            'Fry samosas until golden brown on all sides',
            'Drain on paper towels',
            'Serve hot with mint chutney and tamarind sauce',
            'Can be baked at 400°F for healthier option'
        ]
    },
    'biryani': {
        'name': 'Chicken Biryani',
        'prep_time': '45 minutes',
        'cook_time': '1 hour',
        'servings': '6',
        'description': 'Aromatic rice dish with spiced chicken.',
        'instructions': [
            'Marinate chicken with yogurt, spices, and herbs for 30 minutes',
            'Soak basmati rice for 30 minutes, then parboil',
            'Fry sliced onions until golden brown',
            'Layer marinated chicken in a heavy-bottomed pot',
            'Top with parboiled rice',
            'Sprinkle fried onions, saffron milk, and ghee',
            'Cover pot tightly with foil and lid',
            'Cook on low heat for 45 minutes (dum cooking)',
            'Let rest for 5 minutes before opening',
            'Serve with raita and salad'
        ]
    },
    'curry': {
        'name': 'Chicken Curry',
        'prep_time': '20 minutes',
        'cook_time': '40 minutes',
        'servings': '4',
        'description': 'Rich and flavorful chicken curry.',
        'instructions': [
            'Heat oil in a large pot, add cumin seeds',
            'Sauté onions until golden brown',
            'Add ginger-garlic paste, cook for 2 minutes',
            'Add tomatoes and cook until soft',
            'Mix in curry powder, turmeric, and chili powder',
            'Add chicken pieces and brown on all sides',
            'Pour in coconut milk or water',
            'Simmer covered for 25-30 minutes until chicken is cooked',
            'Garnish with fresh cilantro',
            'Serve with rice or naan bread'
        ]
    },
    'default': {
        'name': 'Basic Cooking Instructions',
        'prep_time': 'Varies',
        'cook_time': 'Varies',
        'servings': 'Varies',
        'description': 'General cooking guidelines for this dish.',
        'instructions': [
            'Gather all necessary ingredients and equipment',
            'Prepare ingredients by washing, chopping, and measuring',
            'Follow standard cooking techniques for this type of dish',
            'Cook at appropriate temperature and time',
            'Season to taste with salt, pepper, and herbs',
            'Check for doneness before serving',
            'Plate attractively and serve hot',
            'Store leftovers properly in the refrigerator'
        ]
    }
}

def get_recipe(food_name):
    """Get recipe for a food item"""
    # Normalize food name
    food_key = food_name.lower().strip()
    
    # Try exact match
    if food_key in RECIPES:
        return format_recipe(RECIPES[food_key])
    
    # Try partial match
    for key in RECIPES.keys():
        if key in food_key or food_key in key:
            return format_recipe(RECIPES[key])
    
    # Return default recipe
    recipe = RECIPES['default'].copy()
    recipe['name'] = f'Cooking {food_name.title()}'
    return format_recipe(recipe)

def format_recipe(recipe_data):
    """Format recipe data into readable text"""
    output = []
    output.append(f"**{recipe_data['name']}**\n")
    output.append(recipe_data['description'])
    output.append(f"\n⏱️ Prep Time: {recipe_data['prep_time']}")
    output.append(f"🔥 Cook Time: {recipe_data['cook_time']}")
    output.append(f"🍽️ Servings: {recipe_data['servings']}\n")
    output.append("**Instructions:**")
    
    for i, step in enumerate(recipe_data['instructions'], 1):
        output.append(f"{i}. {step}")
    
    output.append("\n✨ Enjoy your homemade meal!")
    
    return '\n'.join(output)
