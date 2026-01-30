import pandas as pd

HIGH_NULL_PERCENTAGE = 30

# Used AI to figure out encoding problems
df = pd.read_csv('sales_data_sample.csv', 
                 encoding='ISO-8859-1', 
                 keep_default_na=False, 
                 na_values=[''])

# Check high null percentages and drop them
print("The following columns have a high null percentage and will be dropped:", end = "\n\n")
for col_name, data in df.items():
    if (data.isnull().mean() * 100) > HIGH_NULL_PERCENTAGE:
        print(f"{col_name}: Null Percentage: {(data.isnull().mean() * 100):.2f}", end = "\n\n")
        df = df.drop(columns = [col_name])

# Hand Selected Columns to be Dropped
df = df.drop(columns = ['CONTACTLASTNAME'])
df = df.drop(columns = ['CONTACTFIRSTNAME'])
df = df.drop(columns = ['PHONE'])

df.to_csv('cleaned_sales_data.csv', index=False)