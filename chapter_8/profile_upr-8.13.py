def build_profile(first, last, **kwargs):
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs
user_profile = build_profile('aslan','kayl',
                             location='world',
                             speciality='python developer',
                             eye_color='brown')
print(user_profile)
