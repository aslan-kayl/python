country = ['Австрия',
           'Азербайджан',
           'алжир' ,
           'Албании',
           'Ангола',
           'Андорра',
           'Армении',
           'Аргентина',
           'Афганистан',
           'Бангладеш',
           'Багамы',
           'Барбадос'
]
print(country[3].title())
print(country[-1].title())
message = f'I love {country[9]}!'
print(message)
country[0] = 'Англия'
print(country[0])
country.append('Испании')
print(country[-1])
country.insert(2, 'Италия')
print(country)
del country[5]
print(country)
country_delete = country.pop()
print(country)
print(country_delete)
print(f"Я уже бывал в {country_delete.upper()}"
      f", но мне там очень понравилось из-за этого не буду его полностью удалять из списка")
country_delete = country.pop(-1)
print(f'В {country_delete.lower()}, я тоже был. Какой же там прекрасный пляж')
country.remove('Армении')
print(country)
country_delete = 'Албании'
country.remove(country_delete)
print(f'Когда-то я был в  {country_delete} и там замечательные люди!')

print(country)
country.sort(reverse=True)
print(sorted(country))
