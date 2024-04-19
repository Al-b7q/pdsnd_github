#importing needed libraries

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#creatign needed functions

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    CITIES = ('chicago', 'new york city', 'washington')
    MONTHS = ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
    DAYS_OF_WEEK = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


    city = input('Would you like to see data for Chicago, New York City, or, Washington?\n').lower()
    while city not in CITIES:
          city = input('Please try again ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter the desired month (all, January, February, ..., June):\n').lower()
    while month not in MONTHS:
        month = input('Please try again ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter the desired day of week (all, monday, tuesday, ... sunday):\n').lower()
    while day not in DAYS_OF_WEEK:
        day = input('Please try again ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    MONTHS = ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print(f'The most common month is {MONTHS[most_common_month]}')

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print(f'The most common day of week is {most_common_day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].value_counts().idxmax()
    
    print(f'The most common hour is {most_common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print(f'The most common start staion is {most_common_start_station}')


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print(f'The most common end station is {most_common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'The most frequent combination of start station and end station trip is {most_frequent_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'The total travel time is {total_travel_time / 3600}')

    # TO DO: display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    print(f'The mean travel time is {total_travel_time / 3600}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f'The count of user types is \n {user_types}')

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print(f'The count of user types is \n {gender}')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_yob = df['Birth Year'].min()
    most_recent_yob = df['Birth Year'].max()
    most_common_yob = df['Birth Year'].value_counts().idxmax()
    print(f'The earliest year of birth is {earliest_yob:.0f}')
    print(f'The most recent year of birth is {most_recent_yob:.0f}')
    print(f'The most common year of birth is {most_common_yob:.0f}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """ Displays the raw data upon request by the user """
    x = 0
    user_input = input('Would you like to view the raw data ? Type Yes or No ').title() 
    while user_input != 'No':
            if user_input == 'Yes':
                if x < df.shape[0]:
                    x += 5
                    rows = df.head(x)
                    print(rows.tail())
                    user_input = input('Would you like to view the raw data ? Type Yes or No ').title()
                else:
                    print('No more rows')
                    break
            else:
                user_input = input('Please try agian, Type Yes or No ').title()

    
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
