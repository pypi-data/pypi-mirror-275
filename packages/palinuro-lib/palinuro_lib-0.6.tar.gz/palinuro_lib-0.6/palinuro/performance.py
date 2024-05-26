import string
import random
import numpy as np
import pandas as pd
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns



def nav_pro(trades_df, prices, registry, initial_balance = 50000000):
    """
    Compute the Cumulative PnLs and the total NAV of a portfolio defined from a list of trades.
    NB: It does not check if a position can be opened given the correct real amount of cash in the balance, it just open EVERY SINGLE TRADE found in trades_df

    
    Parameters
    ----------
    trades_df : pandas.DataFrame
        DataFrame containing the trades. It must have the following columns:
            - security_id: (str) a unique identifier of the security
            - entry_ts: (datetime) the timestamp at which the trade is open
            - exit_ts: (datetime) the timestamp at which the trade is closed
            - direction: (int) is equal to 1 for a long position, -1 for a short position
            - quantity: (float) the amount traded (n. of stocks for equity instruments or n. of contracts for futures)
        
    prices : pandas.DataFrame
        DataFrame containing the prices of the securities. It is mandatory to have 365 days per year and 0 missing values (do ffill for NaNs).
        It must have the following columns:
            - security_id: (str) a unique identifier of the security
            - date: (datetime) a timestamp that identifies the date.
            - price_usd: (float) the price in USD

    registry : pandas.DataFrame
        DataFrame containing the master data for the traded securities. It must have the following columns:
            - security_id: (str) a unique identifier of the security
            - multiplier: (float) multiplier (field <Value of 1.0 pt> in Bloomberg DES) for futures contract. Must be equal to 1 for equity instruments
            - currency: (str) currency of the instrument
            - type: (str) type of the instrument, can be equity or future

    initial_balance : float
        The initial balance available when started trading, to which the PnLs of the various trades are summed

    
    Returns
    -------
    trades_ext : pandas.DataFrame
        Extended version of the trades_df dataframe including other columns:
            - trade_id : (str) unique identifier for each trade
            - multiplier: (float) security's multiplier from registry
            - currency: (str) security's currency from registry
            - type: (str) security's type from registry
            - entry_px: (float) the price at which the trade is open

    pnl_df : pandas.DataFrame
        DataFrame that contains for each row the Cumulative PnL for the corresponding trade (since the position is entered, up to time t).
        Cumulative PnL = (Px - EntryPx) * Multiplier * Qt * direction

    nav : pandas.Series
        Series of the NAV of the portfolio
    """
    

    pivoted_prices = prices.pivot(index = 'date', columns = 'security_id', values = 'price_usd')
    trades_df_ext = trades_df.copy()
    
    # add to trades_df_ext a unique trade_id for each trade
    random.seed(5) # set seed for reproducibility
    trades_df_ext.insert(0, 'trade_id',
            [f'{random.choice(string.ascii_uppercase)}{random.randint(0,9)}{random.choice(string.ascii_uppercase)}{random.randint(0,9)}' for _ in range(len(trades_df))])
    
    if trades_df_ext['trade_id'].nunique() != len(trades_df_ext):
        raise Exception("A duplicated trade_id occurred, increase the characters in the trade_id code")
    
    # extend the initial trades_df with the info from the registry
    trades_df_ext = trades_df_ext.merge(registry[['security_id', 'multiplier', 'currency', 'type']], on=['security_id'], how='left')

    # add to trades_df_ext the price at which the trade is open
    trades_df_ext = trades_df_ext.merge(prices[['security_id', 'date', 'price_usd']],
                                    left_on = ['security_id', 'entry_ts'],
                                    right_on = ['security_id', 'date'],
                                    how = 'left'
                                        ).drop('date', axis=1).rename({'price_usd':'entry_px'}, axis=1)
    
    trades_df_ext = trades_df_ext.sort_values(by=['entry_ts', 'exit_ts', 'type']).reset_index(drop=True)

    # check if securities that are not futures have a short position
    if len(trades_df_ext[trades_df_ext['direction'] == -1]) > 0 and not 'future' in trades_df_ext.loc[trades_df_ext['direction'] == -1, 'type'].unique():
        raise Exception("Only futures can be shorted")

    # create a df where to store the PnLs from the trades
    pnl_df = pd.DataFrame(index=pivoted_prices.loc[trades_df_ext['entry_ts'].min():trades_df_ext['exit_ts'].max()].index)

    for idx in trades_df_ext.index:

        # store trade_id, security_id, entry_px and multiplier of the current trade
        tradeid_j = trades_df_ext.loc[idx, 'trade_id']
        sec_j = trades_df_ext.loc[idx, 'security_id']
        direc_j = trades_df_ext.loc[idx, 'direction']
        entrypx_j = trades_df_ext.loc[idx, 'entry_px']
        multi_j = trades_df_ext.loc[idx, 'multiplier']
        qt_j = trades_df_ext.loc[idx, 'quantity']

        # raise error if the trade's entry date is not in the price table
        if np.isnan(entrypx_j) == True:
            raise Exception(f"The start date for trade: [{direc_j}, {sec_j}] is not covered in the Prices Table. Check the security_id and the price series availability.")
        
        # create a series on which the PnL computations are done, slicing on the entry/exit timestamps
        temp_pxseries = pivoted_prices.loc[trades_df_ext.loc[idx, 'entry_ts'] : trades_df_ext.loc[idx, 'exit_ts'], sec_j].copy()

        # compute the Cumulative PnL (since the position is entered, up to time t) as: Cumulative PnL = (Px - EntryPx) * Multiplier * Qt * direction
        temp_series = (temp_pxseries - entrypx_j) * multi_j * qt_j * direc_j
        temp_series = temp_series.rename(tradeid_j)

        # store the Cumulative PnL
        pnl_df = pnl_df.join(temp_series)
    
    # the ffill crystallize the last PnL position, the fillna 0 makes irrelevant for the NAV each position before it is opened
    pnl_df = pnl_df.ffill().fillna(0)

    # delete Sat&Sun
    pnl_df = pnl_df[pnl_df.index.day_of_week < 5]

    # NAV = Initial Balance + sum(PnLs)
    nav = pnl_df.sum(axis=1) + initial_balance
    nav.name = 'nav'
    
    return trades_df_ext, pnl_df, nav



def cumulative_return(return_series, annualization=None):
    """
    Calculate the cumulative return of a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    annualization : int or None
        If False, no annualization is applied. If a float, it is used as the annualization factor.
        For example, 252 for trading days in a year.

    Returns
    -------
    cum_ret : float
        The period cumulative return.
    """

    if len(return_series) == 0:
        raise ValueError("The return series is empty")
    
    cum_ret = np.prod(1 + return_series) - 1

    if (annualization != None) and (annualization != False):
        cum_ret = (1 + cum_ret) ** (annualization / len(return_series)) - 1

    return cum_ret



def volatility(return_series, annualization=252):
    """
    Calculate the volatility of a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    annualization : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor.
        For example, 252 for trading days in a year. Default is 252.

    Returns
    -------
    vol : float
        The volatility of the series over the period
    """

    if len(return_series) == 0:
        raise ValueError("The return series is empty")

    vol = np.std(return_series, ddof=1)  # Using ddof=1 for sample standard deviation

    if (annualization != None) and (annualization != False):
        vol *= np.sqrt(annualization)

    return vol



def sharpe_ratio(return_series, annualize_returns=None, annualize_volatility=252):
    """
    Calculate the Sharpe ratio of a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    annualize_returns : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor for returns.

    annualize_volatility : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor for volatility.

    Returns
    -------
    sharpe : float
        The Sharpe ratio of the series over the period.
    """

    if len(return_series) == 0:
        raise ValueError("The return series is empty")
    
    sharpe = (cumulative_return(return_series, annualization=annualize_returns) /
                    volatility(return_series, annualization=annualize_volatility))

    return sharpe



def downside_volatility(return_series, annualization=252):
    """
    Calculate the downside volatility of a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    annualization : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor.
        For example, 252 for trading days in a year. Default is 252.

    Returns
    -------
    downside_vol : float
        The downside volatility of the series over the period
    """

    if len(return_series) == 0:
        raise ValueError("The return series is empty")

    return_series = return_series[return_series < 0]
    downside_vol = np.std(return_series, ddof=1)  # Using ddof=1 for sample standard deviation

    if (annualization != None) and (annualization != False):
        downside_vol *= np.sqrt(annualization)

    return downside_vol



def sortino_ratio(return_series, annualize_returns=None, annualize_downsidevol=252):
    """
    Calculate the Sortino ratio of a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    annualize_returns : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor for returns.

    annualize_volatility : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor for volatility.

    Returns
    -------
    sortino : float
        The Sortino ratio of the series over the period.
    """

    if len(return_series) == 0:
        raise ValueError("The return series is empty")
    
    sortino = (cumulative_return(return_series, annualization=annualize_returns) /
                    downside_volatility(return_series, annualization=annualize_downsidevol))

    return sortino



def max_drawdown(return_series):
    """
    Calculate the maximum drawdown of a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    Returns
    -------
    max_dd : dict
        A dictionary containing the maximum drawdown of the series over the period, the date of the peak and the date of the trough
    """

    if len(return_series) == 0:
        raise ValueError("The return series is empty")
    
    cumulative = (1 + return_series).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max

    max_dd = {}
    max_dd['max_drawdown'] = drawdown.min()
    max_dd['maxdd_start'] = cumulative[:drawdown.idxmin()].idxmax().strftime('%Y-%m-%d')
    max_dd['maxdd_end'] = drawdown.idxmin().strftime('%Y-%m-%d')
    
    return max_dd



def stats_table(return_series, annualize_returns=None, annualize_volatility=252):
    """
    Calculate financial metrics from a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    annualize_returns : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor for returns.

    annualize_volatility : int or None
        If None, no annualization is applied. If an int, it is used as the annualization factor for volatility or downside vol.

    Returns
    -------
    stats_table : pandas.DataFrame
        Table with financial metrics.
    """

    stats = {}
    stats['start_date'] = return_series.index.min()
    stats['end_date'] = return_series.index.max()
    stats['return'] = cumulative_return(return_series, annualization = annualize_returns)
    stats['volatility'] = volatility(return_series, annualization = annualize_volatility)
    stats['sharpe_ratio'] = sharpe_ratio(return_series, annualize_returns = annualize_returns, annualize_volatility = annualize_volatility)
    stats['sortino_ratio'] = sortino_ratio(return_series, annualize_returns = annualize_returns, annualize_downsidevol = annualize_volatility)
    stats['max_drawdown'] = max_drawdown(return_series)['max_drawdown']
    stats['maxdd_start'] = max_drawdown(return_series)['maxdd_start']
    stats['maxdd_end'] = max_drawdown(return_series)['maxdd_end']

    stats = pd.DataFrame(stats, index=[0])

    return stats



def value_at_risk(return_series, p=0.05):
    """
    Calculate Historical, Parametric and MonteCarlo VaR at level p from a series of returns.

    Parameters
    ----------
    return_series : pandas.Series
        Series with the daily returns and date as index.

    Returns
    -------
    var : pandas.DataFrame
        Dataframe with VaRs
    """
    
    var = {}

    # Historical VaR
    var['Historical VaR'] = np.percentile(return_series, p)

    # Parametric VaR
    mu = np.mean(return_series)
    sigma = np.std(return_series, ddof=1)
    var['Parametric VaR'] = mu + sigma * norm.ppf(p)

    # MC VaR
    simulations = 10000
    simulated_returns = np.random.normal(np.mean(return_series), np.std(return_series, ddof=1), size=(simulations, len(return_series)))
    var['MonteCarlo VaR'] = pd.DataFrame(simulated_returns).T.apply(lambda x: np.percentile(x, p)).mean()

    var = pd.DataFrame(var, index=[f'p = {p}']).T

    return var



def distribution_properties(return_series, hist_max_return=0.2):

    plt.figure(figsize=(10, 5))
    plt.hist(return_series, bins=np.linspace(-hist_max_return, hist_max_return, int(200*hist_max_return)+1), edgecolor='k', density=True)
    plt.title('Distribution of Returns')
    plt.ylabel('Normalized Frequency (%)')
    plt.grid(True)
    plt.show()


    stats_prop = {}

    stats_prop['Mean'] = np.mean(return_series)
    stats_prop['Standard Dev.'] = np.std(return_series, ddof=1)
    stats_prop['Skewness'] = skew(return_series)
    stats_prop['Kurtosis'] = kurtosis(return_series)
    stats_prop['Min'] = np.min(return_series)
    stats_prop['Percentile 1st'] = np.percentile(return_series, 1)
    stats_prop['Percentile 5th'] = np.percentile(return_series, 5)
    stats_prop['Percentile 10th'] = np.percentile(return_series, 10)
    stats_prop['Percentile 25th'] = np.percentile(return_series, 25)
    stats_prop['Median'] = np.percentile(return_series, 50)
    stats_prop['Percentile 75th'] = np.percentile(return_series, 75)
    stats_prop['Percentile 90th'] = np.percentile(return_series, 90)
    stats_prop['Percentile 95th'] = np.percentile(return_series, 95)
    stats_prop['Percentile 99th'] = np.percentile(return_series, 99)
    stats_prop['Max'] = np.max(return_series)

    stats_prop = round(pd.DataFrame(stats_prop, index=['Statistics (%)']).T * 100, 2)

    return stats_prop



def historical_correlation(list_of_securities, date, prices, lookback_wdw=63, show_fig=True):
    """
    Calculates and optionally displays the historical correlation matrix of selected securities' returns.

    Parameters
    ----------
    list_of_securities : list
        List of security identifiers to include in the correlation calculation.
    date : str or pd.Timestamp
        The end date up to which the historical returns are considered.
    prices : pd.DataFrame
        DataFrame containing price data with columns 'date', 'security_id', and 'price_usd'.
    lookback_wdw : int, optional
        Number of trading days to look back for calculating historical returns (default is 63).
    show_fig : bool, optional
        If True, displays the correlation matrix as a heatmap. If False, returns the correlation matrix.

    Returns
    -------
    pd.DataFrame or None
        Correlation matrix of the selected securities' returns if show_fig is False. Otherwise, displays a heatmap.
    """

    pivoted_prices = prices.pivot(index = 'date', columns = 'security_id', values = 'price_usd')
    pivoted_prices = pivoted_prices[pivoted_prices.index.dayofweek < 5].pct_change()

    temp_rets = pivoted_prices.loc[:date, list_of_securities].iloc[-lookback_wdw:].copy()
    corr_mat = temp_rets.corr()

    mask_nan = []
    for i in range(len(corr_mat)):
        for j in range(len(corr_mat)):
            if j>i:
                mask_nan.append((i,j))

    for i in mask_nan:
        corr_mat.iloc[i[0], i[1]] = np.nan

    corr_mat.index.name, corr_mat.columns.name = '', ''

    if show_fig == True:
        _, ax = plt.subplots(figsize=(len(list_of_securities), len(list_of_securities)))
        sns.heatmap(corr_mat, annot=True, ax=ax, cmap='coolwarm', square=True, cbar_kws={"shrink": .75}, vmin=-1, vmax=1
                    ).set_title(f"Returns' Correlation Matrix \nfrom {str(temp_rets.index.min())[:10]} to {str(temp_rets.index.max())[:10]} ({lookback_wdw} days)")
        plt.show()
    else:
        return corr_mat
