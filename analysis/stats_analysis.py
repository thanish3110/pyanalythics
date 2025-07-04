def funding_stats(df):
    return {
        'mean': df['AmountInUSD'].mean(),
        'median': df['AmountInUSD'].median(),
        'min': df['AmountInUSD'].min(),
        'max': df['AmountInUSD'].max()
    }

def startups_multiple_funding(df):
    return df['StartupName'].value_counts()[df['StartupName'].value_counts() > 1]
def get_top_investors(df, top_n=5):
    return df.groupby('Investors Name')['AmountInUSD'].sum().sort_values(ascending=False).head(top_n)
def get_monthly_trends(df):
    df = df.copy()
    if 'Date' not in df.columns or 'AmountInUSD' not in df.columns:
        return pd.DataFrame(columns=['Month', 'Amount'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly = df.groupby('Month')['AmountInUSD'].sum().reset_index()
    monthly['Month'] = monthly['Month'].astype(str)
    monthly = monthly.rename(columns={'AmountInUSD': 'Amount'})
    return monthly

def get_quarterly_trends(df):
    df = df.copy()
    if 'Date' not in df.columns or 'AmountInUSD' not in df.columns:
        return pd.DataFrame(columns=['Quarter', 'Amount'])
    df['Quarter'] = df['Date'].dt.to_period('Q')
    quarterly = df.groupby('Quarter')['AmountInUSD'].sum().reset_index()
    quarterly['Quarter'] = quarterly['Quarter'].astype(str)
    quarterly = quarterly.rename(columns={'AmountInUSD': 'Amount'})
    return quarterly
import numpy as np
import pandas as pd

def get_total_funding(df):
    return np.sum(df['AmountInUSD'])

def get_top_startups(df, top_n=5):
    return df.groupby('StartupName')['AmountInUSD'].sum().sort_values(ascending=False).head(top_n)

def get_funding_by_city(df):
    return df.groupby('CityLocation')['AmountInUSD'].sum().sort_values(ascending=False)

def get_yearly_trends(df):
    df['Year'] = df['Date'].dt.year
    return df.groupby('Year')['AmountInUSD'].sum()