import pandas as pd

# Create a DataFrame from the provided data
data = {
    'OrderDate': ['1-6-18', '1-23-18', '2-9-18', '2-26-18', '3-15-18', '4-1-18', '4-18-18', '5-5-18', '5-22-18', '6-8-18', '6-25-18', '7-12-18', '7-29-18', '8-15-18', '9-1-18', '9-18-18', '10-5-18', '10-22-18'],
    'Region': ['East', 'Central', 'Central', 'Central', 'West', 'East', 'Central', 'Central', 'West', 'East', 'Central', 'East', 'East', 'East', 'Central', 'East', 'Central', 'East'],
    'Manager': ['Martha', 'Hermann', 'Hermann', 'Timothy', 'Timothy', 'Martha', 'Martha', 'Hermann', 'Douglas', 'Martha', 'Hermann', 'Martha', 'Douglas', 'Martha', 'Douglas', 'Hermann', 'Martha', 'Martha'],
    'SalesMan': ['Alexander', 'Shelli', 'Luis', 'David', 'Stephen', 'Alexander', 'Steven', 'Luis', 'Michael', 'Alexander', 'Sigal', 'Diana', 'Karen', 'Alexander', 'John', 'Alexander', 'Sigal', 'Alexander'],
    'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone', 'Television', 'Home Theater', 'Television', 'Television', 'Television', 'Home Theater', 'Television', 'Home Theater', 'Home Theater', 'Television', 'Desk', 'Video Games', 'Home Theater', 'Cell Phone'],
    'Units': [95, 50, 36, 27, 56, 60, 75, 90, 32, 60, 90, 29, 81, 35, 2, 16, 28, 64],
    'Unit_price': [1198.00, 500.00, 1198.00, 225.00, 1198.00, 500.00, 1198.00, 1198.00, 1198.00, 500.00, 1198.00, 500.00, 500.00, 1198.00, 125.00, 58.50, 500.00, 225.00],
    'Sale_amt': ['1,13,810.00', '25,000.00', '43,128.00', '6,075.00', '67,088.00', '30,000.00', '89,850.00', '1,07,820.00', '38,336.00', '30,000.00', '1,07,820.00', '14,500.00', '40,500.00', '41,930.00', '250.00', '936.00', '14,000.00', '14,400.00']
}

df = pd.DataFrame(data)

# Convert 'Sale_amt' column to numeric by removing commas
df['Sale_amt'] = df['Sale_amt'].str.replace(',', '', regex=True).astype(float)

# Create a Pivot table to find the item-wise unit sold
pivot_table = pd.pivot_table(df, values='Units', index='Item', aggfunc='sum')

# Print the item-wise unit sold
print("Item-Wise Unit Sold:")
print(pivot_table)
