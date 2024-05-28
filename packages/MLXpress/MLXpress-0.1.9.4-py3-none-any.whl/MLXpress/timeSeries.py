import pandas as pd
import numpy as np

def create_time_series(data, index=None):
    """
    Create a time series object from various data sources.

    Parameters:
    - data: The time series data. This can be a list, numpy array, pandas Series, or DataFrame.
    - index: Optional. The index associated with the time series data. If not provided,
             a default integer index will be used.

    Returns:
    - A pandas Series or DataFrame representing the time series data.
    """
    # If data is a list or numpy array, create a pandas Series with default index
    if isinstance(data, (list, np.ndarray)):
        if index is None:
            return pd.Series(data)
        else:
            return pd.Series(data, index=index)
    
    # If data is a pandas Series or DataFrame, return it as is
    elif isinstance(data, (pd.Series, pd.DataFrame)):
        return data
    
    # If none of the above, raise an error
    else:
        raise ValueError("Unsupported data type. Supported types are list, numpy array, pandas Series, or DataFrame.")


def time_indexing(time_series, start_time=None, end_time=None):
    """
    Perform time indexing on a time series data.

    Parameters:
    - time_series: The input time series data. This can be a pandas Series or DataFrame with a DateTimeIndex.
    - start_time: Optional. The start time for slicing the time series. If not provided, all data from the beginning is included.
    - end_time: Optional. The end time for slicing the time series. If not provided, all data up to the end is included.

    Returns:
    - A pandas Series or DataFrame representing the sliced time series data.
    """
    # Check if the input is a pandas Series or DataFrame with DateTimeIndex
    if not isinstance(time_series, (pd.Series, pd.DataFrame)):
        raise ValueError("Input must be a pandas Series or DataFrame.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")

    # Slice the time series based on start and end times
    if start_time is not None and end_time is not None:
        return time_series.loc[start_time:end_time]
    elif start_time is not None:
        return time_series.loc[start_time:]
    elif end_time is not None:
        return time_series.loc[:end_time]
    else:
        return time_series


def resample_and_aggregate(time_series, frequency, method='mean'):
    """
    Resample time series data to a different frequency and aggregate data within each interval.

    Parameters:
    - time_series: The input time series data. This can be a pandas Series or DataFrame with a DateTimeIndex.
    - frequency: The frequency to which the data will be resampled. For example: 'M' for monthly, 'Q' for quarterly, etc.
    - method: Optional. The aggregation method to use. Default is 'mean'. Other options include 'sum', 'median', 'max', 'min', etc.

    Returns:
    - A pandas Series or DataFrame representing the resampled and aggregated time series data.
    """
    # Check if the input is a pandas Series or DataFrame with DateTimeIndex
    if not isinstance(time_series, (pd.Series, pd.DataFrame)):
        raise ValueError("Input must be a pandas Series or DataFrame.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")

    # Resample and aggregate the time series data
    resampled_data = time_series.resample(frequency).agg(method)
    
    return resampled_data


def time_shift(time_series, periods, freq=None):
    """
    Shift time series data forward or backward in time.

    Parameters:
    - time_series: The input time series data. This can be a pandas Series or DataFrame with a DateTimeIndex.
    - periods: The number of periods to shift the data. Use a positive number to shift forward, negative number to shift backward.
    - freq: Optional. The frequency of the data. If provided, the index will be shifted by multiples of the frequency.

    Returns:
    - A pandas Series or DataFrame representing the shifted time series data.
    """
    # Check if the input is a pandas Series or DataFrame with DateTimeIndex
    if not isinstance(time_series, (pd.Series, pd.DataFrame)):
        raise ValueError("Input must be a pandas Series or DataFrame.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")

    # Shift the time series data
    shifted_data = time_series.shift(periods, freq=freq)
    
    return shifted_data


def calculate_rolling_statistics(time_series, window, statistic='mean'):
    """
    Calculate rolling statistics such as moving averages and rolling standard deviations.

    Parameters:
    - time_series: The input time series data. This can be a pandas Series or DataFrame with a DateTimeIndex.
    - window: The size of the moving window, i.e., the number of periods to include in the calculation.
    - statistic: Optional. The type of rolling statistic to calculate. Default is 'mean'. Other options include 'std' for standard deviation, 'median', etc.

    Returns:
    - A pandas Series or DataFrame representing the calculated rolling statistic.
    """
    # Check if the input is a pandas Series or DataFrame with DateTimeIndex
    if not isinstance(time_series, (pd.Series, pd.DataFrame)):
        raise ValueError("Input must be a pandas Series or DataFrame.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")

    # Calculate rolling statistics
    if statistic == 'mean':
        rolling_statistic = time_series.rolling(window=window).mean()
    elif statistic == 'std':
        rolling_statistic = time_series.rolling(window=window).std()
    elif statistic == 'median':
        rolling_statistic = time_series.rolling(window=window).median()
    # Add more options for other rolling statistics as needed
    
    return rolling_statistic


def time_series_analysis(time_series):
    """
    Perform basic statistical analysis on time series data.

    Parameters:
    - time_series: The input time series data. This should be a pandas Series or DataFrame with a DateTimeIndex.

    Returns:
    - A dictionary containing various statistical measures.
    """
    # Check if the input is a pandas Series or DataFrame with DateTimeIndex
    if not isinstance(time_series, (pd.Series, pd.DataFrame)):
        raise ValueError("Input must be a pandas Series or DataFrame.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")
    
    # Calculate statistical measures
    analysis_results = {}

    # Measures of central tendency
    analysis_results['mean'] = time_series.mean()
    analysis_results['median'] = time_series.median()
    analysis_results['mode'] = time_series.mode().iloc[0]

    # Measures of variability
    analysis_results['std_deviation'] = time_series.std()
    analysis_results['variance'] = time_series.var()

    # Measures of correlation (if DataFrame)
    if isinstance(time_series, pd.DataFrame):
        correlation_matrix = time_series.corr()
        analysis_results['correlation_matrix'] = correlation_matrix
    
    return analysis_results


def handle_missing_data(time_series, method='interpolate'):
    """
    Handle missing data in time series using specified method.

    Parameters:
    - time_series: The input time series data. This should be a pandas Series or DataFrame with a DateTimeIndex.
    - method: Optional. The method to handle missing data. Default is 'interpolate'. Other options include 'ffill' (forward fill) and 'bfill' (backward fill).

    Returns:
    - A pandas Series or DataFrame with missing data handled according to the specified method.
    """
    # Check if the input is a pandas Series or DataFrame with DateTimeIndex
    if not isinstance(time_series, (pd.Series, pd.DataFrame)):
        raise ValueError("Input must be a pandas Series or DataFrame.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")
    
    # Handle missing data according to the specified method
    if method == 'interpolate':
        filled_time_series = time_series.interpolate(method='time')
    elif method == 'ffill':
        filled_time_series = time_series.ffill()
    elif method == 'bfill':
        filled_time_series = time_series.bfill()
    else:
        raise ValueError("Unsupported method. Supported methods are 'interpolate', 'ffill', and 'bfill'.")
    
    return filled_time_series


def detect_outliers(time_series, method='zscore', threshold=3, remove_outliers=False):
    """
    Detect outliers in time series data using specified method.

    Parameters:
    - time_series: The input time series data. This should be a pandas Series with a DateTimeIndex.
    - method: Optional. The method to detect outliers. Default is 'zscore'. Other options include 'modified_zscore'.
    - threshold: Optional. The threshold value for outlier detection. Default is 3.
    - remove_outliers: Optional. Whether to remove outliers from the time series. Default is False.

    Returns:
    - If remove_outliers=False, returns a pandas Series containing Boolean values indicating outlier status.
    - If remove_outliers=True, returns a pandas Series with outliers removed.
    """
    # Check if the input is a pandas Series with DateTimeIndex
    if not isinstance(time_series, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")
    
    # Calculate z-scores for outlier detection
    if method == 'zscore':
        z_scores = (time_series - time_series.mean()) / time_series.std()
    elif method == 'modified_zscore':
        median = time_series.median()
        median_absolute_deviation = (time_series - median).abs().median()
        z_scores = 0.6745 * (time_series - median) / median_absolute_deviation
    
    # Detect outliers based on threshold
    outliers = z_scores.abs() > threshold
    
    # Optionally remove outliers
    if remove_outliers:
        time_series = time_series[~outliers]
    
    return time_series if remove_outliers else outliers


def time_series_forecast(time_series, steps=1):
    """
    Perform time series forecasting using a naive method (last observation).

    Parameters:
    - time_series: The input time series data. This should be a pandas Series with a DateTimeIndex.
    - steps: Optional. The number of steps ahead to forecast. Default is 1.

    Returns:
    - A pandas Series containing the forecasted values.
    """
    # Check if the input is a pandas Series with DateTimeIndex
    if not isinstance(time_series, pd.Series):
        raise ValueError("Input must be a pandas Series.")
    if not isinstance(time_series.index, pd.DatetimeIndex):
        raise ValueError("Input must have a DateTimeIndex.")
    
    # Get the last observed value
    last_observed_value = time_series.iloc[-1]
    
    # Create forecasted time index
    forecast_index = pd.date_range(start=time_series.index[-1] + time_series.index.freq, periods=steps, freq=time_series.index.freq)
    
    # Create pandas Series with forecasted values and index
    forecast_series = pd.Series([last_observed_value] * steps, index=forecast_index)
    
    return forecast_series


