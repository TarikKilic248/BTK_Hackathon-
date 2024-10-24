import tkinter as tk
from api import calculate_math

# Tkinter arayüzü
root = tk.Tk()
root.title("Matematik İşlemi Hesaplama")

# Giriş alanı (Matematiksel ifade)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Sonucu gösterecek etiket
result_label = tk.Label(root, text="Sonuç: ")
result_label.pack(pady=10)

# Hesapla butonu (calculate_math fonksiyonuna entry ve result_label parametreleri geçiriliyor)
calculate_button = tk.Button(root, text="Hesapla", command=lambda: calculate_math(entry, result_label))
calculate_button.pack(pady=10)

# Tkinter döngüsünü başlat
root.mainloop()
