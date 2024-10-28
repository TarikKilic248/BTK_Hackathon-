from flask import Flask, jsonify, render_template, request
import requests
import markdown
import easyocr
import cv2
import numpy as np

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
    if 'math_image' in request.files:
        # Resimden metin çıkarma
        image_file = request.files['math_image'].read()
        extracted_text = extract_text_from_image(image_file)
        
        # Çözüm alma
        solution_html = get_gemini_solution(extracted_text)
        
        # JSON formatında döndür
        return jsonify({
            "solution": solution_html,
            "explanation": "Bu açıklama alanında gösterilecektir.",
            "videos": ["https://sample-video1.com", "https://sample-video2.com", "https://sample-video3.com"]
        })
    
    elif 'math_term' in request.json:
        # Kullanıcı metni doğrudan girdiyse
        user_input = request.json['math_term']
        solution_html = get_gemini_solution(user_input)
        
        # JSON formatında döndür
        return jsonify({
            "solution": solution_html,
            "explanation": "Bu açıklama alanında gösterilecektir.",
            "videos": ["https://sample-video1.com", "https://sample-video2.com", "https://sample-video3.com"]
        })
    
    else:
        return jsonify({"error": "Lütfen bir matematik problemi girin veya bir resim yükleyin."}), 400
    
if __name__ == '__main__':
    app.run(debug=True)
