import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'ID': ['A1', 'A2', 'A3'],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 95]
})

# Set the first column as the index
df.set_index(df.columns[0], inplace=True)

print(df)