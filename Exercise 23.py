def weather_detail(temperature):
    if temperature > 7 :
        return "Warm"
    else:
        return "Cold"


print(weather_detail(9))