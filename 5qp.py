import pandas as pd
import matplotlib.pyplot as plt

# Load historical stock price data from the provided CSV file path
file_path = r"C:\Users\USER\Downloads\GoogleStockPrices.csv"  # Replace with your file path
df = pd.read_csv(file_path)

# Assuming your CSV has 'Date' and 'Volume' columns, you may need to adjust column names
# Make sure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the date range you want to plot
start_date = '2004-08-19'
end_date = '2021-10-09'

# Filter the data for the specified date range
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Create a bar plot for trading volume
plt.figure(figsize=(12, 6))
plt.bar(filtered_df['Date'], filtered_df['Volume'], color='royalblue', label='Trading Volume')
plt.title('Trading Volume of Alphabet Inc. Stock')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.grid(axis='y')

# Show the plot
plt.show()
