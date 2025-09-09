import pandas as pd

details = {
    'NAME': ['ALICE', 'BOB', 'CHARLIE'],
    'AGE': [25, 30, 35],
    'SCORE': [88, 76, 91]
}

df=pd.DataFrame(details)

print(df)
print("first two rows:")
first_2_rows=df.head(2)
print(first_2_rows)
