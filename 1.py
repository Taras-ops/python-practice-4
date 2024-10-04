def formatDate():
    MONTHS_DAYS = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }

    date = input('Enter a date in format dd/mm/yyyy: ')

    invalid_date_error_message = 'Error: Invalid date.'

    arr = date.split('/')

    if len(arr) > 3:
        return invalid_date_error_message
    if len(arr[1]) != 2:
        return invalid_date_error_message
    if len(arr[0]) > 2:
        return invalid_date_error_message
    elif not arr[0].isdigit() or not arr[1].isdigit() or not arr[2].isdigit():
        return invalid_date_error_message
    elif int(arr[1]) > 12:
        return invalid_date_error_message
    elif not int(arr[2]) % 4 == 0 and int(arr[1]) == 2 and int(arr[0]) > 28:
        return invalid_date_error_message
    elif MONTHS_DAYS[arr[1]] < int(arr[0]):
        return invalid_date_error_message

    return f'{arr[2]}-{arr[1]}-{arr[0]}'


print(formatDate())
