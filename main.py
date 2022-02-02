import requests
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

LAT_PAN = 9.074410
LON_PAN = -79.448807

LAT_SAO_P = -23.550520
LON_SAO_P = -46.633308

api_key = os.environ['OWN_API_KEY']

parameters = {
    'lat': LAT_SAO_P,
    'lon': LON_SAO_P,
    'appid': api_key,
    'exclude': 'current,minutely,daily'

}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall',params=parameters)
response.raise_for_status()
data = response.json()

print(data['timezone'])
rain = [data['hourly'][i]['weather'][0]['id'] for i in range(12) if data['hourly'][i]['weather'][0]['id'] < 700]

if len(rain) > 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring a ☔️.",
        from_='+19035680939',
        to='+50760737637'
    )

print(message.status)