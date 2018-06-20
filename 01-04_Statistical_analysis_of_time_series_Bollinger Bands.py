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

def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.rolling_mean(values, window=window)


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    # TODO: Compute and return rolling standard deviation
    rolling_std = pd.rolling_std(values, window)
    return rolling_std


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    # TODO: Compute upper_band and lower_band
    upper_band=rm+2*rstd
    lower_band=rm-2*rstd
    return upper_band, lower_band

def plot_selected(df, simbols, sdate, edate):
    df = df.loc[str(sdate): str(edate), simbols]
    plot_data(df)
   
def compute_daily_returns(df):  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """Compute and return daily returns values"""
    daily_return = (df / df.shift(1)) - 1
    daily_return.iloc[0, :] = 0
    return daily_return

def test_run():
    # Define a date range
    dates = pd.date_range('2017-01-02', '2018-01-26')

    # Choose stock symbols to read
    symbols = ['SPY']
    
    # Get stock data
    df = get_data(symbols, dates)
    
    
    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
   # upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
    
    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)
    
    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
    
    '''Compyte daily returns'''
    daily_retutns = compute_daily_returns(df)
    plot_data(daily_retutns, title='Daily returns')
    
if __name__ == "__main__":
    test_run()
