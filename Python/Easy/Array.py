import pandas as pd
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Create a list of month start dates from the current month until December 2030
date_range = pd.date_range(start=current_date.replace(day=1).date(), end="2030-12-01", freq='MS')

# Create a DataFrame with the month start dates
df = pd.DataFrame(date_range, columns=['Month_Start_Date'])

# Display the DataFrame
print(df.index[df['Month_Start_Date'] == '2023-12-01'][0])

current_time_str = datetime.now().strftime('%H:%M:%S')
print(f"Current Time: {current_time_str}")


# main_script.py
from log import SingletonLogger

# Get the logger instance
logger = SingletonLogger()

# Now you can use the logger in your file
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
   