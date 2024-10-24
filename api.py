import requests

# Gemini API'ye bağlanmak için bir fonksiyon
def calculate_math(entry, result_label):
    math_expression = entry.get()  # Kullanıcının girdiği matematiksel işlem
    try:
        # Gemini API'ye POST isteği gönder
        response = requests.post(
            'https://api.gemini.com/v1/math/calculate',  # Örnek API URL'si
            json={'expression': math_expression},
        )
        result = response.json().get('result', 'Geçersiz işlem')  # Sonuç döndür
    except Exception as e:
        result = f'Hata: {e}'
    
    # Sonucu arayüzde göster
    result_label.config(text=f"Sonuç: {result}")
