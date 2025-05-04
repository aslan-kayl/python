def cars_info(auto, manufacturer, **kwargs):
    kwargs['auto'] = auto
    kwargs[manufacturer] = manufacturer
    return kwargs
get_info = cars_info(
    'ford gt40', 'henry ford jr.',
    year_production=1964,
    maximum_spead='348km-ch'
)
print(get_info)