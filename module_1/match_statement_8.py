# Switch case in Python

http_status = input('Enter status code: ')

match http_status:
    case '200' | '201':
        print('200 OK')
    case _:  # default statement
        print('Unknown')
