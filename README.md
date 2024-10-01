# Exploratory Data Analysis of Electric Vehicle Population in Washington State

## Project Overview
This project is part of the **CS660/71425 Mathematical Foundations of Analytics** course at **Pace University** for Fall 2024. The main goal of the project is to perform **Exploratory Data Analysis (EDA)** on a dataset containing information about electric vehicles (EVs) in Washington State, USA.

## Course Information
- **Course:** CS660/71425 Mathematical Foundations of Analytics
- **Instructor:** Prof. Sarbanes
- **Group-1:** Will Torres, Mike Griffin, Watson Blair, Syed Abdul Mubashir
- **Semester:** Fall 2024
- **Project #:** 1
- **Due Date:** 07-Oct-2024

## Dataset Description
The dataset used in this project is **EV_Population_WA_Data.csv**, which contains information on 200,048 electric vehicles registered in Washington State. The dataset includes attributes like:
- Vehicle Identification Number (VIN)
- Manufacturer
- Model Year
- Electric Range
- Electric Vehicle Type
- Clean Alternative Fuel Vehicle (CAFV) Eligibility
- Base MSRP
- Legislative District
- Electric Utility
- Vehicle Location

## Questions Addressed
The EDA focuses on answering the following key questions:
1. Which car manufacturers are the most commonly used for EVs in Washington?
2. What are the highest and lowest electric ranges, and which car makers and models correspond to these values?
3. Is the maximum electric range value unique? If not, which cars share this range?
4. Is the minimum electric range value unique? If not, which cars share this range?
5. How does the electric range vary between car makers and models?
6. Which are the top 5 cities adopting EVs?
7. How does EV adoption vary among car makers over the years?
8. Is there a correlation between the electric range and the city of an EV?
9. Which county has the greatest variety of EV models?

## Project Structure
This repository contains the following files:
- **EV_EDA_WA.ipynb**: Jupyter Notebook with the full exploratory data analysis process.
- **EV_Population_WA_Data.csv**: The dataset used for analysis.

## Tools and Libraries Used
- **Python**: For data processing and visualization.
- **pandas**: For data manipulation and analysis.
- **matplotlib** and **seaborn**: For data visualization.
- **numpy**: For numerical operations.

## Steps in the EDA Process
1. **Data Loading and Inspection**: Load the dataset and inspect its structure, types, and summary statistics.
2. **Data Cleaning**: Handle missing values, correct data types, and remove duplicates.
3. **Univariate Analysis**: Analyze individual variables with visualizations such as histograms and box plots.
4. **Bivariate and Multivariate Analysis**: Investigate relationships between variables using scatter plots, heatmaps, and correlation matrices.
5. **Feature Engineering**: Create new features and prepare the data for potential future modeling.
6. **Insights and Conclusions**: Summarize key findings from the analysis.

## How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/torrwill/cs660_ev_eda.git
   ```
2. Install required dependencies:
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```
3. Open the Jupyter Notebook and run the analysis:
   ```bash
   jupyter notebook EV_EDA_WA.ipynb
   ```
   
## Acknowledgements
- Data source: [Washington State EV Population Data on data.gov](https://data.gov)
- This project was completed as part of the curriculum for CS660/71425 at Pace University.
