from flask import Flask, render_template, request
import requests

app = Flask(__name__)

api_key = '30d4741c779ba94c470ca1f63045390a'

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    weather = None
    temp = None
    city = None
    
    if request.method == 'POST':
        city = request.form['city']
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

        
        if weather_data.json().get('cod') == '404':
            error = "A város/falu nem található!"
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round(weather_data.json()['main']['temp'])

    return render_template('index.html', weather=weather, temp=temp, city=city, error=error)

if __name__ == '__main__':
    app.run(debug=True)
