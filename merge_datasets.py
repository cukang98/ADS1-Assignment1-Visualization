# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import pandas as pd
import os

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# List of Excel files to merge
file_list = ['ResaleFlatPricesBasedonApprovalDate19901999.csv', 
             'ResaleFlatPricesBasedonApprovalDate2000Feb2012.csv', 
             'ResaleFlatPricesBasedonRegistrationDateFromJan2015toDec2016.csv', 
             'ResaleFlatPricesBasedonRegistrationDateFromMar2012toDec2014.csv', 
             'ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv']

# Create a mapping of towns to areas
town_to_area = {
    'ANG MO KIO': 'North',
    'BEDOK': 'East',
    'BISHAN': 'Central',
    'BUKIT BATOK': 'West',
    'BUKIT MERAH': 'Central',
    'BUKIT TIMAH': 'Central',
    'CENTRAL AREA': 'Central',
    'CHOA CHU KANG': 'West',
    'CLEMENTI': 'West',
    'GEYLANG': 'Central',
    'HOUGANG': 'North-East',
    'JURONG EAST': 'West',
    'JURONG WEST': 'West',
    'KALLANG/WHAMPOA': 'Central',
    'MARINE PARADE': 'Central',
    'QUEENSTOWN': 'Central',
    'SENGKANG': 'North-East',
    'SERANGOON': 'North-East',
    'TAMPINES': 'East',
    'TOA PAYOH': 'Central',
    'WOODLANDS': 'North',
    'YISHUN': 'North',
    'LIM CHU KANG': 'North',
    'SEMBAWANG': 'North',
    'BUKIT PANJANG': 'West',
    'PASIR RIS': 'East',
    'PUNGGOL': 'North-East'
}

for file in file_list:
    if os.path.isfile(file):
        # Read the Excel file into a DataFrame
        df = pd.read_csv(file)
        df['area'] = df['town'].map(town_to_area)
        
        # Concatenate the data, ignoring index
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged data to a new Excel file
merged_data.to_csv('ResaleFlatPrices1990toCurrent.csv', index=False)
