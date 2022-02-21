try:
    the_file = open('peoples.csv')
    print(the_file.name)
    print(the_file)
except FileNotFoundError:
    print('Sorry! The file not found.')
