cities = {
    'granada':{
    'country': 'spain',
    'population': 233_680,
    'fact': 'It is famous for its fine examples of medieval architecture'
    },
    'alberobello': {
    'country': 'italy',
    'population': 10_237,
    'fact': 'famous for its unique structures - trulli, included in the UNESCO World Heritage List',
    },
    'alaska': {
    'country': 'america',
    'population': 740_133,
    'fact': 'the northern lights are located there',
    },
}
for city, city_info in cities.items():
    print(f"\nCity : {city.title()}")
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"
    print(f"\tCountry : {country.title()}"
          f"\n\tPopulation : {population.title()}"
          f"\n\tFact : {fact.title()}")