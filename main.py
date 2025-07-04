from analysis.data_cleaning import load_and_clean_data
from analysis.stats_analysis import (
    get_total_funding, get_top_startups,
    get_funding_by_city, get_yearly_trends,
    get_monthly_trends, get_quarterly_trends
)
from analysis.visualization import (
    plot_top_startups, plot_funding_by_city,
    plot_yearly_trends, plot_funding_pie_by_city,
    plot_monthly_trends, plot_quarterly_trends
)

# Load & clean data
df = load_and_clean_data("data/startup_funding.csv")

# Stats
print("Total Funding in Dataset: $", get_total_funding(df))

top_startups = get_top_startups(df)
print("\nTop Funded Startups:\n", top_startups)

funding_by_city = get_funding_by_city(df)
print("\nFunding by City:\n", funding_by_city)

yearly_trends = get_yearly_trends(df)
print("\nYearly Trends:\n", yearly_trends)

# Top Investors
from analysis.stats_analysis import get_top_investors
top_investors = get_top_investors(df)
print("\nTop Investors:\n", top_investors)


# Funding Stats
from analysis.stats_analysis import funding_stats, startups_multiple_funding
stats = funding_stats(df)
print("\nFunding Stats (USD):")
print("Mean:", stats['mean'])
print("Median:", stats['median'])
print("Min:", stats['min'])
print("Max:", stats['max'])

multi_funded = startups_multiple_funding(df)
print("\nStartups with Multiple Fundings:\n", multi_funded)

# Visualizations
plot_top_startups(top_startups)
plot_funding_by_city(funding_by_city)
plot_yearly_trends(yearly_trends)
plot_funding_pie_by_city(funding_by_city)


# Monthly and Quarterly Trends
monthly_trends = get_monthly_trends(df)
plot_monthly_trends(monthly_trends)

quarterly_trends = get_quarterly_trends(df)
plot_quarterly_trends(quarterly_trends)

# Geographical Visualization
from analysis.visualization import plot_funding_map_by_city
plot_funding_map_by_city(funding_by_city)