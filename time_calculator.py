testing = '11:55 AM'
duration2 = '3:12'

def add_time(start, duration, day=None):
    
    # Helper function that extracts start or duration to a tuple
    def extract_time_to_tuple(time):
        if time.count(' AM') > 0 or time.count(' PM') > 0:
            parts = time.split(":")
            hour = int(parts[0])
            minutes = int(parts[1].split()[0])
            am_pm = parts[1].split()[1].upper()

            result = (hour, minutes, am_pm)
            return result

        elif time.count(' AM') == 0 and time.count(' PM') == 0:
            parts = time.split(":")
            hour = int(parts[0])
            minutes = int(parts[1])
            
            result = (hour, minutes)
            return result
        
    # Initializing variables to calculate on
    weekdays = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    if day != None:
        current_day = weekdays.get(day.lower())
    
    result_h = 0
    result_m = 0
    result_d = 0
    meridien = ''
    days_later = 0

    # Extracting start and duration time
    start_tuple = extract_time_to_tuple(start)
    duration_tuple = extract_time_to_tuple(duration)
    
    # Main time calculations
    # Setting AM/PM
    if start_tuple[2] == 'AM':
        meridien = 'AM'
    elif start_tuple[2] == 'PM':
        meridien = 'PM'

    # Calculating total minutes & hours
    result_h = start_tuple[0] + duration_tuple[0]
    result_m = start_tuple[1] + duration_tuple[1]

    # Taking care of edge cases where both hours and minutes can change meridien
    while result_m > 60:

        if meridien == 'PM' and start_tuple[0] == 11:
            days_later += 1
            meridien = 'AM'
        elif meridien == 'PM' and start_tuple[0] == 11 and (start_tuple[0] + duration_tuple[0]) > 12:
            pass
        elif meridien == 'AM' and start_tuple[0] == 11 and (start_tuple[0] + duration_tuple[0]) > 12:
            pass
        elif meridien == 'AM' and start_tuple[0] == 11:
            meridien = 'PM'
            if result_h > 11:
                days_later -= 1
        result_m -= 60
        result_h += 1

    while result_h > 12:
        if meridien == 'AM':
            meridien = 'PM' 
        else:
            meridien = 'AM'
            days_later += 1
        result_h -= 12

    if day != None:
        result_d = ((days_later % 7) + current_day) % 7

    # Output, padding
    str_result_h = str(result_h)
    str_result_m = ''
    str_result_d = ''
    str_result_ampm = ''

    if result_m < 10:
        str_result_m = '0' + str(result_m)
    else:
        str_result_m = str(result_m)

    for key, val in weekdays.items():
        if val == result_d:
            str_result_d = key

    if meridien == 'AM':
        str_result_ampm = 'AM'
    elif meridien == 'PM':
        str_result_ampm = 'PM'
    
    hour_result = f'{str_result_h}:{str_result_m} {str_result_ampm}'
    
    # Return statements depending on input
    if day == None:
        if days_later == 0:
            return hour_result
        elif days_later == 1:
            result_to_return = f'{hour_result} (next day)'
            return result_to_return
        elif days_later > 1:
            return f'{hour_result} ({days_later} days later)'
    else:
        if days_later == 0:
            return f'{hour_result}, {str_result_d.capitalize()}'
        elif days_later == 1:
            return f'{hour_result}, {str_result_d.capitalize()} (next day)'
        elif days_later > 1:
            return f'{hour_result}, {str_result_d.capitalize()} ({days_later} days later)'

add_time(testing, duration2)