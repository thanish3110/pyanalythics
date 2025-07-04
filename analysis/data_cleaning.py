import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    # Rename columns to match code expectations
    df.rename(columns={
        'City  Location': 'CityLocation',
        'Startup Name': 'StartupName',
        'Amount in USD': 'AmountInUSD',
        'Date dd/mm/yyyy': 'Date'
    }, inplace=True)
    # Debug: print columns if needed
    # print(df.columns)

    # Drop rows where all fields are NaN
    df.dropna(how='all', inplace=True)

    # Fill missing CityLocation with 'Unknown'
    df['CityLocation'] = df['CityLocation'].fillna('Unknown')
    df['CityLocation'] = df['CityLocation'].apply(lambda x: str(x).strip().title())

    # Standardize common city typos
    df['CityLocation'] = df['CityLocation'].replace({
        'Delhi': 'New Delhi',
        'Delhi.': 'New Delhi',
        'Banglore': 'Bangalore',
        'Gurugram': 'Gurgaon',
        'Bengaluru': 'Bangalore'  
    })

    # Clean amount column
    df['AmountInUSD'] = df['AmountInUSD'].replace(r'[\$,]', '', regex=True)
    df['AmountInUSD'] = pd.to_numeric(df['AmountInUSD'], errors='coerce').fillna(0)

    # Convert Date to datetime and fill missing with previous value
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Date'] = df['Date'].ffill()

    # Remove empty columns
    df.dropna(axis=1, how='all', inplace=True)

    # Save cleaned data to Excel (convert Date to date only for Excel)
    df_to_save = df.copy()
    df_to_save['Date'] = df_to_save['Date'].dt.date
    df_to_save.to_excel("data/cleaned_startup_funding.xlsx", index=False)
    return df