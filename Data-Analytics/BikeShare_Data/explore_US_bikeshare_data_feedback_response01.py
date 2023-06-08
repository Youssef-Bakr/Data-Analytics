#################################################################################################

#################################################################################################
import time
import pandas as pd
import numpy as np
#################################################################################################

#################################################################################################
CITY_DATA = {"Chicago": "chicago.csv",
              "New York City": "new_york_city.csv",
              "Washington": "washington.csv"}
#################################################################################################

#################################################################################################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some (Chicago, New York City, Washington) bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
             city = input(
                 " Please write the name of the city, you would like to view it's statistics for Bike Share. \n\nwrite one of the following: Chicago, New York City, Washington \n")
             city = city.title()
             if city not in ("Chicago", "New York City", "Washington"):
                  print(
                      "No match for what you had enter, write one of the following\n(chicago, new york city, washington)\n")
                  continue
             else:
                  break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
            month = input("\n Which month would you like to view it's statistics for Bike Share \n\n(January, February, ...., or write All)\n")
            month = month.title()
            if month not in ("January", "February", "March", "April", "May", "June","July","August", "September","October","November", "December", "All"):
                  print("No match for what you had enter, \n\nwrite one of the following:\n(January, February, ...., or write All) \n")                   
                  continue
            else:
                  break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
               day = input("Which Day would you like to view it's statistics for Bike Share:\n\n( Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type All).\n\n\n")
               day = day.title()
               if day not in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "All"):
                  print("\n No match for what you had enter, \n\nwrite one of the following: \nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, All \n")
                  continue
               else:
                  break
    print("-=-"*40)
    return city, month, day
#################################################################################################

#################################################################################################
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
# loading data file into the DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # converting the Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extracting month and day of week from Start Time to create new columns

    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
  
    # filtering by month if available
    if month != "All":
   	 	# using the index of the months list to get the corresponding int
        months = ["January", "February", "March", "April", "May", "June","July","August", "September","October","November", "December"]
        month = months.index(month) + 1

    	# filtering by month to create the new DataFrame
        df = df[df["month"] == month]

        # filtering by day of week if available
    if day != "All":
        # filtering by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]

    return df
#################################################################################################

#################################################################################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df["month"].mode()[0]
    print("The Most Common Month:", popular_month)

    # TO DO: display the most common day of week
    popular_day = df["day_of_week"].mode()[0]
    print("The Most Common day:", popular_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The Most Common Hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-=-"*40)
#################################################################################################

#################################################################################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df["Start Station"].value_counts().idxmax()
    print("The Most Commonly used start station:", Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df["End Station"].value_counts().idxmax()
    print("\nThe Most Commonly used end station:", End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combine_Station = df.groupby(["Start Station", "End Station"]).count()
    print("\nThe Most Commonly used pair of start station and end station trip:", Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-=-"*40)
#################################################################################################

#################################################################################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print("The Total travel time:", Total_Travel_Time/86400, " Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df["Trip Duration"].mean()
    print("Mean travel time:", Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-=-"*40)
#################################################################################################

#################################################################################################
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print("\nCalculating User Stats...\n")
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df["User Type"].value_counts()
    #print(user_types)
    print("User Counts:\n", user_types_count)

    # TO DO: Display counts of gender
    try:
      gender_count = df["Gender"].value_counts()
      print("\nGender Counts:\n", gender_count)
    except KeyError:
      print("\nGender Counts:\nNo data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Birth_Year = df["Birth Year"].min()
      print("\nEarliest Birth Year:", Earliest_Birth_Year)
    except KeyError:
      print("\nEarliest Birth Year:\nNo data available.")

    try:
      Most_Recent_Birth_Year = df["Birth Year"].max()
      print("\nMost Recent Birth Year:", Most_Recent_Birth_Year)
    except KeyError:
      print("\nMost Recent Birth Year:\nNo data available.")

    try:
      Most_Common_Birth_Year = df["Birth Year"].value_counts().idxmax()
      print("\nMost Common Birth Year:", Most_Common_Birth_Year)
    except KeyError:
      print("\nMost Common Birth Year:\nNo data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("-=-"*40)
#################################################################################################
#explore_US_bikeshare_data_feedback_response01
#################################################################################################
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        view_data = input("\nWould you like to view 5 rows of individual trip data? \n\nEnter Yes or No\n")
        view_data = view_data.title()
        start_loc = 0
        while (view_data == "Yes"):
               print(df.iloc[start_loc:start_loc+5])
               start_loc += 5
               view_data = input("\nWould you like to view 5 more rows of individual trip data? \n\nEnter Yes to view more 5 rows \nor No to move forward and view statistics\n").title()






        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break

#################################################################################################

#################################################################################################
if __name__ == "__main__":
	main()
#################################################################################################
