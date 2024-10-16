
import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("A város/falu nem található!")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round( weather_data.json()['main']['temp'])

    print(f"Az égbolt itt {user_input} : {weather}")
    print(f"A hőfok itt {user_input} : {temp}")

