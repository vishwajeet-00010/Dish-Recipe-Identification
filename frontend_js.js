const API_URL = 'http://localhost:5000';
const MAX_FILE_SIZE = 5 * 1024 * 1024;

const uploadBtn = document.getElementById('uploadBtn');
const fileInput = document.getElementById('fileInput');
const previewSection = document.getElementById('previewSection');
const previewImage = document.getElementById('previewImage');
const analyzeBtn = document.getElementById('analyzeBtn');
const loadingSection = document.getElementById('loadingSection');
const resultsSection = document.getElementById('resultsSection');
const errorSection = document.getElementById('errorSection');
const resetBtn = document.getElementById('resetBtn');
const retryBtn = document.getElementById('retryBtn');
const getRecipeBtn = document.getElementById('getRecipeBtn');
const recipeContent = document.getElementById('recipeContent');
const recipeLoading = document.getElementById('recipeLoading');

let selectedFile = null;
let currentFood = null;
let currentIngredients = null;

uploadBtn.addEventListener('click', () => {
    fileInput.click();
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;

    if (!file.type.match('image/(png|jpeg|jpg)')) {
        showError('Please select a valid image file (JPG, PNG only)');
        return;
    }

    if (file.size > MAX_FILE_SIZE) {
        showError('File size exceeds 5MB. Please choose a smaller image.');
        return;
    }

    selectedFile = file;
    displayPreview(file);
});

function displayPreview(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImage.src = e.target.result;
        hideAll();
        previewSection.classList.remove('hidden');
    };
    reader.readAsDataURL(file);
}

analyzeBtn.addEventListener('click', async () => {
    if (!selectedFile) return;

    hideAll();
    loadingSection.classList.remove('hidden');

    try {
        const formData = new FormData();
        formData.append('image', selectedFile);

        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || 'Prediction failed');
        }

        if (data.error) {
            showError(data.message || data.error);
            return;
        }

        displayResults(data);
    } catch (error) {
        showError(`Failed to analyze image: ${error.message}`);
    }
});

function displayResults(data) {
    hideAll();

    // Store for recipe generation
    currentFood = data.food;
    currentIngredients = data.ingredients;

    document.getElementById('foodName').textContent = data.food;

    const confidencePercent = Math.round(data.confidence * 100);
    document.getElementById('confidenceFill').style.width = `${confidencePercent}%`;
    document.getElementById('confidenceText').textContent = `${confidencePercent}%`;

    const ingredientsList = document.getElementById('ingredientsList');
    ingredientsList.innerHTML = '';

    data.ingredients.forEach(ingredient => {
        const tag = document.createElement('div');
        tag.className = 'ingredient-tag';
        tag.textContent = ingredient;
        ingredientsList.appendChild(tag);
    });

    resultsSection.classList.remove('hidden');
}

function showError(message) {
    hideAll();
    document.getElementById('errorMessage').textContent = message;
    errorSection.classList.remove('hidden');
}

function hideAll() {
    previewSection.classList.add('hidden');
    loadingSection.classList.add('hidden');
    resultsSection.classList.add('hidden');
    errorSection.classList.add('hidden');
    recipeContent.classList.add('hidden'); // Hide recipe content when hiding all
    recipeLoading.classList.add('hidden'); // Hide recipe loading when hiding all
}

function resetApp() {
    selectedFile = null;
    currentFood = null;
    currentIngredients = null;
    fileInput.value = '';
    hideAll();
}

resetBtn.addEventListener('click', resetApp);
retryBtn.addEventListener('click', resetApp);

// Recipe generation
getRecipeBtn.addEventListener('click', async () => {
    if (!currentFood) return;

    try {
        recipeContent.classList.add('hidden');
        recipeLoading.classList.remove('hidden');

        const response = await fetch(`${API_URL}/recipe`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                food: currentFood,
                ingredients: currentIngredients
            })
        });

        const data = await response.json();

        recipeLoading.classList.add('hidden');

        if (response.ok && data.recipe) {
            // Format recipe with proper HTML
            const formattedRecipe = data.recipe
                .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')  // Bold text
                .replace(/\n/g, '<br>')  // Line breaks
                .replace(/(\d+\.)/g, '<br>$1');  // Number lists

            recipeContent.innerHTML = `
                <h3>📖 Recipe for ${currentFood.charAt(0).toUpperCase() + currentFood.slice(1)}</h3>
                <div style="margin-top: 15px;">${formattedRecipe}</div>
            `;
            recipeContent.classList.remove('hidden');
        } else {
            recipeContent.innerHTML = `<p style="color: #d63447;">❌ ${data.error || 'Failed to generate recipe'}</p>`;
            recipeContent.classList.remove('hidden');
        }
    } catch (error) {
        recipeLoading.classList.add('hidden');
        recipeContent.innerHTML = `<p style="color: #d63447;">❌ Error: ${error.message}</p>`;
        recipeContent.classList.remove('hidden');
    }
});

window.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (!response.ok) {
            console.warn('Backend not available');
        }
    } catch (error) {
        console.warn('Backend connection failed:', error.message);
    }
});