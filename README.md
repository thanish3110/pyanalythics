# Indian Startup Funding Analysis

This project analyzes Indian startup funding data, providing data cleaning, statistical analysis, visualizations, and an interactive dashboard.

## Features
- Data cleaning and preprocessing
- Statistical summaries (total funding, top startups, top investors, etc.)
- Visualizations: bar charts, line charts, pie charts, and a funding map
- Interactive dashboard with filters (Streamlit)
- Export filtered data as CSV

## Project Structure
```
main.py                      # Script for data analysis and static visualizations
analysis/
    data_cleaning.py         # Data cleaning functions
    stats_analysis.py        # Statistical analysis functions
    visualization.py         # Visualization functions
    __init__.py
    __pycache__/
data/
    startup_funding.csv      # Raw data file
dashboard.py                 # Streamlit dashboard
```

## How to Run

### 1. Install Requirements
```
pip install pandas numpy matplotlib plotly openpyxl streamlit
```

### 2. Run the Dashboard
```
streamlit run dashboard.py
```


### 3. Run the Analysis Script (for static charts and stats)
```
python main.py
```
This will print statistics in the terminal and show charts as pop-up windows (matplotlib/plotly). Make sure you are not running in a headless environment (like some remote servers) if you want to see the charts.

## Data
- Place your `startup_funding.csv` file in the `data/` folder.

## Output
- The dashboard provides interactive charts, tables, and a map.
- The script prints statistics and shows static charts.

## License
MIT
