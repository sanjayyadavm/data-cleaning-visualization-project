# Data Cleaning & Visualization Project

## Objective
Clean a raw sales dataset, handle missing values, duplicates and outliers, create useful features, and visualize important insights.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib

## Project Steps
1. Load the raw dataset.
2. Inspect missing values and duplicate records.
3. Remove duplicate order IDs.
4. Fill missing categorical values using the mode.
5. Fill missing numeric values using the median.
6. Detect and cap an outlier using the IQR method.
7. Create a Sales column and Month column.
8. Save the cleaned dataset.
9. Create visualizations for category sales, regional sales, and monthly sales.

## Key Insights
The analysis produces:
- Total sales by product category
- Total sales by region
- Monthly sales trend
- A cleaned dataset ready for further analysis

## How to Run
```bash
pip install pandas numpy matplotlib
python analysis.py
```
