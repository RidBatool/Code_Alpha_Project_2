import requests
import time
from plyer import notification

API_KEY = "ab583c13cc6ee6edafb1c0a0a60adab1"  # Replace with your actual API key

def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp_c = round(data['main']['temp'] - 273.15)
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            name = data['name']
            
            # Truncate each part to ensure the message is concise
            message = (
                f"{name}: {temp_c}°C, "
                f"{description[:20]}... "
                f"Humidity: {humidity}%, Wind: {wind_speed} m/s."
            )
            return message[:256]  # Final check to ensure it's within 256 characters
        else:
            return "Error fetching weather data."
    except Exception as e:
        return f"An error occurred: {e}"

def notify_weather():
    while True:
        weather_info = fetch_weather()
        notification.notify(
            title='Weather Update for Karachi',
            message=weather_info,
            app_name='Weather Notifier',
            timeout=10  # Duration in seconds
        )
        time.sleep(300)  # Wait for 5 minutes

if __name__ == '__main__':
    notify_weather()
