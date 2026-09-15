from tools.weather_tool import get_weather


city = input("Enter city: ")


result = get_weather(city)


print(result)