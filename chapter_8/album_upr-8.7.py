def get_make_album(executor_name, album, colum_track=''):
    if colum_track:
        musician = f"\nExecutor: {executor_name} \nTrack: {colum_track} \nAlbum: {album}"
    else:
        musician = f"\nExecutor: {executor_name} \nAlbum: {album}"
    return musician.title()
person = get_make_album('karen mal', 'wildwood flower','3')
print(person)
person = get_make_album('karen mal', 'rosalie')
print(person)
person = get_make_album('ludovico einaudi', 'underwater', '9')
print(person)