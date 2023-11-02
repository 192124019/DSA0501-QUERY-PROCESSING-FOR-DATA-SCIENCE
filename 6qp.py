import pandas as pd
import matplotlib.pyplot as plt

# Load historical stock price data from the provided CSV file path
file_path = r"C:\Users\USER\Downloads\GoogleStockPrices.csv"  # Replace with your file path
df = pd.read_csv(file_path)

# Assuming your CSV has 'Date', 'Volume', and 'Close' columns, you may need to adjust column names
# Make sure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the date range you want to plot
start_date = '2021-04-01'
end_date = '2021-05-01'

# Filter the data for the specified date range
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Create a scatter plot for trading volume vs. stock prices
plt.figure(figsize=(12, 6))
plt.scatter(filtered_df['Volume'], filtered_df['Close'], color='royalblue', label='Trading Volume vs. Stock Price')
plt.title('Scatter Plot of Trading Volume vs. Stock Prices of Alphabet Inc. Stock')
plt.xlabel('Volume')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
