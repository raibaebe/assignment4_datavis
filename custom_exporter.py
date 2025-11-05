from prometheus_client import start_http_server, Gauge
import requests, time

# --- OpenWeather API Setup ---
API_KEY = "cdf3594010f8513f97df0d7840062930"
CITY = "Astana" 
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# --- Define Metrics ---
temp = Gauge('weather_temperature_celsius', 'Current temperature in °C')
feels_like = Gauge('weather_feels_like_celsius', 'Feels-like temperature in °C')
humidity = Gauge('weather_humidity_percent', 'Humidity in %')
pressure = Gauge('weather_pressure_hpa', 'Atmospheric pressure in hPa')
wind_speed = Gauge('weather_wind_speed_mps', 'Wind speed in m/s')
wind_deg = Gauge('weather_wind_direction_deg', 'Wind direction in degrees')
clouds = Gauge('weather_clouds_percent', 'Cloudiness in %')
visibility = Gauge('weather_visibility_m', 'Visibility in meters')
rain = Gauge('weather_rain_1h_mm', 'Rain volume for the last hour in mm')
timestamp = Gauge('weather_last_update_timestamp', 'Last update timestamp (epoch)')

def fetch_weather():
    try:
        r = requests.get(URL)
        data = r.json()

        temp.set(data["main"]["temp"])
        feels_like.set(data["main"]["feels_like"])
        humidity.set(data["main"]["humidity"])
        pressure.set(data["main"]["pressure"])
        wind_speed.set(data["wind"]["speed"])
        wind_deg.set(data["wind"]["deg"])
        clouds.set(data["clouds"]["all"])
        visibility.set(data.get("visibility", 0))
        rain.set(data.get("rain", {}).get("1h", 0))
        timestamp.set(time.time())

        print(f"✅ Updated: {CITY} | Temp: {data['main']['temp']}°C | Humidity: {data['main']['humidity']}%")

    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    start_http_server(8000)
    print("Custom exporter running on http://localhost:8000/metrics")
    while True:
        fetch_weather()
        time.sleep(20)
