from flask import Flask, jsonify, render_template, request
import requests
import markdown
import easyocr
import cv2
import numpy as np
import base64
import re

app = Flask(__name__)

# Global EasyOCR reader
reader = None

def initialize_ocr():
    """Initialize the EasyOCR reader."""
    global reader
    if reader is None:
        # Create reader for English and Turkish
        reader = easyocr.Reader(['en', 'tr'])
    return reader

def preprocess_image(image):
    """Prepare the image for OCR."""
    # Convert to OpenCV format
    if isinstance(image, str) and image.startswith('data:image'):
        # Handle base64 encoded images
        image = re.sub('^data:image/.+;base64,', '', image)
        image = base64.b64decode(image)
    
    nparr = np.frombuffer(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Reduce noise
    denoised = cv2.fastNlMeansDenoising(gray)
    
    # Increase contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(denoised)
    
    # Thresholding
    _, binary = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return binary

def extract_text_from_image(image_data):
    """Extract text from the image."""
    try:
        # Prepare the image
        processed_image = preprocess_image(image_data)
        
        # Initialize the OCR reader
        reader = initialize_ocr()
        
        # Extract text
        results = reader.readtext(processed_image)
        
        # Concatenate all text results
        text = ' '.join([result[1] for result in results])
        
        return text.strip()
    
    except Exception as e:
        return f"OCR Error: {str(e)}"

def get_gemini_solution(text):
    """Retrieve solution from the Gemini API."""
    api_key = "AIzaSyCUeZCNNOGu_HU1W7nbj-zbOELRW7ULyyg"  # Replace with your actual Gemini API key
    gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Please solve this math problem step by step: {text}"
                    }
                ]
            }
        ]
    }
    
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    
    try:
        response = requests.post(gemini_api_url, json=payload, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            solution_md = data['candidates'][0]['content']['parts'][0]['text']
            return markdown.markdown(solution_md)
        else:
            return f"API Error: {response.status_code}"
            
    except Exception as e:
        return f"Connection Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html', solution=None)

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Check if the request contains form data
        if request.files:
            # Handle file upload
            if 'file' in request.files:
                image_file = request.files['file'].read()
                extracted_text = extract_text_from_image(image_file)
            else:
                extracted_text = ""

        # Handle form data
        math_term = request.form.get('math_term', '')
        
        # Handle photo data
        photo = request.form.get('photo', '')
        if photo and photo.startswith('data:image'):
            photo_text = extract_text_from_image(photo)
            math_term = f"{math_term} {photo_text}".strip()

        # Handle audio data (placeholder for future implementation)
        audio = request.form.get('audio', '')
        if audio:
            # Burada ses dosyasını işleyecek kod eklenebilir
            # Örneğin: speech-to-text dönüşümü yapılabilir
            pass

        # Get final solution
        if math_term:
            solution_html = get_gemini_solution(math_term)
        elif extracted_text:
            solution_html = get_gemini_solution(extracted_text)
        else:
            return jsonify({"error": "No input provided"}), 400

        # Return the solution
        return jsonify({
            "solution": solution_html,
            "explanation": "Bu açıklama alanında gösterilecektir.",
            "videos": ["https://sample-video1.com", "https://sample-video2.com", "https://sample-video3.com"]
        })

    except Exception as e:
        app.logger.error(f"Error in solve endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

def handle_audio_input(audio_data):
    """
    Process audio input and convert to text.
    This is a placeholder for future implementation.
    """
    # Implement speech-to-text conversion here
    return ""

if __name__ == '__main__':
    app.run(debug=True)