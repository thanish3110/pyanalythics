import streamlit as st
import pandas as pd
from analysis.data_cleaning import load_and_clean_data
from analysis.stats_analysis import (
    get_total_funding, get_top_startups,
    get_funding_by_city, get_yearly_trends,
    get_monthly_trends, get_quarterly_trends, get_top_investors
)
from analysis.visualization import plot_funding_pie_by_city

st.title("Startup Funding Analysis Dashboard")

# Load data
@st.cache_data
def get_data():
    return load_and_clean_data("data/startup_funding.csv")

df = get_data()

# Sidebar filters

city = st.sidebar.selectbox("Select City", ["All"] + sorted(df['CityLocation'].dropna().astype(str).unique().tolist()))
year = st.sidebar.selectbox("Select Year", ["All"] + sorted(df['Date'].dt.year.dropna().unique().astype(int).tolist()))
if 'Industry Vertical' in df.columns:
    industries = df['Industry Vertical'].dropna().astype(str).unique().tolist()
    industry = st.sidebar.selectbox("Select Industry", ["All"] + sorted(industries))
else:
    industry = st.sidebar.selectbox("Select Industry", ["All"])
if 'Investors Name' in df.columns:
    investors = df['Investors Name'].dropna().astype(str).unique().tolist()
    investor = st.sidebar.selectbox("Select Investor", ["All"] + sorted(investors))
else:
    investor = st.sidebar.selectbox("Select Investor", ["All"])

filtered = df.copy()
if city != "All":
    filtered = filtered[filtered['CityLocation'] == city]
if year != "All":
    filtered = filtered[filtered['Date'].dt.year == int(year)]
if industry != "All" and 'Industry Vertical' in filtered.columns:
    filtered = filtered[filtered['Industry Vertical'] == industry]
if investor != "All":
    filtered = filtered[filtered['Investors Name'] == investor]

# Show filtered data preview and warning if empty
st.write('#### Filtered Data Preview')
if filtered.empty:
    st.warning('No data available for the selected filters. Please adjust your filters.')
else:
    st.dataframe(filtered.head())

st.write(f"### Total Funding: $ {get_total_funding(filtered):,.2f}")

st.write("#### Top Funded Startups")
st.dataframe(get_top_startups(filtered))

st.write("#### Funding by City")
st.dataframe(get_funding_by_city(filtered))

st.write("#### Yearly Trends")
st.dataframe(get_yearly_trends(filtered))

st.write("#### Top Investors")
st.dataframe(get_top_investors(filtered))

st.write("#### Funding Pie Chart (Top 5 Cities)")
from analysis import visualization
visualization.plot_funding_pie_by_city(get_funding_by_city(filtered), st_module=st)


# --- Additional Visualizations and Features ---



# Monthly Trends Line Chart
st.write("#### Monthly Funding Trends")
monthly_trends = get_monthly_trends(filtered)
st.write('Monthly Trends Data Preview:')
st.dataframe(monthly_trends)
if isinstance(monthly_trends, pd.DataFrame):
    st.write('Monthly Trends Columns:', list(monthly_trends.columns))
    st.write('Monthly Trends dtypes:', monthly_trends.dtypes.astype(str).to_dict())
if isinstance(monthly_trends, pd.DataFrame) and not monthly_trends.empty and 'Month' in monthly_trends.columns and 'Amount' in monthly_trends.columns:
    monthly_trends = monthly_trends.dropna(subset=['Month', 'Amount'])
    if not monthly_trends.empty:
        monthly_trends = monthly_trends.copy()
        monthly_trends['Month'] = monthly_trends['Month'].astype(str)
        st.line_chart(monthly_trends.set_index('Month')['Amount'])
    else:
        st.info("No data available for the selected filters.")
else:
    st.info("No data available for the selected filters.")



# Quarterly Trends Line Chart
st.write("#### Quarterly Funding Trends")
quarterly_trends = get_quarterly_trends(filtered)
st.write('Quarterly Trends Data Preview:')
st.dataframe(quarterly_trends)
if isinstance(quarterly_trends, pd.DataFrame):
    st.write('Quarterly Trends Columns:', list(quarterly_trends.columns))
    st.write('Quarterly Trends dtypes:', quarterly_trends.dtypes.astype(str).to_dict())
if isinstance(quarterly_trends, pd.DataFrame) and not quarterly_trends.empty and 'Quarter' in quarterly_trends.columns and 'Amount' in quarterly_trends.columns:
    quarterly_trends = quarterly_trends.dropna(subset=['Quarter', 'Amount'])
    if not quarterly_trends.empty:
        quarterly_trends = quarterly_trends.copy()
        quarterly_trends['Quarter'] = quarterly_trends['Quarter'].astype(str)
        st.line_chart(quarterly_trends.set_index('Quarter')['Amount'])
    else:
        st.info("No data available for the selected filters.")
else:
    st.info("No data available for the selected filters.")

# Map Visualization (if available)
try:
    from analysis.visualization import plot_funding_map
    st.write("#### Funding Distribution Map")
    plot_funding_map(filtered)
except ImportError:
    st.info("Map visualization is not available.")

# Download cleaned/filtered data
st.write("#### Download Filtered Data")
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(filtered)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='filtered_startup_funding.csv',
    mime='text/csv',
)
