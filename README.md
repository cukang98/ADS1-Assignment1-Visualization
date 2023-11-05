# ADS1-Assignment1-Visualization

## Singapore Housing Market Data Visualization
This data visualization project explores and presents insights from the Singapore housing market using Python, Pandas, and Matplotlib. The project is divided into several visualizations, each providing a unique perspective on the housing market trends in Singapore.
source: https://beta.data.gov.sg/collections/189/view

## NOTE: Data Preparation

The original dataset for this project consists of five separate files. To create a consolidated dataset for analysis, we used the `merge_datasets.py` program. This program merged the original datasets and added an additional column that categorizes each town into different areas. The areas include "North," "East," "Central," "North-East," and "West," enabling more focused analysis and visualization.

For more details on the data preparation process and how the area categorization was performed, refer to the `merge_datasets.py` script in the project repository.

## Visualizations
### 1. Time Series of Resale Prices by Area
This visualization offers a time series analysis of resale prices by area over the years. It helps to track the average resale prices in different regions of Singapore and observe price trends. The plot uses a variety of line styles and colors for each area, providing a visually appealing and informative representation of historical resale prices.

### 2. Distribution of Flats by Town
This pie chart illustrates the distribution of transactions by town, highlighting the proportion of transactions in different areas. Each town is color-coded for easy reference, making it a concise and informative visualization of the distribution of flats among towns.

### 2.1 Distribution of Towns in "North" and "West" Areas
Building on the previous visualization, this pie chart narrows the focus to the "North" and "West" areas. It displays the distribution of towns within these two regions, providing a clear picture of where most transactions occur in these areas.

### 3. Distribution of Property Types
This bar chart presents the distribution of different property types in the dataset, including "1 ROOM," "3 ROOM," and more. Each property type is represented as a bar, and the exact count is displayed on top of each bar. This visualization helps to understand the variety of property types in the Singapore housing market.

### Usage
To run this project and generate the visualizations, make sure you have Python, Pandas, and Matplotlib installed on your local machine. You can customize and adapt the code to analyze other datasets or explore different aspects of the Singapore housing market.

Credits
Pandas - Data manipulation library
Matplotlib - Data visualization library
License
This project is open-source and available under the MIT License.
