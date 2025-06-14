import requests
import smtplib
MY_LAT = 43.817070
MY_LON = 125.323547
API_KEY = "32e196706b138aa5744535de5008a551"
PASSWORD = "wgyi wsuh viwv cuvx"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt":4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login("rezarezai164164@gmail.com", PASSWORD)
        connection.sendmail(
            from_addr="rezarezai164164@gmail.com",
            to_addrs="rezarezai164@yahoo.com",
            msg="Subject: Rain Alert\n\nbring an umbrella"
        )



