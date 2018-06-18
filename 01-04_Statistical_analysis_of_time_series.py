"""Utility functions"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
        
    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_symbol = pd.read_csv(symbol_to_path(symbol), index_col="Date",parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_symbol = df_symbol.rename(columns={'Adj Close': symbol})
        df = df.join((df_symbol), how='inner')
        
    return df

def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def plot_selected(df, simbols, sdate, edate):
    df = df.loc[str(sdate): str(edate), simbols]
    plot_data(df)


def normolize_data(df):
    df = df/df.ix[0,:]
    return df 
    

def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-02', '2018-01-26')

    # Choose stock symbols to read
    symbols = ['SPY']
    
    # Get stock data
    df = get_data(symbols, dates)
    # Plot SPY data? retain matplotlib axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')
    
    # Compute rolling mean using a 20-day window
    rm_SPY = pd.rolling_mean(df['SPY'], window=20)
    
    #Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)
    
    #df = df/df.ix[0,:]
    #print (df.loc['2018-01-22':'2018-01-26',['GOOG','SPY']])
    plot_data()

if __name__ == "__main__":
    test_run()
