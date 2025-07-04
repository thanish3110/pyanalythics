import streamlit as st
import plotly.express as px

def plot_funding_map(filtered_df):
    # Try to find the correct amount column
    amount_col = None
    for col in filtered_df.columns:
        if col.lower() == 'amount' or 'amount' in col.lower():
            amount_col = col
            break
    if 'CityLocation' not in filtered_df.columns or amount_col is None:
        st.info('Map cannot be displayed: CityLocation or Amount column missing.')
        return
    city_funding = filtered_df.groupby('CityLocation')[amount_col].sum().reset_index()
    city_funding = city_funding[city_funding['CityLocation'].notna() & (city_funding['CityLocation'] != '')]
    if city_funding.empty:
        st.info('No city funding data available for map.')
        return
    # Add ', India' for geocoding
    city_funding['City'] = city_funding['CityLocation'].astype(str) + ', India'
    fig = px.scatter_geo(
        city_funding,
        locations="City",
        locationmode="country names",
        size=amount_col,
        hover_name="CityLocation",
        size_max=30,
        title="Funding by City (India)",
        scope="asia"
    )
    st.plotly_chart(fig)
def plot_monthly_trends(monthly_data):
    monthly_data.plot(kind='line', marker='o', figsize=(12, 5), color='purple')
    plt.title("Monthly Funding Trend")
    plt.xlabel("Month")
    plt.ylabel("Funding (USD)")
    plt.grid(True)
    plt.tight_layout()
    # plt.show()  # Disabled for Streamlit compatibility

def plot_quarterly_trends(quarterly_data):
    quarterly_data.plot(kind='line', marker='o', figsize=(12, 5), color='brown')
    plt.title("Quarterly Funding Trend")
    plt.xlabel("Quarter")
    plt.ylabel("Funding (USD)")
    plt.grid(True)
    plt.tight_layout()
    # plt.show()  # Disabled for Streamlit compatibility
import plotly.express as px

def plot_funding_map_by_city(city_data):
    df_map = city_data.reset_index()
    df_map.columns = ['City', 'Funding']
    # Add ', India' to each city for better geocoding
    df_map['City'] = df_map['City'] + ', India'
    fig = px.scatter_geo(
        df_map,
        locations="City",
        locationmode="country names",
        size="Funding",
        title="Funding by City (India)",
        scope="asia",
        hover_name="City",
        size_max=30
    )
    # fig.show()  # Disabled for Streamlit compatibility
    return fig
def plot_funding_pie_by_city(city_data, top_n=5, st_module=None):
    import matplotlib.pyplot as plt
    import io
    top_cities = city_data.head(top_n)
    others = city_data.iloc[top_n:].sum()
    labels = list(top_cities.index) + ['Others']
    sizes = list(top_cities.values) + [others]
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(f"Funding Distribution by Top {top_n} Cities")
    ax.axis('equal')
    if st_module is not None:
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        st_module.image(buf)
        plt.close(fig)
    # plt.show()  # Disabled for Streamlit compatibility
import matplotlib.pyplot as plt

def plot_top_startups(startup_data):
    startup_data.plot(kind='bar', figsize=(10, 5), color='green')
    plt.title("Top Funded Startups")
    plt.xlabel("Startup")
    plt.ylabel("Total Funding (USD)")
    plt.tight_layout()
    # plt.show()  # Disabled for Streamlit compatibility

def plot_funding_by_city(city_data):
    city_data.plot(kind='bar', figsize=(10, 5), color='orange')
    plt.title("Funding by City")
    plt.xlabel("City")
    plt.ylabel("Funding (USD)")
    plt.tight_layout()
    # plt.show()  # Disabled for Streamlit compatibility

def plot_yearly_trends(trend_data):
    trend_data.plot(kind='line', marker='o', figsize=(10, 5), color='blue')
    plt.title("Yearly Funding Trend")
    plt.xlabel("Year")
    plt.ylabel("Funding (USD)")
    plt.grid(True)
    plt.tight_layout()
    # plt.show()  # Disabled for Streamlit compatibility