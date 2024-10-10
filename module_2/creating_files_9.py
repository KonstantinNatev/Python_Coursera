try:
    with open('s/new_file.txt', 'a') as file:
        file.write('Hello World s')

    with open('new_file.txt', 'a') as file:
        file.writelines(['Hello World', '\nHello World 3'])
except FileNotFoundError as e:
    print('File not found', e)