# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 9, 2026
# | Last update..: March 9, 2026
# | WhatIs.......: Bacteria Analysis with Pandas - Main
# +----------------------------------------------------------------------------++
# ------------------------- Instructions -----------------------

# ------------ Resources / Documentation involved -------------
# documentation for Kaggle API *within* python?: https://stackoverflow.com/questions/55934733/documentation-for-kaggle-api-within-python
# Kaggle CLI Documentation: https://github.com/Kaggle/kaggle-cli/blob/main/docs/README.md#authentication
# Matplotlib List of named colors: https://matplotlib.org/stable/gallery/color/named_colors.html

# Original dataset (Bacteria Dataset): https://www.kaggle.com/datasets/kanchana1990/bacteria-dataset

# Inspiration from:
# Bacteria Analysis: https://www.kaggle.com/code/osamaalfa/bacteria-analysis

# ------------------------- Libraries -------------------------
from kaggle.api.kaggle_api_extended import KaggleApi
import os  # os.path.exists(path)
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------- Imports --------------------------


# ------------------------- Functions -------------------------


# ------------------------- Variables -------------------------
datasetFolder = 'BacteriaDataset'
datasetId = 'kanchana1990/bacteria-dataset'
global datasetPath

# --------------------------- Code ----------------------------
try:
    datasetPath = f'{datasetFolder}/{os.listdir(datasetFolder)[0]}'
except FileNotFoundError or IndexError:
    print(f'File not found. Downloading dataset at {datasetFolder}')
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(datasetId, path=datasetFolder, unzip=True)
    print("File successfully downloaded")

# Transform csv into a pandas dataframe
BacteriaData = pd.read_csv(datasetPath)

# Get data as a dictionary
bacteria_dic = BacteriaData.to_dict()
# print(bacteria_dic)

# Example of data (4 rows)
# print(BacteriaData.head())

# A summary of our data
# print(BacteriaData.describe())

# Get Data in Columns
# print(BacteriaData["Where Found"])
# print(BacteriaData.Family)

# Get Data in Row
# print(BacteriaData[BacteriaData.Family == "Bacillaceae"])


# Create a dataframe from scratch
data_dict = {
    "students": ["María", "Jaime", "Luis"],
    "grades": [89, 91, 72]
}
data = pd.DataFrame(data_dict)
# print(data)

# Transform data into a new csv file
data.to_csv("test_grades.csv")

# Graph
harmful_counts = BacteriaData["Harmful to Humans"].value_counts()
# print(harmful_counts)

# Creating the Pie Chart
# plt.figure(figsize=(6, 6))
# plt.pie(harmful_counts, labels=harmful_counts.index, autopct='%1.1f%%', colors=['mediumturquoise', 'lightcoral'])
# plt.title("Percentage of Harmful vs Non-Harmful Bacteria")
# plt.show()

# Calculating the 10 Most Common Bacterial Families
"""
top_families = BacteriaData["Family"].value_counts().nlargest(10)

plt.figure(figsize=(14, 5))
plt.barh(top_families.index, top_families.values, color='mediumslateblue')
plt.title('10 Most Common Bacterial Families')
plt.xlabel('Number of Bacteria')
plt.ylabel('Family')
plt.show()
"""

# Calculating the 5 most common places bacteria was found
"""
top_places = BacteriaData["Where Found"].value_counts().nlargest(5)

plt.figure(figsize=(15, 5))
plt.barh(top_places.index, top_places.values, color='sandybrown')
plt.title('5 Most Common Places Bacteria Was Found')
plt.xlabel('Number of Bacteria')
plt.ylabel('Place')
plt.show()
"""
