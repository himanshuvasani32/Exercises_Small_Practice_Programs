freezing_point = 0
boiling_point = 100

def water_state(temperature):
    if temperature <= freezing_point:
        return "Solid"
    elif freezing_point < temperature < boiling_point:
        return "Liquid"
    else:
        return "Gas"


print(water_state(50))