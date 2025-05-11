def open_file(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
            print(content)
    except FileNotFoundError:
        pass
filename = ['dogs.txt', 'cats.txt']
for filenames in filename:
    open_file(filenames)
