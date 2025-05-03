def get_make_album(executor_name, album):
    musician = f"\nExecutor: {executor_name} \nAlbum: {album}"
    return musician.title()
while True:
    print(f"Please enter the artist's name: "
          f"(enter 'q' at any time to quit)")
    e_name = input('Executor name: ')
    if e_name == 'q':
        break
    album_name = input('Album :')
    if album_name == 'q':
        break
    make_album = get_make_album(e_name, album_name)
    print(make_album)