# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 23:43:29 2022

@author: dingq
"""

import unittest

from dqlib.analytics import *
from dqlib.fianalytics import *
from dqlib.fimarket import *


class TestFiAnalytics(unittest.TestCase):
    def setUp(self):
        self.cal = 'CAL_CFETS'
        create_calendar(self.cal, [44654, 44954], [44655])

        self.currency = 'CNY'
        self.as_of_date = create_date(2021, 7, 22)

        self.cny_treas_zero_1m = create_std_zero_cpn_bond_template('cny_treas_zero_1m', to_period('1m'), self.currency,
                                                                   self.cal)
        self.cny_treas_cpn_a_3m = create_std_fixed_cpn_bond_template('cny_treas_cpn_a_3m', to_period('3m'),
                                                                     self.currency, self.cal)
        self.cny_treas_cpn_a_6m = create_std_fixed_cpn_bond_template('cny_treas_cpn_a_6m', to_period('6m'),
                                                                     self.currency, self.cal)
        self.cny_treas_cpn_a_9m = create_std_fixed_cpn_bond_template('cny_treas_cpn_a_9m', to_period('9m'),
                                                                     self.currency, self.cal)
        self.cny_treas_cpn_a_1y = create_std_fixed_cpn_bond_template('cny_treas_cpn_a_1y', to_period('1y'),
                                                                     self.currency, self.cal)
        self.cny_treas_cpn_a_2y = create_std_fixed_cpn_bond_template('cny_treas_cpn_a_2y', to_period('2Y'),
                                                                     self.currency, self.cal)
        self.cny_treas_cpn_a_3y = create_std_fixed_cpn_bond_template('cny_treas_cpn_a_3y', to_period('3Y'),
                                                                     self.currency, self.cal)
        self.cny_treas_cpn_a_5y = create_std_fixed_cpn_bond_template('cny_treas_cpn_a_5y', to_period('5Y'),
                                                                     self.currency, self.cal)
        self.cny_treas_cpn_sa_7y = create_std_fixed_cpn_bond_template('cny_treas_cpn_sa_7y', to_period('7Y'),
                                                                      self.currency, self.cal)
        self.cny_treas_cpn_sa_10y = create_std_fixed_cpn_bond_template('cny_treas_cpn_sa_10y', to_period('10Y'),
                                                                       self.currency, self.cal)
        self.cny_treas_cpn_sa_15y = create_std_fixed_cpn_bond_template('cny_treas_cpn_sa_15y', to_period('15Y'),
                                                                       self.currency, self.cal)
        self.cny_treas_cpn_sa_20y = create_std_fixed_cpn_bond_template('cny_treas_cpn_sa_20y', to_period('20Y'),
                                                                       self.currency, self.cal)
        self.cny_treas_cpn_sa_30y = create_std_fixed_cpn_bond_template('cny_treas_cpn_sa_30y', to_period('30Y'),
                                                                       self.currency, self.cal)

        self.cny_mtn_aaa_cpn_a_1m = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_1m', to_period('1M'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_3m = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_3m', to_period('3M'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_6m = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_6m', to_period('6M'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_9m = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_9m', to_period('9M'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_1y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_1y', to_period('1Y'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_2y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_2y', to_period('2Y'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_3y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_3y', to_period('3Y'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_4y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_4y', to_period('4Y'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_5y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_5y', to_period('5Y'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_7y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_7y', to_period('7Y'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_8y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_8y', to_period('8Y'),
                                                                       self.currency, self.cal)
        self.cny_mtn_aaa_cpn_a_9y = create_std_fixed_cpn_bond_template('cny_mtn_aaa_cpn_a_9y', to_period('9Y'),
                                                                       self.currency, self.cal)

        self.cny_treas_cpn_bond_200014_template = create_fixed_cpn_bond_template('cny_treas_cpn_bond_200014',
                                                                                 create_date(2020, 10, 9), 1,
                                                                                 create_date(2020, 10, 10),
                                                                                 to_period('5Y'),
                                                                                 2.15e-2, self.currency, self.cal,
                                                                                 frequency=ANNUAL,
                                                                                 day_count=ACT_365_FIXED,
                                                                                 issue_price=100.0,
                                                                                 interest_day_convention=MODIFIED_FOLLOWING,
                                                                                 stub_policy=INITIAL,
                                                                                 broken_period_type=LONG,
                                                                                 pay_day_offset=0,
                                                                                 pay_day_convention=MODIFIED_FOLLOWING,
                                                                                 ex_cpn_period=to_period('0d'),
                                                                                 ex_cpn_calendar='',
                                                                                 ex_cpn_day_convention=INVALID_BUSINESS_DAY_CONVENTION,
                                                                                 ex_cpn_eom=False)

        self.cny_treas_std_cfets_name = 'cny_treas_std_cfets'
        bond_names = ['CNY_TREAS_ZERO_1M',
                      'CNY_TREAS_CPN_A_3M',
                      'CNY_TREAS_CPN_A_6M',
                      'CNY_TREAS_CPN_A_9M',
                      'CNY_TREAS_CPN_A_1Y',
                      'CNY_TREAS_CPN_A_2Y',
                      'CNY_TREAS_CPN_A_3Y',
                      'CNY_TREAS_CPN_A_5Y',
                      'CNY_TREAS_CPN_SA_7Y',
                      'CNY_TREAS_CPN_SA_10Y',
                      'CNY_TREAS_CPN_SA_15Y',
                      'CNY_TREAS_CPN_SA_20Y',
                      'CNY_TREAS_CPN_SA_30Y']
        bond_quotes = [1.7112E-02,
                       1.8317E-02,
                       1.9413E-02,
                       1.9500E-02,
                       2.1563E-02,
                       2.4985E-02,
                       2.5538E-02,
                       2.7550E-02,
                       2.9175E-02,
                       2.9263E-02,
                       3.2984E-02,
                       3.3462E-02,
                       3.5023E-02]

        self.par_cny_treas_std_cfets = create_bond_par_curve(self.as_of_date, self.currency,
                                                             bond_names, bond_quotes,
                                                             YIELD_TO_MATURITY, self.cny_treas_std_cfets_name)

        build_settings = create_bond_curve_build_settings(self.cny_treas_std_cfets_name, ZERO_RATE, LINEAR_INTERP,
                                                          FLAT_EXTRAP)

        self.cny_treas_std_cfets = build_bond_yield_curve(build_settings, self.cny_treas_std_cfets_name,
                                                          self.as_of_date, self.par_cny_treas_std_cfets,
                                                          day_count=ACT_365_FIXED,
                                                          compounding_type=CONTINUOUS_COMPOUNDING, freq=ANNUAL,
                                                          build_method=BOOTSTRAPPING_METHOD, calc_jacobian=False,
                                                          fwd_curve=None)

        self.cny_mtn_aaa_sprd_std_cfets_name = 'cny_mtn_aaa_sprd_std_cfets'
        bond_names = ['CNY_MTN_AAA_CPN_A_1M',
                      'CNY_MTN_AAA_CPN_A_3M',
                      'CNY_MTN_AAA_CPN_A_6M',
                      'CNY_MTN_AAA_CPN_A_9M',
                      'CNY_MTN_AAA_CPN_A_1Y',
                      'CNY_MTN_AAA_CPN_A_2Y',
                      'CNY_MTN_AAA_CPN_A_3Y',
                      'CNY_MTN_AAA_CPN_A_4Y',
                      'CNY_MTN_AAA_CPN_A_5Y',
                      'CNY_MTN_AAA_CPN_A_7Y',
                      'CNY_MTN_AAA_CPN_A_8Y',
                      'CNY_MTN_AAA_CPN_A_9Y']
        bond_quotes = [0.022916,
                       0.024213,
                       0.025822,
                       0.026675,
                       0.027216,
                       0.028916,
                       0.031112,
                       0.032824,
                       0.033816,
                       0.036816,
                       0.037026,
                       0.037311]
        self.par_cny_mtn_aaa_sprd_std_cfets = create_bond_par_curve(self.as_of_date, self.currency,
                                                                    bond_names, bond_quotes,
                                                                    YIELD_TO_MATURITY,
                                                                    self.cny_mtn_aaa_sprd_std_cfets_name)
        build_settings = create_bond_curve_build_settings(self.cny_mtn_aaa_sprd_std_cfets_name,
                                                          ZERO_RATE, LINEAR_INTERP, FLAT_EXTRAP)
        self.cny_mtn_aaa_sprd_std_cfets = build_bond_sprd_curve(build_settings, self.cny_mtn_aaa_sprd_std_cfets_name,
                                                                self.as_of_date, self.par_cny_mtn_aaa_sprd_std_cfets,
                                                                self.cny_treas_std_cfets,
                                                                build_method=BOOTSTRAPPING_METHOD, calc_jacobian=False,
                                                                fwd_curve=None)

    def test_create_bond_yield_curve_build_settings(self):
        expected = b'\n\tCNY_TREAS\x18\x01 \x01'
        test = create_bond_curve_build_settings('CNY_TREAS', ZERO_RATE,
                                                LINEAR_INTERP, FLAT_EXTRAP)
        # print(test.SerializeToString())
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_bond_par_curve(self):
        expected = b'\n\x07\x08\xe5\x0f\x10\x07\x18\x16\x12\x03CNY\x1a\x18\n\rCNYGOVBOND_1Y\x11\x9a\x99\x99\x99\x99\x99\x99?\x1a\x18\n\rCNYGOVBOND_2Y\x11y\xe9&1\x08\xac\x9c?*\tCNY_TREAS'
        test = create_bond_par_curve(self.as_of_date, self.currency,
                                     ['CNYGOVBOND_1Y', 'CNYGOVBOND_2Y'],
                                     [2.5e-2, 2.8e-2],
                                     YIELD_TO_MATURITY, 'CNY_TREAS')
        # print('test_create_bond_par_curve', test.SerializeToString())
        self.assertEqual(test.SerializeToString(), expected)

    def test_bond_yield_curve_builder(self):
        expected = b'\x12\xc2\x02\n\xbd\x02\n\x07\x08\xe5\x0f\x10\x07\x18\x16\x10\x02\x1a\x07\x08\xe5\x0f\x10\x08\x18\x17\x1a\x07\x08\xe5\x0f\x10\n\x18\x19\x1a\x07\x08\xe6\x0f\x10\x01\x18\x18\x1a\x07\x08\xe6\x0f\x10\x04\x18\x19\x1a\x07\x08\xe6\x0f\x10\x07\x18\x19\x1a\x07\x08\xe7\x0f\x10\x07\x18\x18\x1a\x07\x08\xe8\x0f\x10\x07\x18\x17\x1a\x07\x08\xea\x0f\x10\x07\x18\x17\x1a\x07\x08\xec\x0f\x10\x07\x18\x18\x1a\x07\x08\xef\x0f\x10\x07\x18\x17\x1a\x07\x08\xf4\x0f\x10\x07\x18\x17\x1a\x07\x08\xf9\x0f\x10\x07\x18\x17\x1a\x07\x08\x83\x10\x10\x07\x18\x18"\x021M"\x023M"\x026M"\x029M"\x021Y"\x022Y"\x023Y"\x025Y"\x027Y"\x0310Y"\x0315Y"\x0320Y"\x0330Y*j\nh\x13\x1e\xab=\xdd\xd4\x90?\xeb\xfbs\x86(d\x92?\x94.A\x1c#\x95\x93?\x1dg\xd6sT\xb4\x93?\xc5e\x99\x1eU\xc9\x95?Z[)\xa5X<\x99?Uvc=\x8d\xcc\x99?6\x92\x94Wy\xd0\x9b?\x135f\xb2\xa9o\x9d?\xc5\xafH\xe8\xf3\x86\x9d?\xfe^\x08\xb2\xbb\x9c\xa0?{\x0b \x85\x8e\xd9\xa0?KZ/\x94\x90\x9f\xa1?0\x018\x01B\x13CNY_TREAS_STD_CFETS\x10\x01\x1a\x03CNY \x01'
        curve_name = 'cny_treas_std_cfets'
        currency = 'CNY'
        build_settings = create_bond_curve_build_settings(curve_name, ZERO_RATE, LINEAR_INTERP, FLAT_EXTRAP)
        test = build_bond_yield_curve(build_settings, curve_name, self.as_of_date, self.par_cny_treas_std_cfets,
                                      day_count=ACT_365_FIXED, compounding_type=CONTINUOUS_COMPOUNDING, freq=ANNUAL,
                                      build_method=BOOTSTRAPPING_METHOD, calc_jacobian=False,
                                      fwd_curve=None)
        #print('test_bond_yield_curve_builder', test.SerializeToString())
        # print(curve_name)
        # print(print_term_structure_curve(test.curve.curve))
        self.assertEqual(test.SerializeToString(), expected)

    def test_bond_spread_curve_builder(self):
        expected =  b'\n\xab\x02\n\x07\x08\xe5\x0f\x10\x07\x18\x16\x10\x02\x1a\x07\x08\xe5\x0f\x10\x08\x18\x17\x1a\x07\x08\xe5\x0f\x10\n\x18\x19\x1a\x07\x08\xe6\x0f\x10\x01\x18\x18\x1a\x07\x08\xe6\x0f\x10\x04\x18\x19\x1a\x07\x08\xe6\x0f\x10\x07\x18\x19\x1a\x07\x08\xe7\x0f\x10\x07\x18\x18\x1a\x07\x08\xe8\x0f\x10\x07\x18\x17\x1a\x07\x08\xe9\x0f\x10\x07\x18\x17\x1a\x07\x08\xea\x0f\x10\x07\x18\x17\x1a\x07\x08\xec\x0f\x10\x07\x18\x18\x1a\x07\x08\xed\x0f\x10\x07\x18\x17\x1a\x07\x08\xee\x0f\x10\x07\x18\x17"\x021M"\x023M"\x026M"\x029M"\x021Y"\x022Y"\x023Y"\x024Y"\x025Y"\x027Y"\x028Y"\x029Y*b\n`4\x1a<@\x15\x94v?\xaa\xb7\x13q\xf7ew?s\xa8\xd3\xd5`\x88y?\xa9\x87\xd2=<\x9f|?\x19\x03\x9e\xfa\xc2\x8av?l\x84C\xe1\x99Po?!\xb3\xe9@\x9a.v?\x8b!x\x94n\xf8x?{\xcd\x94fO\xe3x?\x06\xbbj\x98@I~?.I\x97wc\x00\x7f?\x9e.J\xa1f\x01\x80?0\x038\x01B\x1aCNY_MTN_AAA_SPRD_STD_CFETS'
        curve_name = 'cny_mtn_aaa_sprd_std_cfets'
        build_settings = create_bond_curve_build_settings(curve_name, ZERO_RATE, LINEAR_INTERP, FLAT_EXTRAP)
        test = build_bond_sprd_curve(build_settings, curve_name,
                                     self.as_of_date, self.par_cny_mtn_aaa_sprd_std_cfets,
                                     self.cny_treas_std_cfets,
                                     build_method=BOOTSTRAPPING_METHOD, calc_jacobian=False,
                                     fwd_curve=None)
        #print('test_bond_spread_curve_builder', test.SerializeToString())
        # print(curve_name)
        # print(print_term_structure_curve(test.curve))
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_fi_mkt_data_set(self):
        expected = b'\n\x07\x08\xe6\x0f\x10\x03\x18\t\x12X\x12;\n7\n\x07\x08\xe6\x0f\x10\x03\x18\t\x10\x02\x1a\x07\x08\xe6\x0f\x10\x03\x18\n\x1a\x07\x08\xe9\x0f\x10\x03\x18\n"\x00*\x12\n\x10{\x14\xaeG\xe1z\x94?\x9a\x99\x99\x99\x99\x99\x99?0\x018\x01\x10\x01\x1a\x03CNY \x01:\x12\x12\x10\x08\x01\x10\x01\x1a\x08\x00\x00\x00\x00\x00\x00\x00\x00 \x01\x1a9\n7\n\x07\x08\xe6\x0f\x10\x03\x18\t\x10\x02\x1a\x07\x08\xe6\x0f\x10\x03\x18\n\x1a\x07\x08\xe9\x0f\x10\x03\x18\n"\x00*\x12\n\x10\xfc\xa9\xf1\xd2Mb`?{\x14\xaeG\xe1zd?0\x018\x01"\x00'
        as_of_date = create_date(2022, 3, 9)
        discount_curve = create_ir_yield_curve(as_of_date, 'CNY', [create_date(2022, 3, 10), create_date(2025, 3, 10)],
                                               [0.02, 0.025])
        cs_curve = create_credit_curve(create_date(2022, 3, 9), [create_date(2022, 3, 10), create_date(2025, 3, 10)],
                                       [0.2e-2, 0.25e-2])
        fwd_curve = IrYieldCurve()
        test = create_fi_mkt_data_set(as_of_date, discount_curve, cs_curve, fwd_curve)
        #print('test_create_fi_mkt_data_set', test.SerializeToString())
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_fi_risk_settings(self):
        expected = b'\n\x1b!-C\x1c\xeb\xe26\x1a?){\x14\xaeG\xe1zt?A-C\x1c\xeb\xe26\x1a?\x12\x0b\x10\x01\x19\x1ag\x016\x9fqf?\x1a\x12!-C\x1c\xeb\xe26\x1a?A-C\x1c\xeb\xe26\x1a?'
        ir_curve_settings = create_ir_curve_risk_settings()
        cs_curve_settings = create_credit_curve_risk_settings()
        theta_settings = create_theta_risk_settings()
        test = create_fi_risk_settings(ir_curve_settings, cs_curve_settings, theta_settings)
        self.assertEqual(test.SerializeToString(), expected)

    def test_vanilla_bond_pricer(self):
        expected = 972343.084988016
        bond = build_fixed_cpn_bond(1000000.0, self.cny_treas_cpn_bond_200014_template)
        mkt_data = create_fi_mkt_data_set(self.as_of_date, self.cny_treas_std_cfets, self.cny_mtn_aaa_sprd_std_cfets,
                                          self.cny_treas_std_cfets)
        ir_curve_settings = create_ir_curve_risk_settings()
        cs_curve_settings = create_credit_curve_risk_settings()
        theta_settings = create_theta_risk_settings()
        risk_settings = create_fi_risk_settings(ir_curve_settings, cs_curve_settings, theta_settings)
        pricing_settings = create_model_free_pricing_settings()
        test = vanilla_bond_pricer(bond, self.as_of_date, mkt_data, pricing_settings, risk_settings)
        self.assertEqual(test.present_value, expected)

    def test_vanilla_bond_greeks(self):
        expected = b'\t\x9b\x8c\x83+n\xac-A\x1a\xef\x07\n?\n\x0eCURVATURE_DOWN\x12-\n\rINTEREST_RATE\x12\x1c\n\x03CNY\x12\x15\n\n\n\x08\x9c\x9b\x870GF.A\x12\x05TOTAL\x1a\x00\n=\n\x0cCURVATURE_UP\x12-\n\rINTEREST_RATE\x12\x1c\n\x03CNY\x12\x15\n\n\n\x08\x91\x83\x9e\x9c\xbf\x15-A\x12\x05TOTAL\x1a\x00\n\x9d\x03\n\x05DELTA\x12\xc0\x01\n\x06CREDIT\x12\xb5\x01\n\x1aCNY_MTN_AAA_SPRD_STD_CFETS\x12\x96\x01\nb\n`\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0?\xec\x95}\xb2\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00:\xe4\x8a\xae\xbc\xd8\xc0\x80S H\xb7\xc9\xe5\xc0\x004\x1d\xc7\x92\xa4\xee\xc0:\x9f\xaa\xa7>\xb0L\xc1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x021M\x12\x023M\x12\x026M\x12\x029M\x12\x021Y\x12\x022Y\x12\x023Y\x12\x024Y\x12\x025Y\x12\x027Y\x12\x028Y\x12\x029Y\x1a\x00\x12\xd0\x01\n\rINTEREST_RATE\x12\xbe\x01\n\x13CNY_TREAS_STD_CFETS\x12\xa6\x01\nj\nh\x00\xd0\xa3\xb5\xa1o\x90\xc0\x00`\xc1\xfdZ\xc3\xac\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xed\x0cw\x13\x81\xd3\xc0\x00\x10\xe0\x8c\x91\xbf\xe3\xc0\x00rR\xd1\x87z7\xc1\xa4o\xe8\xcc,\x80A\xc1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x021M\x12\x023M\x12\x026M\x12\x029M\x12\x021Y\x12\x022Y\x12\x023Y\x12\x025Y\x12\x027Y\x12\x0310Y\x12\x0315Y\x12\x0320Y\x12\x0330Y\x1a\x00\n\xa6\x03\n\x0eDELTA_EXPOSURE\x12\xc0\x01\n\x06CREDIT\x12\xb5\x01\n\x1aCNY_MTN_AAA_SPRD_STD_CFETS\x12\x96\x01\nb\n`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xb7\x81K\xde\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb4\xa1\xbbC\x04\xc0\x00\x00\x97\xd0C\xd9\x11\xc0\x00\x00\xe8DF\x1a\x19\xc0\x00\xb4w\xc1g\x80w\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x021M\x12\x023M\x12\x026M\x12\x029M\x12\x021Y\x12\x022Y\x12\x023Y\x12\x024Y\x12\x025Y\x12\x027Y\x12\x028Y\x12\x029Y\x1a\x00\x12\xd0\x01\n\rINTEREST_RATE\x12\xbe\x01\n\x13CNY_TREAS_STD_CFETS\x12\xa6\x01\nj\nh\x00\x00@\xa3\xc8\xed\xba\xbf\x00\x00\xc0\x8e\x0f\x90\xd7\xbf\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf4\xe0\xa7\xf4\xff\xbf\x00\x00 \x92\x85-\x10\xc0\x00\x00$\x9d\xd3;c\xc0\x00\x90\xcf\x97Q\xacl\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x12\x021M\x12\x023M\x12\x026M\x12\x029M\x12\x021Y\x12\x022Y\x12\x023Y\x12\x025Y\x12\x027Y\x12\x0310Y\x12\x0315Y\x12\x0320Y\x12\x0330Y\x1a\x00\n$\n\x05THETA\x12\x1b\n\x05THETA\x12\x12\x12\x10\n\n\n\x08\x00\x00\xe0\xef\xba\x07X@\x12\x00\x1a\x00"\x9e\x04\x11\x9b\x8c\x83+n\xac-A"`\n\x07\x08\xe4\x0f\x10\n\x18\x0c\x12\x07\x08\xe5\x0f\x10\n\x18\x0b\x1a\x07\x08\xe4\x0f\x10\n\x18\x0c"\n\n\x08\x99\xfe\xc9`\x8e\xe9\xef?)j\xbct\x93\x18\x04\x96?1-\xa0\xc5q\xb0\xd5\xef?9\xc4\x88\x11#F\xf0\xd4@A\xbf\xf1\xc5\xb8\x96\xd4\xd4@J\x07\x08\xe5\x0f\x10\n\x18\x0bR\n\n\x08\x00\x00\x00\x00\x00\x00\x00\x00"`\n\x07\x08\xe5\x0f\x10\n\x18\x0b\x12\x07\x08\xe6\x0f\x10\n\x18\n\x1a\x07\x08\xe5\x0f\x10\n\x18\x0b"\n\n\x08\x99\xfe\xc9`\x8e\xe9\xef?)j\xbct\x93\x18\x04\x96?1\x04~x\xee9\x02\xef?9\xc4\x88\x11#F\xf0\xd4@A.\xfda\xde8J\xd4@J\x07\x08\xe6\x0f\x10\n\x18\nR\n\n\x08\x00\x00\x00\x00\x00\x00\x00\x00"`\n\x07\x08\xe6\x0f\x10\n\x18\n\x12\x07\x08\xe7\x0f\x10\n\x18\n\x1a\x07\x08\xe6\x0f\x10\n\x18\n"\n\n\x08\x00\x00\x00\x00\x00\x00\xf0?)j\xbct\x93\x18\x04\x96?1\xc6\xa3ik[\xed\xed?9\x00\x00\x00\x00\x00\xff\xd4@A-\xf8\xa1\x93\xd4\xa2\xd3@J\x07\x08\xe7\x0f\x10\n\x18\nR\n\n\x08\x00\x00\x00\x00\x00\x00\x00\x00"`\n\x07\x08\xe7\x0f\x10\n\x18\n\x12\x07\x08\xe8\x0f\x10\n\x18\n\x1a\x07\x08\xe7\x0f\x10\n\x18\n"\n\n\x08\xb4\x00\x9b\xcf8\x0b\xf0?)j\xbct\x93\x18\x04\x96?1\x9e\xd9JBM\xe9\xec?9<w\xee\xdc\xb9\r\xd5@A\x89\x1aFg\x81\x05\xd3@J\x07\x08\xe8\x0f\x10\n\x18\nR\n\n\x08\x00\x00\x00\x00\x00\x00\x00\x00"`\n\x07\x08\xe8\x0f\x10\n\x18\n\x12\x07\x08\xe9\x0f\x10\n\x18\n\x1a\x07\x08\xe8\x0f\x10\n\x18\n"\n\n\x08\x00\x00\x00\x00\x00\x00\xf0?)j\xbct\x93\x18\x04\x96?1\x86\x08\x00_\xa4\xe6\xeb?9\x00\x00\x00\x00\x00\xff\xd4@A\x98\r5\xa9|N\xd2@J\x07\x08\xe9\x0f\x10\n\x18\nR\n\n\x08\x00\x00\x00\x00\x00\x00\x00\x002$\t\x86\x08\x00_\xa4\xe6\xeb?\x11\x00\x00\x00\x00\x80\x84.A\x19!d\xa9\x19\xc1\x9b*A"\x07\x08\xe9\x0f\x10\n\x18\nB\x03CNY*\x03CNY2J\nH\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        bond = build_fixed_cpn_bond(1000000.0, self.cny_treas_cpn_bond_200014_template)
        mkt_data = create_fi_mkt_data_set(self.as_of_date, self.cny_treas_std_cfets, self.cny_mtn_aaa_sprd_std_cfets,
                                          self.cny_treas_std_cfets)
        ir_curve_settings = create_ir_curve_risk_settings(True, False, True, granularity=TERM_BUCKET_RISK)
        cs_curve_settings = create_credit_curve_risk_settings(True, granularity=TERM_BUCKET_RISK)
        theta_settings = create_theta_risk_settings(True)
        risk_settings = create_fi_risk_settings(ir_curve_settings, cs_curve_settings, theta_settings)
        pricing_settings = create_model_free_pricing_settings('CNY', True, cash_flows=True)
        test = vanilla_bond_pricer(bond, self.as_of_date, mkt_data, pricing_settings, risk_settings)
        #print('test_vanilla_bond_greeks', test)
        #print('test_vanilla_bond_greeks', test.SerializeToString())
        self.assertEqual(test.SerializeToString(), expected)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFiAnalytics)
    unittest.TextTestRunner(verbosity=2).run(suite)
