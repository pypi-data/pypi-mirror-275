# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:00:34 2022

@author: dingq
"""
from dqlib.datetime import to_business_day_convention, to_period
from dqlib.proto.dqproto import *
from dqlib.staticdata import create_static_data


def to_time_series_mode(src):
    '''
    Convert a string to TimeSeries.Mode.
    
    Parameters
    ----------
    src : str
        a string of frequency, i.e. 'TS_FORWARD_MODE'.
    
    Returns
    -------
    None.

    '''
    if src in ['', 'nan']:
        return TS_FORWARD_MODE
    else:
        return TimeSeries.Mode.DESCRIPTOR.values_by_name[src.upper()].number


# Time Series
def create_time_series(dates,
                       values,
                       mode=TimeSeries.Mode.TS_FORWARD_MODE,
                       name=''):
    '''
    Create a time series.
    
    Parameters
    ----------
    dates : list
        A list of dates.The dates are type of Date.
    values : list
        A list of floating numbers.
    mode : TimeSeries.Mode, optional
        Mode indicates the time series is in the date ascending (forward) or descending (backward) order. The default is 'TS_FORWARD_MODE'.
    name : str, optional
        Name of time series given by user. The default is ''.
    
    Returns
    -------
    TimeSeries
        A time series object.
    
    '''
    p_values = dqCreateProtoMatrix(len(values), 1, values, Matrix.StorageOrder.ColMajor)
    return dqCreateProtoTimeSeries(dates, p_values, mode, name.upper())


# Currency Pair
def to_ccy_pair(src):
    '''
    Create a currency pair. 
    
    Parameters
    ----------
    src : str
        a string of 6 chars, i.e. 'USDCNY', 'usdcny'.
    
    Returns
    -------
    CurrencyPair
        Object of CurrencyPair.
    
    '''
    left = src[0:3]
    right = src[3:6]
    return dqCreateProtoCurrencyPair(dqCreateProtoCurrency(left.upper()),
                                     dqCreateProtoCurrency(right.upper()))


def create_foreign_exchange_rate(value,
                                 base_currency,
                                 target_currency):
    """
    创建一个外汇利率对象.

    Parameters
    ----------
    value: float
    base_currency: str
    target_currency: str

    Returns
    -------
    ForeignExchangeRate

    """
    return dqCreateProtoForeignExchangeRate(value,
                                            base_currency,
                                            target_currency)


def create_fx_spot_rate(fx_rate,
                        ref_date,
                        spot_date):
    """
    创建一个外汇即期利率对象.

    Parameters
    ----------
    fx_rate: ForeignExchangeRate
    ref_date: Date
    spot_date: Date

    Returns
    -------
    FxSpotRate

    """
    return dqCreateProtoFxSpotRate(fx_rate,
                                   ref_date,
                                   spot_date)


def create_fx_spot_template(inst_name,
                            currency_pair,
                            spot_day_convention,
                            calendars,
                            spot_delay):
    """
    Create a fx spot template object.

    :param inst_name: str
    :param currency_pair: str
    :param spot_day_convention: str
    :param calendars: list
    :param spot_delay: str
    :return: FxSpotTemplate
    """
    p_type = FX_SPOT
    p_currency_pair = to_ccy_pair(currency_pair)
    p_spot_day_convention = to_business_day_convention(spot_day_convention)
    p_spot_delay = to_period(spot_delay)
    pb_data = dqCreateProtoFxSpotTemplate(p_type,
                                          inst_name,
                                          p_currency_pair,
                                          p_spot_day_convention,
                                          calendars,
                                          p_spot_delay)
    pb_data_list = dqCreateProtoFxSpotTemplateList([pb_data])
    create_static_data(SDT_FX_SPOT, pb_data_list.SerializeToString())
    return pb_data
