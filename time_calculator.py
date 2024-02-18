testing = '11:02 AM'
duration2 = '424:02'

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
    is_AM = None
    days_later = 0

    # Extracting start and duration time
    start_tuple = extract_time_to_tuple(start)
    duration_tuple = extract_time_to_tuple(duration)
    
    # Main time calculations
    if start_tuple[2] == 'AM':
        is_AM = True
    elif start_tuple[2] == 'PM':
        is_AM = False

    result_h = start_tuple[0] + duration_tuple[0]
    result_m = start_tuple[1] + duration_tuple[1]
    
    while result_m > 60:
        result_m -= 60
        result_h += 1

    while result_h > 12:
        if is_AM == True:
            is_AM = False 
        else:
            is_AM = True
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

    if is_AM == True:
        str_result_ampm = 'AM'
    elif is_AM == False:
        str_result_ampm = 'PM'
    
    hour_result = (f'{str_result_h + ':' + str_result_m + ' ' + str_result_ampm}')

    print(days_later)
    if day == None:
        if days_later == 0:
            print(hour_result)
        elif days_later == 1:
            print(f'{hour_result} (next day)')
        elif days_later > 1:
            print(f'{hour_result} ({days_later} days later)')
    else:
        if days_later == 0:
            print(f'{hour_result}, {str_result_d.capitalize()}')
        elif days_later == 1:
            print(f'{hour_result}, {str_result_d.capitalize()} (next day)')
        elif days_later > 1:
            print(f'{hour_result}, {str_result_d.capitalize()} ({days_later} days later)')

add_time(testing, duration2, 'Monday')