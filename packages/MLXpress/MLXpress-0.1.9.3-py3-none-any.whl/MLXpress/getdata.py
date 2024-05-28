

import pandas as pd

import ccxt
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
import pandas as pd
from forex_python.converter import CurrencyRates


def convert_to_inr(currency, amount):
    """
    Convert currency to INR.

    Args:
        currency (str): Currency code (e.g., 'USD').
        amount (float): Amount to convert.

    Returns:
        float: Converted amount in INR.
    """
    c = CurrencyRates()
    inr_amount = c.convert(currency, 'INR', amount)
    return inr_amount


def get_stock_data(symbol, start_date, end_date, save=False, filename=None):
    """
    Get historical stock data.

    Args:
        symbol (str): Ticker symbol of the stock.
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.
        save (bool): Whether to save the data to a CSV file (default is False).
        filename (str): Filename to save the CSV file (required if save=True).

    Returns:
        DataFrame: Historical stock data in INR.
    """
    data = yf.download(symbol, start=start_date, end=end_date)

    # Convert Close prices to INR
    data['Close_INR'] = data['Close'].apply(lambda x: convert_to_inr('USD', x))

    # Save data to CSV file if save=True
    if save:
        if filename is None:
            raise ValueError("Filename must be provided when save is True")
        data.to_csv(filename)

    return data


def visualize_stock_data(symbol, start_date, end_date):
    """
    Visualize historical stock data.

    Args:
        symbol (str): Ticker symbol of the stock.
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.
    """
    # Get stock data
    stock_data = get_stock_data(symbol, start_date, end_date)

    # Plot the stock prices in INR
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['Close_INR'], label=f'{symbol} Close Price (INR)')
    plt.title(f'{symbol} Close Price in INR')
    plt.xlabel('Date')
    plt.ylabel('Close Price (INR)')
    plt.legend()
    plt.grid(True)
    plt.show()

def compare_stock_prices(symbols, start_date, end_date):
    """
    Compare historical stock prices over a specified interval.

    Args:
        symbols (list of str): List of stock ticker symbols.
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.
    """
    # Fetch historical price data for each stock symbol
    stock_dfs = {}
    for symbol in symbols:
        stock_dfs[symbol] = get_stock_data(symbol, start_date, end_date)

    # Plot the close prices for each stock symbol
    plt.figure(figsize=(12, 8))
    for symbol, df in stock_dfs.items():
        plt.plot(df.index, df['Close_INR'], label=symbol)

    # Set plot labels and legend
    plt.title('Comparison of Stock Prices (INR)')
    plt.xlabel('Date')
    plt.ylabel('Close Price (INR)')
    plt.legend()
    plt.grid(True)
    plt.show()


import pandas as pd

import ccxt
import matplotlib.pyplot as plt
from datetime import datetime


def get_crypto_data(symbol, timeframe, limit=100, save=False, filename=None):
    """
    Get historical cryptocurrency data.

    Args:
        symbol (str): Symbol of the cryptocurrency (e.g., 'BTC/INR' for Bitcoin to INR).
        timeframe (str): Timeframe of the data (e.g., '1d' for daily).
        limit (int): Number of data points to fetch.
        save (bool): Whether to save the data to a CSV file (default is False).
        filename (str): Filename to save the CSV file (required if save=True).

    Returns:
        DataFrame: Historical cryptocurrency data with columns ['Timestamp', 'Close Price'].
    """
    exchange = ccxt.wazirx()  # Initialize WazirX exchange
    data = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    # Convert timestamp to datetime and extract close prices
    timestamps = [pd.to_datetime(data_point[0], unit='ms') for data_point in data]
    close_prices = [data_point[4] for data_point in data]

    # Create DataFrame
    df = pd.DataFrame({'Timestamp': timestamps, 'Close Price': close_prices})

    # Save data to CSV file if save=True
    if save:
        if filename is None:
            raise ValueError("Filename must be provided when save is True")
        df.to_csv(filename, index=False)

    return df


def visualize_crypto_data(symbol, timeframe, limit=100):
    """
    Visualize historical cryptocurrency data.

    Args:
        symbol (str): Symbol of the cryptocurrency (e.g., 'BTC/INR' for Bitcoin to INR).
        timeframe (str): Timeframe of the data (e.g., '1d' for daily).
        limit (int): Number of data points to fetch.
    """
    # Get cryptocurrency data
    crypto_data = get_crypto_data(symbol, timeframe, limit)

    # Extract date and close price
    dates = [datetime.utcfromtimestamp(data[0] / 1000) for data in crypto_data]
    close_prices = [data[4] for data in crypto_data]

    # Plot the cryptocurrency prices
    plt.figure(figsize=(10, 6))
    plt.plot(dates, close_prices, label=f'{symbol} Close Price')
    plt.title(f'{symbol} Close Price')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.show()


def compare_crypto_prices(symbols, timeframe, limit=100):
    """
    Compare historical cryptocurrency prices over a specified interval.

    Args:
        symbols (list of str): List of cryptocurrency symbols (e.g., ['BTC/INR', 'ETH/INR']).
        timeframe (str): Timeframe of the data (e.g., '1d' for daily).
        limit (int): Number of data points to fetch.
    """
    # Fetch historical price data for each cryptocurrency symbol
    crypto_dfs = {}
    for symbol in symbols:
        crypto_dfs[symbol] = get_crypto_data(symbol, timeframe, limit)

    # Plot the close prices for each cryptocurrency
    plt.figure(figsize=(12, 8))
    for symbol, df in crypto_dfs.items():
        plt.plot(df['Timestamp'], df['Close Price'], label=symbol)

    # Set plot labels and legend
    plt.title('Comparison of Cryptocurrency Prices')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.show()


