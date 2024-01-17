import requests
from twilio.rest import Client

# openweathermap info, complete your own info
OWM_API_KEY = {"openweathermap api key"}
lat = {"your latitude"}
lon = {"your longitude"}
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": OWM_API_KEY,
    "cnt": 4,
}
# twilio data, you need to set up at least a free twilio account for this info
PHONE_NUMBER = "twilio phone number"
account_sid = 'twilio sid'
auth_token = 'twilio auth token'

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella.☔ ",
        from_=PHONE_NUMBER,
        # you need to insert your real verified with twilio phone number here
        to='Your real phone number'
    )
    print(message.status)
