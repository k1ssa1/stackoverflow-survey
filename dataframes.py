import pandas as pd

people = {
    "fName": ["Sami","John","Jane"],
    "lName": ["Kissai","Doe","Doe"],
    "Age": [23,27,25],
    "job_title": ["CEO","CTO","CFO"]
}

df = pd.DataFrame(people)

print(df)