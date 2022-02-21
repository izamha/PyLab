import datetime as dt


def main():
    print('Hello Hell!')
    name = input('Enter your name: ')
    age = input('And your age: ')
    now = dt.date.today()
    now_year = now.year
    now_year_hundy = now_year + 100
    print(name, ', you are', age, '. and today were in', now_year,
          'So you will turn 100 in', now_year_hundy)


if __name__ == "__main__":
    main()
