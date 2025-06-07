import requests

def main():
    city = input("Enter your city: ")
    weather = get_weather(city)
    if weather:
        suggest_activity(weather)
    else:
        print("Sorry, couldn't fetch the weather. Please check your city name.")

def get_weather(city):
    API_KEY = '9e5b6785214c160446f3d028e837c140'
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(URL)
    data = response.json()

    if data.get('cod') != 200:
        return None

    weather = {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }
    return weather
def suggest_activity(weather):
    temp = weather['temperature']
    desc = weather['description']
    humidity = weather['humidity']

    print(f"\nWeather: {desc.capitalize()}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")

    if "rain" in desc or humidity > 85:
        print(" It might not be a good idea to go outside. Try indoor activities like yoga or reading.")
    elif 20 <= temp <= 30:
        print(" Perfect for outdoor activities like jogging, cycling, or a walk!")
    elif temp < 10:
        print(" Too cold! Consider indoor workouts.")
    else:
        print("Might be too hot, stay hydrated and avoid peak sun hours, carry hydration pack and some electrolyte "
              "solution.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
