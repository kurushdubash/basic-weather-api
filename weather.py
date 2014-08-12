import requests

wind_directions = {'S': 'South', 'N':'North', 'W': 'West', 'E': 'East', 'SW' : 'South West', 'NW': 'North West', 'NE': 'North East', 'SE': 'South East',}

def get_zip_code():
	print('Please enter your zip code:')
	zip_code = input()

	while len(zip_code) < 5 or len(zip_code) > 5:
		print('Invalid Zip Code')
		print('Please enter your zip code:')
		zip_code = input()
	return zip_code

def get_weather_json(zip):
	url = 'http://www.myweather2.com/developer/forecast.ashx?uac=xuv-N8e7ge&output=json&query=' + zip + '&temp_unit=f&ws_unit=mph'
	weather_data = requests.get(url)
	weather_json = weather_data.json()
	return weather_json

def get_location_info(zip):
	url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + str(zip) + '&sensor=true'
	location_data = requests.get(url)
	location_json = location_data.json()
	return location_json['results'][0]['formatted_address']

def get_temperature(json_data):
	temp = json_data['weather']['curren_weather'][0]['temp']
	return str(temp) + ' degrees fahrenheit / ' + str(int((int(temp) - 32) / 1.8)) + ' degrees celsius'

def get_wind_data(json_data):
	wind_speed = json_data['weather']['curren_weather'][0]['wind']
	return wind_speed

zip_code_input = get_zip_code()
data = get_weather_json(zip_code_input) 

print()
#Get Zip Code City, State, and Country info
print(get_location_info(zip_code_input))
#Get Temperature 
print('Temperature:' , get_temperature(data))
#Collect all wind data
wind_data = get_wind_data(data) 
if wind_data[0]['dir'] != "Not Available" and wind_data[0]['dir'] in wind_directions: #If Weather is avalible, show it
	wind_dire = get_wind_data(data)[0]['dir']
	print('Wind Speed:', get_wind_data(data)[0]['speed'] + 'MPH' , wind_directions[wind_dire])
print(data['weather']['curren_weather'][0]['weather_text']) #Weather Description