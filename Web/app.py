from flask import Flask, render_template, request
import requests
import markdown

app = Flask(__name__)

# Ana sayfa rotası
@app.route('/')
def index():
    return render_template('index.html', solution=None)

# Çözüm üretme rotası
@app.route('/solve', methods=['POST'])
def solve():
    user_input = request.form['math_term']
    api_key = "Your gemini api key"
    gemini_api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        ]
    }
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    response = requests.post(gemini_api_url, json=payload, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        solution_md = data['candidates'][0]['content']['parts'][0]['text']
        
        # Markdown'ı HTML'ye dönüştürme
        solution_html = markdown.markdown(solution_md)
        
        return render_template('solution.html', solution=solution_html)
    else:
        return render_template('solution.html', solution="Bir hata oluştu.")

if __name__ == '__main__':
    app.run(debug=True)
