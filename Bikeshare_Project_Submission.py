## TODO: import all necessary packages and functions
import csv
import time
import pprint
import datetime
import calendar
from itertools import islice

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York City, or Washington?\n')
        # TODO: handle raw input and complete function
        city_file = ""
        if city.lower() == 'chicago':
            print ('The filename for {} is {}'.format(city, chicago))
            city_file = chicago
            return (str(city_file))
        elif city.lower() == 'new york city':
            print('The filename for {} is {}'.format(city, new_york_city))
            city_file = new_york_city
            return (str(city_file))
        elif city.lower() == 'washington':
            print ('The filename for {} is {}'.format(city, washington))
            city_file = washington
            return (str(city_file))
        else:
            print ('Enter one of the 3 mentioned cities')


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Respected time period per user input
    '''
    while True:
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')
        # TODO: handle raw input and complete function

        if time_period.lower() == 'month':
            print ("You chose {}".format(time_period))
            return time_period
        elif time_period.lower() == 'day':
            print ("You chose {}".format(time_period))
            return time_period
        elif time_period.lower() == 'none':
            print ("You chose {}".format(time_period))
            return time_period
        else:
            print("Invalid input. PLease enter month, day or none")

def get_month(city_file):
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        # TODO: handle raw input and complete function

        count = 0


        if month.lower() == 'january' or month.lower() == 'february' or month.lower() == 'march' or month.lower() == 'april' or month.lower() == 'may' or month.lower() == 'june':
            print ("You chose {}".format(month.title()))
            print(city_file)
            if city_file[-11:-4].lower() == 'chicago' or city_file[-17:-4].lower() == 'new_york_city':
                with open(city_file, 'r') as selected_city:
                    reader = csv.DictReader(selected_city)

                    write_file = 'filtered_month_cityfile.csv'
                    with open(write_file, 'w') as new_city_file:
                        fieldnames_file = ['', 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']
                        writer = csv.DictWriter(new_city_file, fieldnames = fieldnames_file, extrasaction='ignore')
                        writer.writeheader()

                        for row in reader:
                            date_time_strp = datetime.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S")
                            x = date_time_strp.strftime("%B")
                            if x.lower() == month.lower():
                                count += 1
                                writer.writerow(row)
                return (write_file)

            elif city_file[-14:-4].lower() == 'washington':
                with open(city_file, 'r') as selected_city:
                    reader = csv.DictReader(selected_city)

                    write_file = 'filtered_month_cityfile_washington.csv'
                    print(write_file)
                    with open(write_file, 'w') as new_city_file:
                        fieldnames_file = ['', 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']

                        writer = csv.DictWriter(new_city_file, fieldnames = fieldnames_file, extrasaction='ignore')
                        writer.writeheader()

                        for row in reader:
                            date_time_strp = datetime.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S")
                            x = date_time_strp.strftime("%B")
                            if x.lower() == month.lower():
                                count += 1
                                writer.writerow(row)
                return (write_file)
        else:
            print ("{} is an Invalid input".format(month))


def get_day(city_file):
    '''Asks the user for a day as an integer(0-6) and returns the specified weekday.

    Args:
        city_file
    Returns:
        (str) City bikeshare data filtered with respect to day
    '''
    # TODO: handle raw input and complete function
    while True:
        while True:
            try:
                day = int(input ('\nWhich day? Please type your response as an integer.\n'))
                break
            except ValueError:
                print('Invalid Input! Please enter a number.')
        count = 0

        if day >= 0 and day <= 6:
            print ("You chose {}".format(calendar.day_name[day]))
            #print(calendar.day_name[day])
            #print(city_file)
            if city_file[-11:-4] == 'chicago' or city_file[-17:-4] == 'new_york_city':
                with open(city_file, 'r') as selected_city:
                    reader = csv.DictReader(selected_city)

                    write_file = 'filtered_day_cityfile.csv'
                    with open(write_file, 'w') as new_city_file:
                        fieldnames_file = ['', 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']
                        writer = csv.DictWriter(new_city_file, fieldnames = fieldnames_file, extrasaction='ignore')
                        writer.writeheader()
                        for row in reader:
                            date_time_strp = datetime.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S")
                            x = date_time_strp.strftime("%A")
                            if x.lower() == calendar.day_name[day].lower():
                                count += 1
                                writer.writerow(row)
                return (write_file)

            elif city_file[-14:-4] == 'washington':
                with open(city_file, 'r') as selected_city:
                    reader = csv.DictReader(selected_city)

                    write_file = 'filtered_day_cityfile_washington.csv'
                    with open(write_file, 'w') as new_city_file:
                        fieldnames_file = ['', 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']

                        writer = csv.DictWriter(new_city_file, fieldnames = fieldnames_file, extrasaction='ignore')
                        writer.writeheader()

                        for row in reader:
                            date_time_strp = datetime.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S")
                            x = date_time_strp.strftime("%A")
                            if x.lower() == calendar.day_name[day].lower():
                                count += 1
                                writer.writerow(row)
                return (write_file)
        else:
            print("Invalid input, Enter an integer between 0 and 6")

def popular_month(city_file, time_period):
    ''' Question: What is the most popular month for start time?
    Args:
        city_file, time_period
    Returns:
        (str) Most popular month in requested City bikeshare data
    '''
    # TODO: complete function

    with open(city_file, 'r') as selected_city:
        reader = csv.DictReader(selected_city)
        list_months = []
        months_count = {}
        for row in reader:
            date_time_strp = datetime.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S")
            x = date_time_strp.strftime("%B")
            list_months.append(x)
        for month in  list_months:
            if month in months_count:
                months_count[month] += 1
            else:
                months_count[month] = 1
    #print(months_count)

    max_value = max(months_count.values())
    max_keys = [k for k, v in months_count.items() if v == max_value]
    print("The most Popular Month is {} ".format(max_keys[0]))
    return (max_keys[0])

def popular_day(city_file, time_period):
    '''Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Args:
        city_file, time_period
    Returns:
        (str) Most popular weekday in requested City bikeshare data
    '''
    # TODO: complete function

    with open(city_file, 'r') as selected_city:
        reader = csv.DictReader(selected_city)
        list_weekdays = []
        weekdays_count = {}
        for row in reader:
            date_time_strp = datetime.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S")
            x = date_time_strp.strftime("%A")
            list_weekdays.append(x)
        for weekday in  list_weekdays:
            if weekday in weekdays_count:
                weekdays_count[weekday] += 1
            else:
                weekdays_count[weekday] = 1
    #print(weekdays_count)

    max_value = max(weekdays_count.values())
    max_keys = [k for k, v in weekdays_count.items() if v == max_value]
    print("The most Popular Weekday is {} ".format(max_keys[0]))
    return (max_keys[0])


def popular_hour(city_file, time_period):
    '''Question: What is the most popular hour of day for start time?
    Args:
        city_file, time_period
    Returns:
        (str) Most popular start time hour in requested City bikeshare data
    '''
    # TODO: complete function
    with open(city_file, 'r') as selected_city:
        reader = csv.DictReader(selected_city)
        list_hour = []
        hour_count = {}
        for row in reader:
            date_time_strp = datetime.datetime.strptime(row['Start Time'], "%Y-%m-%d %H:%M:%S")
            x = date_time_strp.strftime("%H")
            list_hour.append(x)
        for hour in  list_hour:
            if hour in hour_count:
                hour_count[hour] += 1
            else:
                hour_count[hour] = 1
    #print(hour_count)

    max_value = max(hour_count.values())
    max_keys = [k for k, v in hour_count.items() if v == max_value]
    print("The most Popular hour is {} ".format(max_keys[0]))
    return (max_keys[0])


def trip_duration(city_file, time_period):
    '''Question: What is the total trip duration and average trip duration?
    Args:
        city_file, time_period
    Returns:
        (Int/Float) Total and Average trip duration in requested City bikeshare data
    '''
    # TODO: complete function
    with open(city_file, 'r') as selected_city:
        reader = csv.DictReader(selected_city)
        total_trip_duration = []
        total_len_count = 0
        for row in reader:
            if washington:
                row_wash = int(float(row['Trip Duration']))
                total_trip_duration.append(row_wash)
                total_len_count += 1
            else:
                total_trip_duration.append(int(row['Trip Duration']))
                total_len_count += 1

        total_trip_duration = sum(list(total_trip_duration))
        avg_trip_duration = total_trip_duration/total_len_count
        print('Total trip duration is {} '.format(total_trip_duration))
        #print(total_len_count)
        print('Average trip duration is {} '.format(avg_trip_duration))

    return (total_trip_duration, avg_trip_duration)

def popular_stations(city_file, time_period):
    '''Question: What is the most popular start station and most popular end station?
    Args:
        city_file, time_period
    Returns:
        (str) Most popular start station and most popular end station from the requested City bikeshare data
    '''
    # TODO: complete function
    with open(city_file, 'r') as selected_city:
        reader = csv.DictReader(selected_city)
        list_station_start = []
        list_station_end = []
        station_count_start = {}
        station_count_end = {}
        for row in reader:
            list_station_start.append(row['Start Station'])
            list_station_end.append(row['End Station'])
        for station in  list_station_start:
            if station in station_count_start:
                station_count_start[station] += 1
            else:
                station_count_start[station] = 1
        for station in  list_station_end:
            if station in station_count_end:
                station_count_end[station] += 1
            else:
                station_count_end[station] = 1

    #print(station_count_start)
    #print(station_count_end)

    max_value_start = max(station_count_start.values())
    max_keys_start = [k for k, v in station_count_start.items() if v == max_value_start]
    print("The most Popular Start station is {} and count is {} ".format(max_keys_start[0], max_value_start))
    return (max_keys_start[0])

    max_value_end = max(station_count_end.values())
    max_keys_end = [k for k, v in station_count_end.items() if v == max_value_end]
    print("The most Popular end station is {} and count is {} ".format(max_keys_end[0], max_value_end))
    return (max_keys_end[0])

def popular_trip(city_file, time_period):
    '''Question: What is the most popular trip?
    Args:
        city_file, time_period
    Returns:
        (str) Most popular trip from the requested City bikeshare data
    '''
    # TODO: complete function
    with open(city_file, 'r') as selected_city:
        reader = csv.DictReader(selected_city)
        trip_Start_Station_list = []
        trip_End_Station_list = []
        popular_trip = {}

        for row in reader:
            trip_Start_Station_list.append(row['Start Station'])
            trip_End_Station_list.append(row['End Station'])

        Start_End_pair = list(zip(trip_Start_Station_list, trip_End_Station_list))

        for pair in Start_End_pair:
            if pair in popular_trip:
                popular_trip[pair] += 1
            else:
                popular_trip[pair] = 1

        #print(popular_trip)

        max_value_popular_trip = max(popular_trip.values())
        max_keys_popular_trip = [k for k, v in popular_trip.items() if v == max_value_popular_trip]
        print("The most Popular Start station is {} and count is {} ".format(max_keys_popular_trip[0], max_value_popular_trip))

    return (max_keys_popular_trip[0])

def users(city_file, time_period):
    '''Question: What are the counts of each user type?
    Args:
        city_file, time_period
    Returns:
        (Dict) Counts of usertype from the requested City bikeshare data
    '''
    # TODO: complete function
    with open(city_file, 'r') as selected_city:
        reader = csv.DictReader(selected_city)
        user_list = []
        user_type_dict = {}
        for row in reader:
            user_list.append(row['User Type'])

        for each in user_list:
            if each in user_type_dict:
                user_type_dict[each] += 1
            else:
                user_type_dict[each] = 1

        #print(user_type_dict)

    print('The counts of each user type are', user_type_dict)
    return (user_type_dict)

def gender(city_file, time_period):
    '''Question: What are the counts of gender?
    Args:
        city_file, time_period
    Returns:
        (Int) Counts of gender from the requested City bikeshare data
    '''
    # TODO: complete function
    gender_list = []
    gender_type_dict = {}
    if city_file[-14:-4] == 'washington' or city_file == 'filtered_month_cityfile_washington.csv' or city_file == 'filtered_day_cityfile_washington.csv' :
        print ('Washingtom city file has no Gender column hence cannot compute statistics')
        return
    else:
        with open(city_file, 'r') as selected_city:
            reader = csv.DictReader(selected_city)
            for row in reader:
                gender_list.append(row['Gender'])

            for each in gender_list:
                if each in gender_type_dict:
                    gender_type_dict[each] += 1
                else:
                    gender_type_dict[each] = 1

        print('The counts of Male is {} and the count of Female is {} '.format(gender_type_dict['Male'], gender_type_dict['Female']))

        return (gender_type_dict)

def birth_years(city_file, time_period):
    '''Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Args:
        city_file, time_period
    Returns:
        (str) Birth years from the requested City bikeshare data
    '''
    # TODO: complete function
    birth_year_list = []
    years = []
    year_popular = {}
    if city_file[-14:-4] == 'washington' or city_file == 'filtered_month_cityfile_washington.csv' or city_file == 'filtered_day_cityfile_washington.csv':
        print ('Washingtom city file has no Birth year column hence cannot compute statistics')
        return
    else:
        with open(city_file, 'r') as selected_city:
            reader = csv.DictReader(selected_city)
            for row in reader:
                birth_year_list.append(row['Birth Year'])

            for year in birth_year_list:
                if year != '':
                    years.append(int(float(year)))

            for year in years:
                if year in year_popular:
                    year_popular[year] += 1
                else:
                    year_popular[year] = 1

        max_value = max(year_popular.values())
        max_keys = [k for k, v in year_popular.items() if v == max_value]
        print("The most Popular birth year is {} ".format(max_keys[0]))
        print("The most Popular year is {} ".format(max_keys[0]))
        pop_year = max_keys[0]
        young_year = max(years)
        old_year = min(years)

        #print(birth_year_list)
        print(pop_year)
        print("The most recent user's birth year is {} ".format(young_year))
        print("The oldest user's birth year is {} ".format(old_year))
    return(old_year, young_year, pop_year)

def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    #display = input('\nWould you like to view individual trip data?''Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    #counter = 0
    print ('mark', city_file)
    with open(city_file, 'r') as selected_city1:
        while True:
            display = input('\nWould you like to view individual trip data?'
                        'Type \'yes\' or \'no\'.\n')
            print(display)
            if display == 'yes':
                csvReader1 = csv.reader(selected_city1)
                for line_number, row in zip(range(5), csvReader1):
                    print(row)
            else:
                break
    return

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print('city is', city)

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    #print ('NOTE : time period is', time_period)

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        popular_month(city, time_period)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        if time_period == 'month':
            city = get_month(city)

        # TODO: call popular_day function and print the results
        popular_day(city, time_period)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    if time_period == 'none' or time_period == 'month' or time_period == 'day':
        start_time = time.time()
        if time_period == 'day':
            city = get_day(city)

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(city, time_period)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years(city, time_period)
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    print('display city', city)
    display_data(city)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
