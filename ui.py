#arayuz tasarimi

import tkinter as tk
import requests

# Gemini API'ye bağlanmak için bir fonksiyon
def calculate_math():
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

# Tkinter arayüzü
root = tk.Tk()
root.title("Matematik İşlemi Hesaplama")

# Giriş alanı (Matematiksel ifade)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Hesapla butonu
calculate_button = tk.Button(root, text="Hesapla", command=calculate_math)
calculate_button.pack(pady=10)

# Sonucu gösterecek etiket
result_label = tk.Label(root, text="Sonuç: ")
result_label.pack(pady=10)

# Tkinter döngüsünü başlat
root.mainloop()

