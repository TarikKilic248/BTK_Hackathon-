import requests

# Alınan OAuth 2.0 access token'ı buraya ekleyin
# Replace 'YOUR_API_KEY' with your actual API key
api_key = "AIzaSyCUeZCNNOGu_HU1W7nbj-zbOELRW7ULyyg"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
payload = {
    "contents": [
    {
      "parts": [
        {
          "text": "2x + 3 = 7 denklemini çöz"
        }
      ]
    }
  ]
}
headers = {"Content-Type": "application/json"}

# Authenticate with API key (assuming key goes in query parameter)
params = {"key": api_key}

# Send POST request with payload and headers
response = requests.post(url, headers=headers, params=params, json=payload)


if response.status_code == 200:
  # Parse the JSON response
  data = response.json()
  type(data)
  print(data.keys())
  # Metni almak için:
  text = data['candidates'][0]['content']['parts'][0]['text'] 
  print(text)
else:
    print(f"API Hatası: {response.status_code}, Mesaj: {response.json()}")
