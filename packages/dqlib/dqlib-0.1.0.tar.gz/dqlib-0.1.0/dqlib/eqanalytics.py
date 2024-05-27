# coding: utf-8
from dqlib.proto.dqproto import *
from dqlib.processrequest import *


# EQ Market Data Set:
def create_eq_mkt_data_set(as_of_date,
                           discount_curve,
                           dividend_curve,
                           underlying_price,
                           vol_surf,
                           quanto_discount_curve,
                           quanto_fx_vol_curve,
                           quanto_correlation,
                           underlying):
    """
    Create a set of market data.
    :param as_of_date: Date
    :param discount_curve: IrYieldCurve
    :param dividend_curve: DividendCurve
    :param underlying_price: double
    :param vol_surf: VolatilitySurface
    :param quanto_discount_curve: IrYieldCurve
    :param quanto_fx_vol_curve: VolatilityCurve
    :param quanto_correlation: double
    :param underlying: string
    :return: EqMktDataSet
    """
    return dqCreateProtoEqMktDataSet(as_of_date,
                                     discount_curve,
                                     dividend_curve,
                                     underlying_price,
                                     vol_surf,
                                     quanto_discount_curve,
                                     quanto_fx_vol_curve,
                                     quanto_correlation,
                                     underlying)


# Eq Volatility Surface
def build_eq_vol_surface(reference_date,
                         smile_method,
                         wing_strike_type,
                         lower,
                         upper,
                         option_quote_matrix,
                         underlying_prices,
                         discount_curve,
                         dividend_curve,
                         pricing_settings,
                         building_settings,
                         underlying):
    """
    Build Eq Volatility Surface.
    :param reference_date: Date
    :param smile_method: VolSmileMethod
    :param wing_strike_type: WingStrikeType
    :param lower: float
    :param upper: float
    :param option_quote_matrix: OptionQuoteMatrix
    :param underlying_prices: list
    :param discount_curve: IrYieldCurve
    :param dividend_curve: DividendCurve
    :param pricing_settings: PricingSettings
    :param building_settings: VolatilitySurfaceBuildSettings
    :param underlying: string
    :return:
    """
    definition = dqCreateProtoVolatilitySurfaceDefinition("",
                                                          smile_method,
                                                          "",
                                                          "",
                                                          "",
                                                          "",
                                                          "",
                                                          wing_strike_type,
                                                          lower,
                                                          upper)
    pb_input = dqCreateProtoEqVolatilitySurfaceBuildingInput(reference_date,
                                                             definition,
                                                             option_quote_matrix,
                                                             underlying_prices,
                                                             discount_curve,
                                                             dividend_curve,
                                                             building_settings,
                                                             pricing_settings,
                                                             underlying)
    req_name = "EQ_VOLATILITY_SURFACE_BUILDER"
    res_msg = process_request(req_name, pb_input.SerializeToString())
    pb_output = EqVolatilitySurfaceBuildingOutput()
    pb_output.ParseFromString(res_msg)
    if pb_output.success == False:
        raise Exception(pb_output.err_msg)
    return pb_output.volatility_surface




