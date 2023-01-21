import pandas as pd

people = {
    "fName": ["Sami","John","Jane"],
    "lName": ["Kissai","Doe","Doe"],
    "Age": [23,27,25],
    "job_title": ["CEO","CTO","CFO"]
}

# displaying the entire dataframes
df = pd.DataFrame(people)

# accesing series in dataframes in two ways
serie1 = df['lName']
serie2 = df.job_title

# accesing multiple series
multi_series = df[["lName","fName"]]

# displaying colums of a dataframe
col = df.columns

# columns accessing using loc and iloc
iloc_display = df.iloc[[0,1],[1]]
loc_display = df.loc[[0,1],"lName"]

# printing the display
print("******* displaying the dataframe *******")
print(df)
print("\n")
print("******* displaying the first serie *******")
print(serie1)
print("\n")
print("******* displaying the second serie *******")
print(serie2)
print("\n")
print("******* displaying multi serie *******")
print(multi_series)
print("\n")
print("******* displaying the columns of a dataframe *******")
print(col)
print("\n")
print("******* iloc display of the 2 first row and the second column*******")
print(iloc_display)
print("\n")
print("******* loc display of the 2 first row and the second column*******")
print(loc_display)
print("\n")