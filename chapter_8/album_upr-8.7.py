def get_make_album(executor_name, album, colum_track=''):
    if colum_track:
        musician = (f"\nExecutor: "
                    f"{executor_name} \nTrack: "
                    f"{colum_track} \nAlbum: "
                    f"{album}"
                    )
    else:
        musician = (f"\nExecutor: {executor_name} "
                    f"\nAlbum: {album}"
                    )
    return musician.title()
person = get_make_album(
    'karen mal',
    'wildwood flower',
    '3'
)
print(person)
person = get_make_album(
    'karen mal',
    'rosalie'
)
print(person)
person = get_make_album(
    'ludovico einaudi',
    'underwater',
    '9'
)
print(person)