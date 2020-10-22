import pyowm

owm = pyowm.OWM('f34a3b16d0cf715d638eb1c2bae33f37', language = "ru")

place = input("В каком городе/стране? : ")

observation = owm.weather_at_place(palace)
w = observation.get_weather()

print(w)
