import requests

# Define crop suitability based on weather parameters
def suggest_crops(temperature, rainfall, humidity):
    crops = []
    
    # Example crop suggestions based on temperature, rainfall, and humidity
    # Adjusted to be more lenient and ensure at least one crop is suggested
    if 15 <= temperature <= 25 and rainfall < 200 and humidity < 70:
        crops.append("Wheat")
    if 20 <= temperature <= 30 and rainfall >= 200 and humidity >= 70:
        crops.append("Corn")
    if 25 <= temperature <= 35 and rainfall >= 250 and humidity >= 75:
        crops.append("Rice")
    if 18 <= temperature <= 28 and rainfall < 150 and humidity < 60:
        crops.append("Barley")
    if 22 <= temperature <= 32 and rainfall >= 150 and humidity >= 80:
        crops.append("Soybeans")
    if 20 <= temperature <= 30 and rainfall >= 100 and humidity < 75:
        crops.append("Millet")
    
    # Always return some crops, even if no perfect match
    if not crops:
        # If no crops fit exactly, suggest fallback options
        if temperature < 15:
            crops.append("Oats")  # Example of a cooler-weather crop
        elif temperature > 35:
            crops.append("Sorghum")  # Example of a drought-resistant crop
        elif rainfall < 100:
            crops.append("Lentils")  # Tolerant to low rainfall
        else:
            crops.append("Cassava")  # Tolerant to various conditions

    return crops

# Define nearby cities for crop suggestions
def nearby_cities(city):
    cities = {
        "London": ["Birmingham", "Manchester", "Liverpool"],
        "New York": ["Philadelphia", "Boston", "Baltimore"],
        "Delhi": ["Noida", "Gurgaon", "Faridabad"],
        "Chennai": ["Ooty", "Coimbatore", "Salem"],
        "Tokyo": ["Yokohama", "Osaka", "Nagoya"],
        "Sydney": ["Newcastle", "Wollongong", "Central Coast"],
        "Rio de Janeiro": ["São Paulo", "Belo Horizonte", "Salvador"],
        "Cairo": ["Alexandria", "Giza", "Luxor"]
    }
    return cities.get(city, [])

API_KEY = '4f6a211e1ec594251b8b4de6d2838ba9'  # Replace with your actual API key
CITY = 'Rome'  # You can change this to any city
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temperature = data['main']['temp']  # Get current temperature
    humidity = data['main']['humidity']  # Get current humidity
    rainfall = data.get('rain', {}).get('1h', 0)  # Get rainfall amount in the last hour (default to 0 if not present)
    
    print(f"Current temperature in {CITY}: {temperature}°C")
    print(f"Current humidity in {CITY}: {humidity}%")
    print(f"Rainfall in the last hour in {CITY}: {rainfall} mm")
    
    # Crop suggestions based on the temperature, rainfall, and humidity
    crops = suggest_crops(temperature, rainfall, humidity)
    if crops:
        print(f"Suitable crops for {CITY}: {', '.join(crops)}")
    else:
        print(f"No suitable crops found for {CITY} at this time.")  # This line should rarely be reached now
    
    # Suggest nearby cities for growing the crops
    cities = nearby_cities(CITY)
    if cities:
        print(f"Nearby cities where these crops can also be grown: {', '.join(cities)}")
    else:
        print("No nearby cities found for crop suggestions.")
else:
    print("Error:", data.get('message', 'Something went wrong'))
