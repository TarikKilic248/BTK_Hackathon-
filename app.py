from flask import Flask, jsonify, render_template, request,send_from_directory
import requests
import markdown
import easyocr
import cv2
import numpy as np
import base64
import re
import speech_recognition as sr # pip install SpeechRecognition
from PIL import Image
from werkzeug.utils import secure_filename
import os
import os
import google.generativeai as genai
import json
from gemini_question import gemini_create_document,send_problem_to_gemini,gemini_video_oneri
import tempfile

app = Flask(__name__)

# Global EasyOCR reader
reader = None

# Ses dosyalarının kaydedileceği dizin
AUDIO_FOLDER = 'audios'
app.config['AUDIO_FOLDER'] = AUDIO_FOLDER

# Dizin yoksa oluştur
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route('/save-audio', methods=['POST'])
def save_audio():
    try:
        if 'audio' not in request.files:
            return jsonify({'success': False, 'error': 'Ses dosyası bulunamadı'})
        
        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'success': False, 'error': 'Dosya seçilmedi'})
        
        # Güvenli dosya adı oluştur
        filename = secure_filename(audio_file.filename)
        filepath = os.path.join(app.config['AUDIO_FOLDER'], filename)
        
        # Dosyayı kaydet
        audio_file.save(filepath)
        
        return jsonify({
            'success': True,
            'filepath': filepath,
            'filename': filename
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

# Kaydedilen ses dosyalarına erişim için route
@app.route('/audios/<filename>')
def serve_audio(filename):
    return send_from_directory(app.config['AUDIO_FOLDER'], filename)


def initialize_ocr():
    """Initialize the EasyOCR reader."""
    global reader
    if reader is None:
        # Create reader for English and Turkish
        reader = easyocr.Reader(['en', 'tr'])
    return reader

def preprocess_image(image):
    """Prepare the image for OCR."""
    # Convert PIL image to NumPy array
    if isinstance(image, Image.Image):  # Check if the input is a PIL image
        image = np.array(image)

    # Convert to OpenCV format
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV
    
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

def extract_Text_from_waw(waw_data):
    # Recognizer oluşturun
    recognizer = sr.Recognizer()

    # WAV dosyasını yükleyin
    file_path = waw_data 

    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    # Ses verisini yazıya dökün
    try:
        text = recognizer.recognize_google(audio_data, language="tr-TR")  # Türkçe dilini seçiyoruz
        print("Çözümlenen metin:", text)
    except sr.UnknownValueError:
        text="Ses anlaşılamadı."
        print("Ses anlaşılamadı.")
    except sr.RequestError as e:
        text="Google API'sine ulaşılamadı."
        print(f"Google API'sine ulaşılamadı: {e}")
    return text

def extract_text_from_image(image_data):
    """Extract text from the image."""
    try:
        # Convert the image_data to a NumPy array
        image_data = np.array(image_data)  # Convert PIL image to NumPy array

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

def get_gemini_solution(text,soru_metni):
    """Retrieve solution from the Gemini API."""
    api_key = "AIzaSyANFGM-zwnIA56Bq4Q4CRe7oKexCuBkxm8"  # Replace with your actual Gemini API key
    gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"{text} {soru_metni} "
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

        photo_path=None
        # Handle form data
        math_term = request.form.get('math_term', '')
        photo_url = request.form.get('geometry_photo', '')

        # Fotoğraf URL'si varsa dosyayı yükle
        if photo_url:
            photo_path = os.path.join(os.getcwd(), photo_url.strip('/'))
            print("Foto yolu",photo_path)
            

        soru_metni="Lütfen bu problemi adım adım çözer misin ?"
        
        # Get final solution
        if photo_path!=None:
            print("Buraya girdi")
            solution_html = send_problem_to_gemini(math_term,photo_path)
            document_text = gemini_create_document("Geometri")
            video_text = gemini_video_oneri("Geometri")
        elif math_term:
            print("Math term alanına girdi")
            solution_html = get_gemini_solution(math_term,soru_metni)
            document_text = gemini_create_document(math_term)
            video_text = gemini_video_oneri(math_term)
        elif extracted_text:
            solution_html = get_gemini_solution(extracted_text)
        else:
            return jsonify({"error": "No input provided"}), 400

        print(video_text)
        # Return the solution
        return jsonify({
            "solution": solution_html,
            "explanation": "Bu açıklama alanında gösterilecektir.",
            "document": document_text,
            "videos": video_text["youtube_videoları"]
        })

    except Exception as e:
        app.logger.error(f"Error in solve endpoint: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/extract-text', methods=['POST'])
def extract_text():
    file = request.files['image']
    image = Image.open(file.stream)
    text = extract_text_from_image(image)
    return jsonify({'text': text})

def handle_audio_input(audio_data):
    """
    Process audio input and convert to text.
    This is a placeholder for future implementation.
    """
    # Implement speech-to-text conversion here
    return ""







# Geometri resmini yükleme

UPLOAD_FOLDER = 'images'
# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.route('/upload_geometry_photo', methods=['POST'])
def upload_geometry_photo():
    try:
        # Check if a file was included in the request
        if 'geometry_photo' not in request.files:
            return jsonify({"success": False, "error": "No file provided"}), 400

        file = request.files['geometry_photo']
        if file.filename == '':
            return jsonify({"success": False, "error": "No selected file"}), 400

        # Create a unique filename
        filename = f"_1{file.filename}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save the file to the images folder
        file.save(file_path)

        # Return the file's URL path
        file_url = f"/{UPLOAD_FOLDER}/{filename}"
        return jsonify({"success": True, "url": file_url}), 200

    except Exception as e:
        print("Error saving file:", e)
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)