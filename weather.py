import requests
print(requests.__version__)


print("=== Simple Weather App ===")

city = input("Enter city name: ")

api_key = "1d4551248c55c6d35988b5d3b8fcee39"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
print(response.json())


if response.status_code == 200:
    data = response.json()
    main = data['main']
    weather = data['weather'][0]

    print(f"\nWeather in {city.capitalize()}:")
    print(f"Temperature: {main['temp']}°C")
    print(f"Feels like: {main['feels_like']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Condition: {weather['description'].capitalize()}")
else:
    print("\nCity not found. Please check the name and try again.")

