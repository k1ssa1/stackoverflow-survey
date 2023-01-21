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