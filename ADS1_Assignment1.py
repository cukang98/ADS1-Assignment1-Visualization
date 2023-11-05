import pandas as pd
import matplotlib.pyplot as plt

# Constants for title and label styling
TITLE_STYLE = {'fontsize': 14, 'weight': 'bold'}
LABEL_STYLE = {'fontsize': 12}

# Visualization 1: Time Series of Resale Prices by Area (Grouped by Year)
file_path = 'ResaleFlatPrices1990toCurrent.csv'
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Convert the 'month' column to datetime format
df['month'] = pd.to_datetime(df['month'])

# Extract the year from the 'month' column and create a new 'year' column
df['year'] = df['month'].dt.year

# Group data by 'area', 'year', and calculate the mean resale price
area_price_data = df.groupby(['area', 'year'])['resale_price'].mean().unstack()

# Transpose the DataFrame to have years as columns
area_price_data = area_price_data.T

# Create time series line plots for each area with styling
plt.figure(figsize=(12, 6))

# Define a list of line styles and colors for styling the plot
line_styles = ['-', '--', '-.', ':']
line_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for i, area in enumerate(area_price_data.columns):
    style = line_styles[i % len(line_styles)]
    color = line_colors[i % len(line_colors)]
    plt.plot(area_price_data.index, area_price_data[area], label=area, linestyle=style, color=color, linewidth=2)

# Set title and labels
plt.title('Resale Prices Over Time by Area', **TITLE_STYLE)
plt.xlabel('Year', **LABEL_STYLE)
plt.ylabel('Average Resale Price', **LABEL_STYLE)

# Customize the legend
plt.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white')

# Display a grid with dashed lines
plt.grid(linestyle='--', alpha=0.7)

# Display the plot with a shadow
plt.box(on=None)
plt.show()

# Visualization 2: Distribution of Transactions by Town
# Group the data by town and count the number of transactions in each town
town_counts = df['area'].value_counts()

# Define a list of colors for the towns (5 colors)
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow', 'lightpink']

# Create a pie chart
plt.figure(figsize=(12, 9))
plt.pie(town_counts, labels=town_counts.index, autopct='%1.1f%%', startangle=140, shadow=True, colors=colors)
plt.title('Distribution of Transactions by Town', **TITLE_STYLE)
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle

# Show the pie chart
plt.show()

# Visualization 2.1: Distribution of Towns in "North" and "West" Areas
# Filter the data for the "North" and "West" areas
north_west_data = df[df['area'].isin(['North', 'West'])]

# Get the count of town names within these areas
town_counts = north_west_data['town'].value_counts()

# Define colors for "North" and "West" areas
colors = ['lightskyblue', 'lightcoral']

# Create a pie chart with color-coding
plt.figure(figsize=(8, 10))
plt.pie(town_counts, labels=town_counts.index, autopct='%1.1f%%', startangle=140, shadow=True, colors=colors)

# Add a legend to clarify the colors
plt.legend(['North', 'West'], title="Areas", loc="upper right", bbox_to_anchor=(1, 1))

plt.title('Distribution of Towns in "North" and "West" Areas', **TITLE_STYLE)
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle

# Show the pie chart
plt.show()

# Visualization 3: Distribution of Property Types
# Calculate the count of each property type
property_type_counts = df['flat_type'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 6))
property_type_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Property Types', **LABEL_STYLE)
plt.ylabel('Count', **LABEL_STYLE)
plt.title('Distribution of Property Types', **TITLE_STYLE)
plt.xticks(rotation=45, **LABEL_STYLE)
plt.yticks(**LABEL_STYLE)

# Add text labels on top of each bar
for i, count in enumerate(property_type_counts):
    plt.text(i, count, str(count), ha='center', va='bottom', **LABEL_STYLE, color='darkblue', weight='bold')

# Add grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

# Show the bar chart
plt.show()
