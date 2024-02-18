# Rules
# Function takes 3 arguments.
# 1. A start time in the 12-hour clock format (ending in AM or PM)
# 2. A duration time that indicates the number of hours and minutes
# 3. (optional) a starting day of the week, case insensitive

# 1. Do not import any Python libraries.
# 2. Assume that the start times are valid times.
# 3. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

testing = '3:12 AM'
duration2 = '2:32'

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
        
    start_tuple = extract_time_to_tuple(start)
    duration_tuple = extract_time_to_tuple(duration)

    

add_time(testing, duration2)