def formatDate():
    date = input('Enter a date in format dd/mm/yyyy: ')

    invalid_date_error_message = 'Error: Invalid date.'

    arr = date.split('/')

    if len(arr) > 3:
        return invalid_date_error_message
    elif not arr[0].isdigit() or not arr[1].isdigit() or not arr[2].isdigit():
        return invalid_date_error_message
    elif int(arr[1]) > 12:
        return invalid_date_error_message
    elif not int(arr[2]) % 4 == 0 and int(arr[0]) > 28:
        return invalid_date_error_message
    elif int(arr[0]) > 31:
        return invalid_date_error_message
    elif int(arr[2]) % 2 == 0 and int(arr[0]) > 30:
        return invalid_date_error_message

    return f'{arr[2]}-{arr[1]}-{arr[0]}'


print(formatDate())
