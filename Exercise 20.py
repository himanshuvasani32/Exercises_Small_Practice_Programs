def get_age(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return age


print(get_age(1996))
