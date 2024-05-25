# Tcalendar and Ttime

This project provides two classes, `Tcalendar` and `Ttime`, which allow for easy manipulation and handling of calendar dates and times in Python. 

## Introduction

- `Tcalendar`: This class represents a date on the calendar. It allows for the representation and manipulation of dates, including addition and subtraction of days, comparison of dates, and conversion to and from string representation.
  
- `Ttime`: This class represents a specific time of day. It allows for the representation and manipulation of time, including addition and subtraction of seconds, comparison of times, and conversion to and from string representation.

## Features

- **Tcalendar**
  - Creation of dates based on year, month, and day.
  - Leap year detection.
  - Getting the name of the month.
  - Finding the maximum number of days in a month.
  - Determining the day of the week.
  - Generating calendar pages.
  - Calculating the next and previous days.
  - Getting today's date.
  - Sorting dates.
  
- **Ttime**
  - Creation of times based on hour, minute, and second.
  - Switching between 12-hour and 24-hour formats.
  - Getting the current time.
  - Sorting times.

- **Tcalendar_time**
  - Combines features of `Tcalendar` and `Ttime` classes.
  - Creation of datetime objects with date and time components.
  - Addition and subtraction of datetime objects.
  - Comparison of datetime objects.
  - Conversion to and from string representation.

## Usage

Here's how you can use these classes in your Python code:

```python
from tcalendar_ttime import Tcalendar, Ttime

# Create a Tcalendar instance
date = Tcalendar(2024, 5, 24)

# Print the date
print(date)  # Output: 2024-05-24

# Create a Ttime instance
mytime = Ttime(13, 30, 0)
mytime.format12() # 12 hour formatting time

# Print the time
print(mytime)  # Output: 01:30:00 PM
```

## Installation
You can install the package using pip:

```
pip install tcalendar-ttime
```

## Examples
```
# Example: Adding days to a date
date = Tcalendar(2024, "May", 24)
new_date = date + 7

# Example: Sorting a list of dates
dates = [date, new_date, Tcalendar.today()]
sorted_dates = Tcalendar.sort(dates)

# Create a Tcalendar_time instance
datetime = Tcalendar_time(2024, 5, 24, 1, 30, 0)

# Print the datetime
print(datetime)  # Output: 2024-05-24 01:30:00 PM
```