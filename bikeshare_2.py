import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which City would you like to analyze? You can choose chicago, new york city or washington. ").lower()
        if not city == "chicago" and not city == "new york city" and not city == "washington":
            print("That is not a valid response, please choose from the options.")
            continue
        else:
            print("Ok!")
            break 

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to look at: january, february, march...june or all? ").lower()
        if month in ('january','february','march','april','may','june', 'all'):
            break
        else:
            print("Invalid response. Please input the full name of the month.")
            continue

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Would you like to look at a specific day? Please type your response as an integer (e.g, 1 = Sunday) or type 'all' for all days. ")
        if day in ('1', '2', '3', '4', '5', '6', '7', 'all'):
            break
        else:
            print("Invalid response. Please enter integer values from 1 to 7 or 'all'")
            continue

    print(city.title())
    print(month.title())
    print(day)

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 
        df = df[df['month'] == month] 
    if day != 'all':
        days = ['1', '2', '3', '4', '5', '6', '7']
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
       
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print("The most popular month is " + str(popular_month) + ".")
    print("The most popular day of the week is " + str(popular_day_of_week) + ".")
    print("The most popular hour is " + str(popular_hour) + ".")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    
    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station','End Station']).size().nlargest()
    print("The most commonly used start station is " + most_common_start_station + ".")
    print("The most commonly used end station is " + most_common_end_station + ".")
    print("The most frequent combination of start station and end station trip is \n\n" + str(most_frequent_combination) + ".")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("The total travel time is " + str(total_travel_time) + ".")
    print("The mean travel time is " + str(mean_travel_time) + ".")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()  
    print("The number of user types is \n" + str(user_type))
    # TO DO: Display counts of gender
    if city == "new york city" or city == "chicago":
        count_of_gender = df['Gender'].nunique()
        print("The counts of gender is " + str(count_of_gender) + ".")
    # TO DO: Display earliest, most recent, and most common year of birth
    if city == "new york city" or city == "chicago":
        
        df['Birth Year'] = pd.to_datetime(df['Birth Year'])
        least_recent_date = df['Birth Year'].min()
        most_recent_date = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("The earliest birth year is " + str(least_recent_date) + ", the most recent birth year is " + str(most_recent_date) + " and the most common year of birth is " + str(most_common_year) + ".")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_disp(df):
    start = 0
    while True:
        user_input = input('Do you want to see the raw data? Enter yes or no. ')
        if user_input.lower() == 'yes':
            five_rows = df.iloc[:start+5]
            print(five_rows)
            start += 5
        elif user_input.lower() != 'no':
            print('Incorrect input. Please try again.')
            
                     
        else:
            break    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data_disp(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
   

if __name__ == "__main__":
	main()
