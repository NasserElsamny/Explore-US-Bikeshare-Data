def main(): 

	import pandas as pd 

	CITY_DATA = { 'chicago': 'chicago.csv',
	              'new york city': 'new_york_city.csv',
	              'washington': 'washington.csv' }

	def get_filters() : 
		"""
			Asks user to specify a city, month, and day to analyze.

	    Returns:
		        (str) city - name of the city to analyze
		        (str) month - name of the month to filter by, or "all" to apply no month filter
		        (str) day - name of the day of week to filter by, or "all" to apply no day filter
	    """		
		print('Hello! Let\'s explore some US bikeshare data!')
		
		# get user input for city (chicago, new york city, washington).
		while True :
			city = input("Would you like to see data for Chicago , New York City or Washington \n").lower()
			if city in ['chicago' , 'new york city' , 'washington']:
				break
			else:
				print("\nInvalid city input please try again.\n")	
		
		# get user input for month (all, january, february, ... , june)
		while True :
			month = input("Would you like to filter by month?, enter(January ,February, March, April, May, June) for filter or enter /'all' for no month filter \n").lower()
			if month in ['january' , 'february' , 'march', 'april', 'may', 'june' , 'all']:
				break
			else:
				print("\nWrong month input please try again\n")

		# get user input for day of week (all, monday, tuesday, ... sunday)
		while True :
			day = input("Would you like to filter by day?, enter(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) or enter /'all' for no day filter \n").lower()
			if day in ['saturday' , 'sunday' , 'monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'all']:
				break
			else:
				print("\nWrong day input please try again\n")

		return city, month, day
	 
	city , month , day = get_filters()

	print('City: {} , Month: {} , Day: {}' .format(city , month, day))

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
		df['day_of_week'] = df['Start Time'].dt.weekday_name

		if month != 'all' :
			months = ['january', 'february', 'march', 'april', 'may', 'june']
			month = months.index(month) + 1
			df = df[df['month'] == month]

		if day != 'all' :
			df = df[df['day_of_week'] == day.title()]

		return df 

	df = load_data(city,month,day)

	def time_stats(df):
		"""Displays statistics on the most frequent times of travel."""
		
		months = ['january', 'february', 'march', 'april', 'may', 'june']
		df['month'] = df['Start Time'].dt.month
		popular_month1 = df['month'].mode()[0]
		print("The most common month is", months[popular_month1 - 1])
		
		df['day_of_week'] = df['Start Time'].dt.weekday_name
		print('The most common day of week is', df['day_of_week'].mode()[0])

		df['Start Time'] = pd.to_datetime(df['Start Time'])
		df['hour'] = df['Start Time'].dt.hour
		print('The most common hour of day is', df['hour'].mode()[0])

	time_stats(df)

	def station_stats(df):
		"""Displays statistics on the most popular stations and trip."""
		
		print("The most common start station is", df['Start Station'].mode()[0])
		print('The most common end station is', df['End Station'].mode()[0])
		df['Trip'] = df['Start Station'] + " to " + df['End Station']
		print('The most common trip is from',df['Trip'].mode()[0])

	station_stats(df)
	 
	def trip_duration_stats(df):
		"""Displays statistics on the total and average trip duration."""

		print("The total travel time is ", round(df['Trip Duration'].sum()) , 'seconds')
		print("The average travel time is ", round(df['Trip Duration'].mean()) , 'seconds')

	trip_duration_stats(df)

	def user_stats(df):
		"""Displays statistics on bikeshare users."""
		
		print("The counts of each user type are:\n", df['User Type'].value_counts())

		if city != 'washington':

			print('The counts of each gender are:\n', df['Gender'].value_counts())
			print('The earliest year of birth is ', int(df['Birth Year'].min()))
			print('The most recent year of birth is ', int(df['Birth Year'].max()))
			print('The most common year of birth is ', int(df['Birth Year'].mode()[0]))

	user_stats(df)		

	def view_data() :
		"""Asks user whether to view some rorws of raw data""" 
		
		view = input('Do you want to view 5 rows of raw data? Enter yes or no\n').lower()
		start = 0
		while view == 'yes' :
			pd.set_option('display.max_columns',200)
			print(df.iloc[start:start+5])
			start += 5
			view= input('Do you want to view another 5 rows? Enter yes or no\n').lower()

	view_data()

	while True:
		restart = input("Do you want to start again? Enter yes or no\n")
		if restart == 'yes':
			main()
			break
		if restart == 'no':
			exit()
			break
		else:
			print("\nInvalid input pleas try again\n")

main()