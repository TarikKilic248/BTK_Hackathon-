from flask import Flask, render_template, request
import requests
import markdown
import easyocr
import cv2
import numpy as np
import os

app = Flask(__name__)

# Global EasyOCR okuyucusu
reader = None

def initialize_ocr():
    """EasyOCR okuyucusunu başlat"""
    global reader
    if reader is None:
        # İngilizce ve Türkçe için okuyucu oluştur
        reader = easyocr.Reader(['en', 'tr'])
    return reader

def preprocess_image(image):
    """Görüntüyü OCR için hazırla"""
    # OpenCV formatına dönüştür
    nparr = np.frombuffer(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Griye çevir
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Gürültüyü azalt
    denoised = cv2.fastNlMeansDenoising(gray)
    
    # Kontrastı artır
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(denoised)
    
    # Eşikleme
    _, binary = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return binary

def extract_text_from_image(image_data):
    """Görüntüden metin çıkar"""
    try:
        # Görüntüyü hazırla
        processed_image = preprocess_image(image_data)
        
        # OCR okuyucusunu başlat
        reader = initialize_ocr()
        
        # Metni çıkar
        results = reader.readtext(processed_image)
        
        # Tüm metinleri birleştir
        text = ' '.join([result[1] for result in results])
        
        return text.strip()
    
    except Exception as e:
        return f"OCR Hatası: {str(e)}"

def get_gemini_solution(text):
    """Gemini API'den çözüm al"""
    api_key = "Your gemini api key"
    gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Bu matematik problemini çöz ve adım adım açıkla: {text}"
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
            return f"API Hatası: {response.status_code}"
            
    except Exception as e:
        return f"Bağlantı Hatası: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html', solution=None)

@app.route('/solve', methods=['POST'])
def solve():
    if 'math_image' in request.files:
        # Görüntüden metin çıkar
        image_file = request.files['math_image'].read()
        extracted_text = extract_text_from_image(image_file)
        
        # Çözüm al
        solution_html = get_gemini_solution(extracted_text)
        
        return render_template('solution.html', 
                             solution=solution_html, 
                             original_text=extracted_text)
    
    elif 'math_term' in request.form:
        # Doğrudan metin girişi
        user_input = request.form['math_term']
        solution_html = get_gemini_solution(user_input)
        
        return render_template('solution.html', 
                             solution=solution_html, 
                             original_text=user_input)
    
    else:
        return render_template('solution.html', 
                             solution="Lütfen bir matematik problemi girin veya görüntü yükleyin.")

if __name__ == '__main__':
    app.run(debug=True)