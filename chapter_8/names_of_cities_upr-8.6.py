def get_city_country(city, country):
    my_city_country = f"{city}, {country}"
    return my_city_country.title()
conclusion = get_city_country('tokyo', 'japan')
print(conclusion)