def weather_details(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature < 15:
        return "Cold"
    else:
        return "Warm"


print(weather_details(15))