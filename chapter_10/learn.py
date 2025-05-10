with open('learning_python.txt') as object_file:
    content = object_file.readlines()
    for line in content:
        print(line.replace('Python', 'C').rstrip())
