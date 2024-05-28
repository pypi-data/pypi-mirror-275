import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Buraya gerçek bir API anahtarı ekleyin
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data['cod'] != '404':
        main = data['main']
        weather_description = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        
        return f"City: {city}\nTemperature: {temp}°C\nHumidity: {humidity}%\nDescription: {weather_description}"
    else:
        return "City Not Found!"

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))

