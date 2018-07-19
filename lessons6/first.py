import pyowm

city = input('Input  name of  your  city : ')


owm = pyowm.OWM('df0a6c844b58c3fe6b81de60ae1c4dfd')
observation = owm.weather_at_place(city)
w = observation.get_weather()
status = w.get_detailed_status()
temperature = w.get_temperature('celsius')['temp']
print('Now in '+ city + ' ' + str(temperature), '\n' +
	str(status)) 


