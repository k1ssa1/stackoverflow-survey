import pandas as pd

# Reading the survey results csv file
df = pd.read_csv('./data/survey_results_public.csv')

# Default row displau: only the first 5 rows
default_display = df.head()
print("****************Default display head****************")
print(default_display)

# Default row displau: only the last 5 rows
default_display = df.tail()
print("****************Default display tail****************")
print(default_display)

# Display the first 10 rows
first_ten = df.head(10)
print("****************first ten rows****************")
print(first_ten)

# Display the last 10 rows
last_ten = df.tail(10)
print("****************Last ten rows****************")
print(last_ten)

# Display all the columns
print(df.columns)

# Display a specific column
print(df['Gender'])

# Display a non duplicate values of a column
print(df['Gender'].value_counts())

# selecting rows
print("****************selecting multiple rows****************")
print(df.loc[[0,1,2]])
print("****************or****************")
print(df.loc[0:2])

# selecting rows
print("****************selecting first row****************")
print(df.loc[0, 'Gender'])

# selecting rows
print("****************selecting mutiple rows with multiple columns****************")
print(df.loc[0:2, 'ResponseId':'Employment'])