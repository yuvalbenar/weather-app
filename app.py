from flask import Flask, render_template, request
import requests

app = Flask(__name__)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

# Your OpenWeather API key
API_KEY = "878aa4daa96b54c229b7f0388991c1dc"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    city_country = "Enter city, country (e.g., London, UK)"
    if request.method == 'POST':
        city_country = request.form['city_country'].replace(" ", "")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_country}&appid={API_KEY}&units=metric"
        
        print(f"Requested URL: {url}")  # Debugging: Check the URL being requested
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            # Extract error message from API response, or default if unavailable
            error_message = response.json().get("message", "City or country not found!")
            weather = {'error': error_message}

    # Static winter facts
    winter_facts = [
        "Snowflakes are not always unique—there are similar ones!",
        "The coldest temperature ever recorded was -128.6°F in Antarctica.",
        "Winter solstice marks the shortest day of the year.",
        "Polar bears are excellent swimmers, even in freezing waters!"
    ]

    return render_template('index.html', weather=weather, facts=winter_facts, city_country=city_country)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
